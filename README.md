# Geocoding with Google Maps

This script allows you to map a description of a place on the planet Earth made by an Homo Sapiens, such as "Paris, France.", to a Machine-friendly description, with GPS coordinates, several administrative/political levels to which the place belong to, and more.

### API KEY and IP registration

You must provide an API_KEY to use this service. Go to: <https://developers.google.com/maps/documentation/geocoding/#api_key>
You should also register the IP of the computer you whish to run this script from.

### Dependency

Install [Requests](http://docs.python-requests.org/en/latest/).

```bash
sudo pip install requests
```

### Usage

`geocoding.py` takes the places described in the file `todo.txt` (one per line), checks if it's not already available in `places.json`, make the query on Google Maps for each of them, and append the result to the file `places.json`.

```bash
$ git clone git@github.com:cortext/geocoding.git
Cloning into 'geocoding'...
remote: Counting objects: 7, done.
remote: Compressing objects: 100% (7/7), done.
remote: Total 7 (delta 1), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (7/7), 8.32 KiB | 0 bytes/s, done.
Resolving deltas: 100% (1/1), done.
Checking connectivity... done.
$ cd geocoding
$ ls
README.md     geocoding.py places.json   todo.txt
$ python geocoding.py
Found 98919 places in ./places.json
Found 13418 new places to check in ./todo.txt
0 ibagué
1 Gebze / KOCAELİ
2 Sant Vicenç dels Horts
3 Campos do Jordão, Brazil
4 Brazil - Paraíba - Campina Grande
5 João Pessoa/PB , Brazil
6 Taubaté/SP - Brasil
7 Bragança Paulista
8 someplace
9 São Paulo, SP, Brazil
10 Jundiaí - SP - Brazil
11 Gyál, Hungary
...
```
