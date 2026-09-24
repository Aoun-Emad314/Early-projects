import requests
import json


def main():
    # date input
    location_info = date_input()
    API_key = "691eac5e27e6f71cb9e4207aac527188"
    # get the geocode
    geocode = geocode_get(location_info, API_key)
    # api call and get the data
    weather = api_call(geocode, API_key)
    # summarize the data
    json_map(weather)


def date_input():
    print("🎯Getting an input started!")
    city_name = input("REQUIRED**Enter the city name: ")
    country_code = input("OPTIONAL**Enter the country code: ")
    state_code = input("OPTIONAL**Enter the state_code(US ONLY!)-leave it blank: ")
    limit = input(
        "OPTIONAL**Limit-Number of the locations in the API response-leave it blank: "
    )
    location_info = city_name, state_code, country_code, limit
    return location_info


def geocode_get(location, API_key):
    print("🎯Getting geocode started!")
    city_name = location[0]
    state_code = location[1]
    country_code = location[2]
    limit = location[3]
    if state_code == "":
        response = requests.get(
            f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{country_code}&limit={limit}&appid={API_key}"
        )
    else:
        state_code = int(location[1])
        response = requests.get(
            f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&limit={limit}&appid={API_key}"
        )
    raw_data = response.json()
    if not raw_data:
        print(f"Error: Could not find city '{city_name}'. Please try again.")
        # You could use sys.exit() here or return to the main menu
        exit()

    data = raw_data[0]
    geocode = data["lat"], data["lon"]
    lat, lon = geocode
    print(f"Lat={lat}\nLon={lon}")
    return geocode


def api_call(geocode, API_key):
    print("🎯API call started!")
    lat = geocode[0]
    lon = geocode[1]
    response = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}"
    )
    weather = response.json()

    in_list_weather = weather["weather"]
    in_list_weather = in_list_weather[0]
    weather_status = in_list_weather["main"], in_list_weather["description"]
    print(f"Weather status : {weather_status[0]}({weather_status[1]})")
    print(
        f"Temperature : Max({temp_converter(weather["main"]["temp_max"])})-Min({temp_converter(weather["main"]["temp_min"])})"
    )
    return weather


def temp_converter(k):
    c = int(k - 273.15)
    return c


def json_map(weather):
    print("🎯Creating json map started!")
    with open("map.json", "w") as f:
        json.dump(weather, f, indent=4)
        print("Saved successfully!")


if __name__ == "__main__":
    main()
