import requests

# lista över artister
def get_artist_list():
    url = 'https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/'
    response = requests.get(url)
    if response.status_code == 200:
        artist_list = response.json()
        return artist_list

    else:
        print("Något gick fel:", response.status_code)
        return None

# info om artisten
def get_artist_info(artist_id):
    url = f'https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/{artist_id}'
    response = requests.get(url)
    if response.status_code == 200:
        artist_info = response.json()

        return artist_info
    else:
        print("Kunde inte hämta artistinformation. Felkod:", response.status_code)
        return None

artist_list = get_artist_list()

if artist_list:
    print("--- ARTIST DB ---")
    for artist in artist_list:
        print(artist['name'])
        print("-----------------")

    while True:
       selected_artist = input("Välj en artist från listan ovan (skriv artistens namn): ").strip().lower()
       selected_artist_id = None
       for artist in artist_list:
           if selected_artist == artist['name'].strip().lower():
               selected_artist_id = artist['id']
               break

       if selected_artist_id:
           artist_info = get_artist_info(selected_artist_id)
           if artist_info:

               print("-----------------")
               print(artist_info['name'])
               print("*" * 18)
               print(f"Genres: {', '.join(artist_info['genres'])}")
               print(f"Years active: {artist_info['yearsActive']}")
               print(f"Members: {artist_info['members']}")
               print("-----------------")
               break
           else:
               print("Kunde inte hämta artistinformation.")
       else:
           print("Ogiltig artist. Försök igen.")
else:
    print("Ingen artistlista tillgänglig.")






