from requests import get

city = input("Enter city: ")

request = get(f"https://wttr.in/{city}?format=j2")
data = request.json()

current_info = data["current_condition"][0]
info = data["weather"][0]

print("\nWeather Information of " + city)
print("Current Temperature:", current_info["FeelsLikeC"], "°C")
print("Average:", info["avgtempC"], "°C")
print("Humidity:", current_info["humidity"], "%")
print("Visibility:", current_info["visibility"], "km")
print("Description:", current_info["weatherDesc"][0]["value"])
print("Wind Speed(km/h):", current_info["windspeedKmph"], current_info["winddir16Point"])
print("Observed At:", current_info["observation_time"])