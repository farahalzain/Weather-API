# ***Weather App – Python Project***

**Weather App** is a simple Python application that fetches the current weather for any city using the **OpenWeatherMap API**. Users can input a city name, and the program displays temperature, humidity, and other key weather details.

---

## ***Features***

* Fetches real-time weather data for any city.
* Displays key weather metrics: temperature, humidity, pressure, etc.
* Handles invalid city names gracefully.
* Interactive loop allows checking multiple cities without restarting the program.
* Clean, modular code with functions and comments in English.

---

## ***Project Structure***

 weather_app.py      # Main script containing all functions

---

## ***Code Overview***

### ***Functions***

* `display_weather(data_dic)` → Displays weather details in a readable format.
* `weather_data(city)` → Fetches weather data from OpenWeatherMap API for a given city.
* `main()` → Main loop asking the user for cities and displaying weather, allows multiple queries.
***Note:*** The `api_key` parameter must be provided by the user. You need to create a free account on [OpenWeatherMap](https://openweathermap.org/?utm_source=chatgpt.com)
 to get your API key.
---

##  ***How to Run***

### ***Requirements***

* Library: `requests`

### ***Run the Project***


Run the file: ***weather_app.py***

---

##  Example Usage

```
Enter the city: Cairo
Enter your key: : <YOUR_KEY>
**** Weather in Cairo *****
Temp : 31.0
Pressure : 1012
Humidity : 40
Temp Min : 29.0
Temp Max : 33.0

Do you want to check another city? (y/n): y

Enter your key: : <YOUR_KEY>
Enter the city: London
**** Weather in London *****
Temp : 18.0
Pressure : 1015
Humidity : 60
Temp Min : 17.0
Temp Max : 19.0

Do you want to check another city? (y/n): n
 Bye!
```
