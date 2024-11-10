# Weather Information CLI Tool

A simple command-line tool built in Python that retrieves and displays current weather information for any city using the Weatherstack API. This tool provides details like temperature, weather conditions, humidity, and wind speed for the specified location.

## Features

- Fetches current weather data based on the user-input city name.
- Provides information on temperature, weather description, humidity, and wind speed.
- Error handling for invalid cities or API errors.

## Requirements

- **Python 3.x**: Ensure Python is installed on your system.
- **Requests Library**: Used to make HTTP requests to the Weatherstack API.
  
  Install it by running:
  ```bash
  pip install requests

SETUP AND USAGE

1. Clone the Repository (or download the weather_cli.py file directly):
          
git clone https://github.com/your-username/weather-cli-tool.git

```bash
cd weather-cli-tool
```
GET A WEATHERSTACK API:

Sign up at Weatherstack to get a free API key.
Replace "YOUR_WEATHERSTACK_API_KEY" in weather_cli.py with your actual API key.

# RUN THE TOOL

Open a terminal in the project directory and execute the script:
```bash
python weather_cli.py
```
Enter a city name when prompted to see the weather information.

# ERROR HANDLING

If the city name is invalid or there is an issue with the API, an error message will be displayed.

# LICENSE

This Project is Licensed under MIT License



