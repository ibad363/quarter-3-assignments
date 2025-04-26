import requests  # For sending HTTP requests
import streamlit as st  # For making the web app

# ---- Function to Get Country Data ----
def fetch_country(country_name):
    url = f"https://restcountries.com/v3.1/name/{country_name}"  # API URL
    response = requests.get(url)  # Send GET request
    
    if response.status_code == 200:
        data = response.json()  # Convert response into JSON format
        
        if len(data) > 0:
            country_data = data[0]  # Take the first matching country
            
            # Get needed information
            name = country_data.get('name', {}).get('common', 'N/A')
            capital = country_data.get('capital', ['N/A'])[0]
            population = country_data.get('population', 'N/A')
            area = country_data.get('area', 'N/A')
            currency = list(country_data.get('currencies', {}).keys())
            region = country_data.get('region', 'N/A')
            
            return name, capital, population, area, currency, region
        else:
            return None  # If no country found
    else:
        return None  # If API call fails

# ---- Main Streamlit App ----
def main():
    st.title("🌍 Country Information Card")  # App title

    country_name = st.text_input("Enter the country name:")  # Input box for country name

    if country_name:
        result = fetch_country(country_name)  # Call function
        
        if result:
            name, capital, population, area, currency, region = result  # Unpack the result
            
            # Show country information
            st.subheader(f"📋 Details for {name}")
            st.write(f"**Capital:** {capital}")
            st.write(f"**Population:** {population}")
            st.write(f"**Area:** {area} km²")
            st.write(f"**Currency:** {', '.join(currency)}")
            st.write(f"**Region:** {region}")
        else:
            st.error("❌ Country not found or API error!")  # Show error if no data
    else:
        st.info("🔎 Please enter a country name to search.")  # Message to user

# ---- Run the App ----
if __name__ == "__main__":
    main()