import requests
import json


def fetch_number_info(number):#hämtar info från api
    url = f'https://4bbh01oqwj.execute-api.eu-north-1.amazonaws.com/numcheck?integer=100'
    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        return None


while True: #huvudprogram för att skriva ut allt
    try:
        number = int(input("Ange ett positivt heltal: "))

        if number <= 0:
            print("ogiltig inmatning. Försök igen.")
        else:
            number_info = fetch_number_info(number)
            if number_info:
                print(f"{number} är ett {number_info['even']} nummer.")
                print(f"Numret är{' inte' if not number_info['prime'] else ''} ett primtal.")
                print(f"Numrets faktorer är {', '.join(map(str, number_info['factors']))}.")
                break
            else:
                print("Något gick fel. Försök igen senare.")
    except ValueError:
        print("Ogiltig inmatning. Ange ett positivt heltal.")
