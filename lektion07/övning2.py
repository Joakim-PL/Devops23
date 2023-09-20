ui_width = 30
import requests
import json


def fetch_stad_info(city):
    url = f'https://54qhf521ze.execute-api.eu-north-1.amazonaws.com/weather/{city}'
    response = requests.get(url)

    if response.status_code == 200:
        return json.loads(response.text)
    else:
        return None


while True:
    try:
        city = input("Enter the name of the city\nfor which you want forecast:\n> ")
        stad_info = fetch_stad_info(city)

        if stad_info:
            print("-" * ui_width)
            print("FORECAST".center(ui_width))
            print("*" * 30)

            for forecast in stad_info['forecasts']:
                date = forecast['date']
                forecast_text = forecast['forecast']
                print(f"{date:<10}   {forecast_text:<20}")
            print("-" * ui_width)
            break

        else:
            print("ogiltig inmatning. Försök igen.")
    except ValueError:
        print("Ogiltig inmatning. Försök igen.")
