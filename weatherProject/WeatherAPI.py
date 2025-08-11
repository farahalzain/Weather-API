import requests
import Weather_show 

def main():
    while True:
        city = input('Enter the city : ')
        Weather_show.weather_data(city)
        try_again = input('Do you want to check another city? (y/n) : ')
        if try_again.lower() == 'n':
            print('Bye!')
            break
        

if __name__ == '__main__':
    main()
