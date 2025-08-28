import requests

# _____________________
# Helper Functions
# _____________________

def display_weather(data_dic):
    """Display the weather data in a readable format"""
    for key, value in data_dic.items():
        print(f'{key.title()} : {value}')

def weather_data(city):
    """Fetch weather data for a city using OpenWeatherMap API"""
    my_key = input("Enter your key: ").lower().strip()  # Your API key
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={my_key}'
    
    response = requests.get(url)
    if response.status_code != 200:
        print('City not found, please try again.')
        return None
    else:
        data = response.json()
        print(f'\n**** Weather in {data["name"]} *****')
        display_weather(data['main'])
        print("\n")  # Extra line for readability
        return data


# _____________________
# Main Loop
# _____________________

def main():
    """Main program loop to ask for cities and display weather"""
    print("Welcome to the Weather App!\n")
    while True:
        city = input('Enter the city: ')
        weather_data(city)
        try_again = input('Do you want to check another city? (y/n): ')
        if try_again.lower() != 'y':
            print('Bye!')
            break

# _____________________
# Entry Point
# _____________________

if __name__ == '__main__':
    main()

