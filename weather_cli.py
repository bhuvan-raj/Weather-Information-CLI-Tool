import requests

API_KEY = "199f0b797ce0eb3b3bcf25c63093297c"
BASE_URL = "http://api.weatherstack.com/current"

def get_weather(city):
    params = {
        'access_key': API_KEY,
        'query': city
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        if "error" in data:
            print(f"Error: {data['error']['info']}")
            return None
        return data 
    else:
        print("Failed to retrieve data")
        return None

def display_weather(data):
    location = data['location']['name']
    country = data['location']['country']
    temperature = data['current']['temperature']
    description = data['current']['weather_descriptions'][0]
    humidity = data['current']['humidity']
    wind_speed = data['current']['wind_speed']
    
    print(f"\nWeather in {location}, {country}:")
    print(f"Temperature: {temperature}°C")
    print(f"Condition: {description}")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} km/h")

def main():
    print("Weather Information CLI Tool")
    city = input("Enter a city name to get weather information: ")
    if city:
        data = get_weather(city)
        if data:
            display_weather(data)
        else:
            print("No data found for the city.")
    else:
        print("City name cannot be empty.")

if __name__ == "__main__":
    main()
