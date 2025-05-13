import streamlit as st
import os,json,time, base64
import hashlib
from cryptography.fernet import Fernet

data_file = "secure_data.json"

if not os.path.exists("secret.key"):
    with open("secret.key", "wb") as f:
        f.write(Fernet.generate_key())

with open("secret.key","rb") as f:
    KEY = f.read()

cipher = Fernet(KEY)

# -------- Utility Functions --------

def hash_passkey(passkey, salt=None):
    if salt is None:
        salt = os.urandom(16)
    hashed = hashlib.pbkdf2_hmac("sha256", passkey.encode(), salt, 100000)
    return base64.b64encode(salt + hashed).decode()

def encrypt_data(text):
    """Encrypt plain text using Fernet"""
    return cipher.encrypt(text.encode()).decode()

def decrypt_data(cipher_text):
    """Decrypt encrypted text using Fernet"""
    return cipher.decrypt(cipher_text.encode()).decode()

def load_data():
    """Load stored data from JSON file"""
    if os.path.exists(data_file):
        try:
            with open(data_file , "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}
    return {}

def save_data(data):
    """Save updated data to file"""
    with open(data_file, "w") as f:
        json.dump(data,f)

def verify_passkey(stored, input_passkey):
    decoded = base64.b64decode(stored)
    salt = decoded[:16]
    true_hash = decoded[16:]
    test_hash = hashlib.pbkdf2_hmac("sha256",input_passkey.encode(), salt,100000)
    return test_hash == true_hash


# -------- Global Variables --------

if "failed_attempts" not in st.session_state:
    st.session_state.failed_attempts = 0

if "lockout_until" not in st.session_state:
    st.session_state.lockout_until = None

if "current_user" not in st.session_state:
    st.session_state.current_user = None

stored_data = load_data()

# ------------ Streamlit UI -------------

st.title("🔒 Secure Data Encryption System")
menu = ["Home","Sign Up", "Login","Store Data", "Retreive Data"]
choice = st.sidebar.selectbox("Navigation", menu)

# ------------- Home -------------

if choice == "Home":
    st.subheader("Home")
    st.write("Securely **store and retrieve** data with a unique passkey.")

# ------------ Store Data -------------
elif choice == "Store Data":
    st.subheader("📂 Store New Data")
    label = st.text_input("Enter Label (like 'email' or 'note'):")
    text = st.text_area("Enter Data to Secure:")
    passkey = st.text_input("Enter Passkey: ",type="password")

    if st.button("Encrypt & Save"):
        if label and text and passkey:
            if st.session_state.current_user:
                user = st.session_state.current_user
                enc = encrypt_data(text)
                hased = hash_passkey(passkey)
                stored_data[user]["data"][label] = {"encrypted text": enc, "passkey": hased}
                save_data(stored_data)
                st.success("✅ Your data has been encrypted and saved.")
            else:
                st.warning("⛔ Please log in first")
        else:
            st.error("❗ Please fill all fields.")


# ------------ Retreive Data -------------
elif choice == "Retreive Data":
    st.subheader("🔍 Retrieve Your Data")

    label = st.text_input("Enter Label You Stored:")
    passkey = st.text_input("Enter Your Passkey:", type="password")

    if st.button("Decrypt"):
        if st.session_state.lockout_until and time.time() >= st.session_state.lockout_until:
            st.session_state.failed_attempts = 0
            st.session_state.lockout_until = None
        if st.session_state.lockout_until and time.time() < st.session_state.lockout_until:
            wait_time = int(st.session_state.lockout_until - time.time())
            st.warning(f"🔒 Locked out! Please wait {wait_time} seconds.")
        elif st.session_state.current_user:
            user = st.session_state.current_user
            if label in stored_data[user]["data"]:
                record = stored_data[user]["data"][label]
                stored_hash = record["passkey"]

                if verify_passkey(record["passkey"], passkey):
                    decrypted = decrypt_data(record["encrypted text"])
                    st.success(f"✅ Decrypted Text: {decrypted}")
                    st.session_state.failed_attempts = 0
                else:
                    st.session_state.failed_attempts += 1
                    remaining = 3 - st.session_state.failed_attempts
                    st.error(f"❌ Incorrect passkey! Attempts left: {remaining}")

                    if st.session_state.failed_attempts >= 3:
                        st.session_state.lockout_until = time.time() + 30
                        st.warning("🔒 Too many wrong attempts. Locked for 5 minutes..")
            else:
                st.error("❗ This label does not exist in your saved data.")
        else:
            st.warning("Please log in to retrieve data.")

elif choice == "Sign Up":
    st.subheader("📝 Create a New Account")
    username = st.text_input("Choose Username")
    password = st.text_input("Choose a strong passkey. Minimum 8 characters recommended." , type="password")

    if st.button("Register"):
        if username in stored_data:
            st.error("Username already exists!")
        else:
            hased = hash_passkey(password)
            stored_data[username] = {"password": hased, "data": {}}
            save_data(stored_data)
            st.success("✅ Account created. Please login.")

elif choice == "Login":
    st.subheader("🔐 Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if st.session_state.lockout_until and time.time() >= st.session_state.lockout_until:
            st.session_state.failed_attempts = 0
            st.session_state.lockout_until = None
        if st.session_state.lockout_until and time.time() < st.session_state.lockout_until:
            wait_time = int(st.session_state.lockout_until - time.time())
            st.warning(f"🔒 Locked out! Please wait {wait_time} seconds.")
        elif username in stored_data and verify_passkey(stored_data[username]["password"], password):
            st.session_state.current_user = username
            st.session_state.failed_attempts = 0
            st.success(f"✅ Logged in as: {username}")
        else:
            st.error("❌ Invalid crediantals!")
