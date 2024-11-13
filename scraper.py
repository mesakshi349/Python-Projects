# Import necessary libraries
import requests  # To send HTTP requests
from bs4 import BeautifulSoup  # To parse HTML content
import pandas as pd  # To handle data and export it to Excel

# Step 1: Define the URL to scrape data from
url = "https://weather.com/weather/tenday/l/USCA1116:1:US"  # Example URL for weather forecast

# Step 2: Send a GET request to fetch the webpage
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}
response = requests.get(url, headers=headers)

# Step 3: Check if the request was successful
if response.status_code == 200:
    print("Webpage fetched successfully!")
else:
    print(f"Failed to fetch the webpage. Status code: {response.status_code}")
    exit()

# Step 4: Parse the webpage content
soup = BeautifulSoup(response.content, 'html.parser')

# Step 5: Extract dates and temperatures (example selectors)
# This will vary based on the structure of the webpage.
dates = []  # List to store dates
temperatures = []  # List to store temperatures

# Locate elements containing dates and temperatures (simplified example)
date_elements = soup.find_all("span", class_="DailyContent--daypartDate--3MM0J")  # Adjust selectors as needed
temp_elements = soup.find_all("span", class_="DetailsSummary--highTempValue--3x6cL")  # Adjust selectors as needed

# Extract text and store in lists
for date in date_elements:
    dates.append(date.get_text())  # Extracts and stores date text

for temp in temp_elements:
    temperatures.append(temp.get_text())  # Extracts and stores temperature text

# Step 6: Save data to a DataFrame and export to an Excel file
data = pd.DataFrame({
    "Date": dates[:len(temperatures)],  # Ensure equal lengths
    "Temperature": temperatures
})

# Export the data to an Excel file
data.to_excel("weather_data.xlsx", index=False)
print("Data has been saved to 'weather_data.xlsx'")
