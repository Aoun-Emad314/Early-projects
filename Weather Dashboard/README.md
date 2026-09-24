# Python Weather Dashboard 🌤️

A command-line weather dashboard built with Python. This tool uses the OpenWeatherMap API to fetch precise geographical coordinates for any city and returns real-time weather data, including temperature (converted to Celsius) and current weather conditions. 

## Features
* **Geocoding API Integration:** Accurately converts city names and country codes into latitude and longitude.
* **Current Weather Data:** Retrieves live weather conditions and temperature ranges.
* **Automatic Temperature Conversion:** Built-in logic to convert Kelvin to Celsius.
* **JSON Export:** Automatically saves the raw API response to a local `map.json` file for future data processing.

## Prerequisites
You will need Python 3 installed on your machine, along with a free API key from [OpenWeatherMap](https://openweathermap.org/).

# Future Improvements (Roadmap)
* **Graphical User Interface (GUI)**: Transition from a terminal script to a desktop window using Tkinter or CustomTkinter.

* **Continuous Search Loop**: Wrap the main function in a while loop so users can look up multiple cities without having to restart the script.

* **Extended Forecast**: Pull data from the 5-day forecast endpoint to show future weather trends.

* **Rich Terminal Formatting**: Add colorized outputs for different weather states (e.g., blue for rain, yellow for sun) using the colorama or rich Python libraries.