
# 🔒 Secure Data Encryption System

A Streamlit-based web app that allows users to securely **store** and **retrieve** sensitive text data (like notes, passwords, etc.) using encrypted storage and passkey verification.

---

## 🚀 Features

- ✅ **User Sign-Up & Login** with password hashing (PBKDF2 + Salt)
- 🔐 **Encrypt Sensitive Data** using [Fernet symmetric encryption](https://cryptography.io/en/latest/fernet/)
- 🔍 **Retrieve & Decrypt Data** with passkey verification
- 🧠 **Brute-force Protection** — 3 wrong attempts = temporary lockout
- 💾 **Secure Storage** using JSON file
- 🔑 Auto-generated and persisted Fernet key

---

## 📁 Folder Structure

```
project/
│
├── secure_data.json       # Stored encrypted user data
├── secret.key             # Encryption key (auto-created)
├── app.py                 # Main Streamlit app
├── pyproject.toml         # Project dependencies (if using UV)
├── uv.lock                # Locked versions (if using UV)
└── .gitignore             # Git ignore file
```

---

## 🛡️ Security Details

- **Passkey Hashing**: Uses `PBKDF2-HMAC-SHA256` + salt
- **Data Encryption**: Uses Fernet encryption (AES 128 under the hood)
- **Lockout Mechanism**: 3 wrong attempts → 30 seconds lockout
- **Key Management**: `secret.key` is auto-generated and saved once

---

## 📦 Dependencies

- `streamlit`
- `cryptography`
- `hashlib`
- `base64`
- `json`, `os`, `time`

---

## 🤝 License

This project is for educational use. You can modify and use it in your own secure apps.

---

## ✍️ Author

Built with ❤️ by Ibad Ur Rehman(https://github.com/ibad363)