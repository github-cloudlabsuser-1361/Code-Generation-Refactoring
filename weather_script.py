import requests

def get_weather(city, api_key):
    """Fetch current weather data for a city from OpenWeatherMap API."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        main = data.get('main', {})
        weather = data.get('weather', [{}])[0]
        return {
            'city': data.get('name'),
            'temperature': main.get('temp'),
            'description': weather.get('description')
        }
    else:
        raise Exception(f"Error fetching weather data: {response.status_code} - {response.text}")

# Example usage:
# api_key = "YOUR_API_KEY"
# print(get_weather("London", api_key))