import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service

# Suppress unnecessary logs and allow for only critical logs
logging.basicConfig(level=logging.ERROR)  # Set logging level to ERROR to suppress info and warnings
options = Options()
options.add_argument('--log-level=3')

# Create a Service object for Edge WebDriver
# Here, the executable path should be replaced with yours,
# which is the part to your Webdriver 
service = Service(executable_path="C:\\Users\\Asus\\Downloads\\edgedriver_win64\\msedgedriver.exe")
service.start()

# Create the driver instance
driver = webdriver.Edge(service=service, options=options)

# Set an implicit wait of 7 seconds
driver.implicitly_wait(7)

# Make use of Open Weather Map site to search for the weather
def get_weather_for_city(city_name):
    # Set up the URL
    base_url = "https://openweathermap.org/find?q="
    url = base_url + city_name
    
    # Open the page
    driver.get(url)
    
    # Find the first result in the search page
    try:
        # Look for the first <tr> element in the search results
        first_result = driver.find_element(By.CSS_SELECTOR, "table.table tbody tr")
        
        # Extract the temperature from the <span class="badge badge-info">
        temperature_span = first_result.find_element(By.CSS_SELECTOR, "span.badge-info")
        temperature = temperature_span.text
        
        # Extract the city name and country code
        city_country = first_result.find_element(By.CSS_SELECTOR, "a").text
        
        # Return the city and temperature
        return city_country, temperature
    except Exception as e:
        print(f"Error for city '{city_name}': {e}")
        return None, None

def get_weather_for_multiple_cities(cities):
    results = []
    for city in cities:
        city_weather = get_weather_for_city(city)
        if city_weather[0] and city_weather[1]:
            results.append(city_weather)
    return results

# Get the weather for 5 capital cities
cities = ["Moscow", "Belgrade", "Paris", "Abuja", "Amsterdam"]
weather_data = get_weather_for_multiple_cities(cities)

# Print out the weather results
for city, temperature in weather_data:
    print(f"City: {city}, Temperature: {temperature}")

# Close the driver
driver.quit()
