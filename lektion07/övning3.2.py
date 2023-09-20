import requests

url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"

r = requests.get(url)

artists = r.json()

artists_list = artists['artists']

print("---Artist DB---")
for artist in artists_list:
    print(artist['name'])
print("-------------")
print("Select artist:")
artist_name = input('> ')
artist_name = artist_name.title()
print("----------------")
print(artist_name)
print("*************")

for artist in artists_list:

    if artist_name == artist['name']:
        artist_id = artist['id']
        break


try:
    url = url + artist_id
except NameError:
    print("saknas")
    exit(1)
r = requests.get(url)
artist_info = r.json()
artist_info = artist_info['artist']

print('Genres:',''.join(), artist_info['genres'], )
