import urllib
import requests
import requests_mock
import os


my_secret_key = os.environ['MASHAPE_KEY']



def test_mock():
    with requests_mock.mock() as m:

        good_data = '''
    {
      "info": {
        "num_results": 27,
        "limit": 100,
        "offset": 0,
        "query": "yellow submarine",
        "type": "album",
        "page": 1
      },
      "albums": [
        {
          "name": "While My Guitar Gently Weeps / Yellow Submarine",
          "popularity": "0.44",
          "external-ids": [
            {
              "type": "upc",
              "id": "4260125292070"
            }
          ],
          "href": "spotify:album:3UiMXMkKxs3arKYYp3isIs",
          "artists": [
            {
              "href": "spotify:artist:2DghgxF3jV3G5xfcTpZpKr",
              "name": "Re Beatles"
            }
          ],
          "availability": {
            "territories": "AD AR AT AU BE BG BO BR CA CH CL CO CR CY CZ DE DK DO EC EE ES FI FR GB GR GT HK HN HR HU IE IS IT LI LT LU LV MC MT MX MY NI NL NO NZ PA PE PH PL PT PY RO SE SG SI SK SV TR TW US UY"
          }
        },
        {
          "name": "咖啡王子",
          "popularity": "0.29",
          "external-ids": [
            {
              "type": "upc",
              "id": "085365745391"
            }
          ],
          "href": "spotify:album:1qigZ4EiDdum043GZ6E6JL",
          "artists": [
            {
              "href": "spotify:artist:1xFWohe80U26QYZBLiG498",
              "name": "Yellow Submarine"
            }
          ],
          "availability": {
            "territories": "HK MY PH SG TW"
          }
        },
        {
          "name": "Yellow Submarine",
          "popularity": "0.09",
          "external-ids": [
            {
              "type": "upc",
              "id": "889176136467"
            }
          ],
          "href": "spotify:album:3EgI9NDpWANbEr9nGC5lav",
          "artists": [
            {
              "href": "spotify:artist:0ttu7CII9sDRT2s3tGg9Gd",
              "name": "Model Boyz"
            }
          ],
          "availability": {
            "territories": "AD AR AT AU BE BG BO BR CA CH CL CO CR CY CZ DE DK DO EC EE ES FI FR GB GR GT HK HN HR HU IE IS IT LI LT LU LV MC MT MX MY NI NL NO NZ PA PE PH PL PT PY RO SE SG SI SK SV TR TW US UY"
          }
        },
        {
          "name": "Yellow Submarine",
          "popularity": "0",
          "external-ids": [
            {
              "type": "upc",
              "id": "859713335073"
            }
          ],
          "href": "spotify:album:3jv3vFWSzOle3Nz2GcYWaY",
          "artists": [
            {
              "href": "spotify:artist:5BSF91uhHHcl6upYJgsY7k",
              "name": "Johnny Six Pack"
            }
          ],
          "availability": {
            "territories": "AD AR AT AU BE BG BO BR CA CH CL CO CR CY CZ DE DK DO EC EE ES FI FR GB GR GT HK HN HR HU IE IS IT LI LT LU LV MC MT MX MY NI NL NO NZ PA PE PH PL PT PY RO SE SG SI SK SV TR TW US UY"
          }
        },
        {
          "name": "My Lovely Sam-soon",
          "popularity": "0.09",
          "external-ids": [
            {
              "type": "upc",
              "id": "085365755048"
            }
          ],
          "href": "spotify:album:3BgSKEoKB2YhkuVa09D1Cy",
          "artists": [
            {
              "href": "spotify:artist:1xFWohe80U26QYZBLiG498",
              "name": "Yellow Submarine"
            }
          ],
          "availability": {
            "territories": "HK MY"
          }
        },
        {
          "name": "อุณหภูมิ",
          "popularity": "0.06",
          "external-ids": [
            {
              "type": "upc",
              "id": "0859711499029"
            }
          ],
          "href": "spotify:album:6ffBxeCzq4qpP0I3OgC0zP",
          "artists": [
            {
              "href": "spotify:artist:1xFWohe80U26QYZBLiG498",
              "name": "Yellow Submarine"
            }
          ],
          "availability": {
            "territories": "AD AR AT AU BE BG BO BR CA CH CL CO CR CY CZ DE DK DO EC EE ES FI FR GB GR GT HK HN HR HU IE IS IT LI LT LU LV MC MT MX MY NI NL NO NZ PA PE PH PL PT PY RO SE SG SI SK SV TR TW US UY"
          }
        },
        {
          "name": "Solika",
          "popularity": "0",
          "external-ids": [
            {
              "type": "upc",
              "id": "7290012058790"
            }
          ],
          "href": "spotify:album:6PTAYxurW9ePUaPqkeFQvC",
          "artists": [
            {
              "href": "spotify:artist:62NWFXwa99zRF9PUmZgIw3",
              "name": "Odelia Dahan"
            }
          ],
          "availability": {
            "territories": "AD AR AT AU BE BG BO BR CA CH CL CO CR CY CZ DE DK DO EC EE ES FI FR GB GR GT HK HN HR HU IE IS IT LI LT LU LV MC MT MX MY NI NL NO NZ PA PE PH PL PT PY RO SE SG SI SK SV TR TW US UY"
          }
        },
        {
          "name": "Yellow Submarine - The Beatles Tribute",
          "popularity": "0.44",
          "external-ids": [
            {
              "type": "upc",
              "id": "7340027012949"
            }
          ],
          "href": "spotify:album:5F2XFTM1GdNd1W9fXjNqOu",
          "artists": [
            {
              "href": "spotify:artist:3K3OsB2PkJBR2qpZoYuSct",
              "name": "The Yellow Subs"
            }
          ],
          "availability": {
            "territories": "AD AR AT AU BE BG BO BR CA CH CL CO CR CY CZ DE DK DO EC EE ES FI FR GB GR GT HK HN HR HU IE IS IT LI LT LU LV MC MT MX MY NI NL NO NZ PA PE PH PL PT PY RO SE SG SI SK SV TR TW US UY"
          }
        },
        {
          "name": "Yellow Submarine",
          "popularity": "0.13",
          "external-ids": [
            {
              "type": "upc",
              "id": "9399238102022"
            }
          ],
          "href": "spotify:album:3oPV4mTYLsOvTbvKxDYLc9",
          "artists": [
            {
              "href": "spotify:artist:0lMFbOfz8ikoEAvrdl61PF",
              "name": "London Session Singers"
            }
          ],
          "availability": {
            "territories": "AD AR AT AU BE BG BO BR CA CH CL CO CR CY CZ DE DK DO EC EE ES FI FR GB GR GT HK HN HR HU IE IS IT LI LT LU LV MC MT MX MY NI NL NO NZ PA PE PH PL PT PY RO SE SG SI SK SV TR TW US UY"
          }
        },
        {
          "name": "Yellow Submarine",
          "popularity": "0",
          "external-ids": [
            {
              "type": "upc",
              "id": "3610150189868"
            }
          ],
          "href": "spotify:album:1O9kICuV70KSFzsicXwL2C",
          "artists": [
            {
              "href": "spotify:artist:46NvHbouOOKmScLlx0djGd",
              "name": "MusiKazoo Ringers"
            }
          ],
          "availability": {
            "territories": "AD AR AT AU BE BG BO BR CA CH CL CO CR CY CZ DE DK DO EC EE ES FI FR GB GR GT HK HN HR HU IE IS IT LI LT LU LV MC MT MX MY NI NL NO NZ PA PE PH PL PT PY RO SE SG SI SK SV TR TW US UY"
          }
        },
        {
          "name": "Yellow Submarine",
          "popularity": "0",
          "external-ids": [
            {
              "type": "upc",
              "id": "887845058782"
            }
          ],
          "href": "spotify:album:4UazJOxQ9Oi378TK98Y081",
          "artists": [
            {
              "href": "spotify:artist:0GQkTwFb7D3ePIpnxwYavf",
              "name": "Done Again"
            }
          ],
          "availability": {
            "territories": "AD AR AT AU BE BG BO BR CA CH CL CO CR CY CZ DE DK DO EC EE ES FI FR GB GR GT HK HN HR HU IE IS IT LI LT LU LV MC MT MX MY NI NL NO NZ PA PE PH PL PT PY RO SE SG SI SK SV TR TW US UY"
          }
        },
        {
          "name": "Baby Beatles: Yellow Submarine",
          "popularity": "0.02",
          "external-ids": [
            {
              "type": "upc",
              "id": "888608984775"
            }
          ],
          "href": "spotify:album:4EKA8Da1BcDjzlyr2Vvkgj",
          "artists": [
            {
              "href": "spotify:artist:1qZqAv80HZsX5qPRIZ4AJW",
              "name": "Baby Sueños"
            }
          ],
          "availability": {
            "territories": "AD AR AT AU BE BG BO BR CA CH CL CO CR CY CZ DE DK DO EC EE ES FI FR GB GR GT HK HN HR HU IE IS IT LI LT LU LV MC MT MX MY NI NL NO NZ PA PE PH PL PT PY RO SE SG SI SK SV TR TW US UY"
          }
        },
        {
          "name": "Yellow Submarine (Karaoke Version) [Originally Performed By the Beatles]",
          "popularity": "0.12",
          "external-ids": [
            {
              "type": "upc",
              "id": "3610151755154"
            }
          ],
          "href": "spotify:album:3LTA83ArSuWWgpYrUT1SqS",
          "artists": [
            {
              "href": "spotify:artist:2C0SBcKuVcbQx2TKv88547",
              "name": "Retro Karaoke Generation"
            }
          ],
          "availability": {
            "territories": "AD AR AT AU BE BG BO BR CA CH CL CO CR CY CZ DE DK DO EC EE ES FI FR GB GR GT HK HN HR HU IE IS IT LI LT LU LV MC MT MX MY NI NL NO NZ PA PE PH PL PT PY RO SE SG SI SK SV TR TW US UY"
          }
        },
        {
          "name": "The Beatles Box Versions Vol.22 - Yellow Submarine",
          "popularity": "0",
          "external-ids": [
            {
              "type": "upc",
              "id": "885686633564"
            }
          ],
          "href": "spotify:album:3QAbXK0BA6lYx54oHpwyIl",
          "artists": [
            {
              "name": "Various Artists"
            }
          ],
          "availability": {
            "territories": "AD AR AT AU BE BG BO BR CA CH CL CO CR CY CZ DE DK DO EC EE ES FI FR GB GR GT HK HN HR HU IE IS IT LI LT LU LV MC MT MX MY NI NL NO NZ PA PE PH PL PT PY RO SE SG SI SK SV TR TW US UY"
          }
        },
        {
          "name": "Yellow Submarine (Karaoke Version In the Style of The Beatles)",
          "popularity": "0",
          "external-ids": [
            {
              "type": "upc",
              "id": "3661585059288"
            }
          ],
          "href": "spotify:album:4PVFi0NLhIGSiElKjv7FfT",
          "artists": [
            {
              "href": "spotify:artist:7yv4DJOCmilSbxxsdQgXWk",
              "name": "Pictomusic"
            }
          ],
          "availability": {
            "territories": "AD AR AT AU BE BG BO BR CA CH CL CO CR CY CZ DE DK DO EC EE ES FI FR GB GR GT HK HN HR HU IE IS IT LI LT LU LV MC MT MX MY NI NL NO NZ PA PE PH PL PT PY RO SE SG SI SK SV TR TW US UY"
          }
        },
        {
          "name": "Yellow Submarine (Sing Like the Beatles) [Karaoke and Vocal Versions]",
          "popularity": "0",
          "external-ids": [
            {
              "type": "upc",
              "id": "882387143262"
            }
          ],
          "href": "spotify:album:57q5VTYx0M0QbiJ5baxsob",
          "artists": [
            {
              "href": "spotify:artist:5UloVKzUNJcjORzhhTWWiJ",
              "name": "The Karaoke Channel"
            }
          ],
          "availability": {
            "territories": "AD AR AT AU BE BG BO BR CA CH CL CO CR CY CZ DE DK DO EC EE ES FI FR GB GR GT HK HN HR HU IE IS IT LI LT LU LV MC MT MX MY NI NL NO NZ PA PE PH PL PT PY RO SE SG SI SK SV TR TW US UY"
          }
        },
        {
          "name": "Yellow Submarine (Sing Like the Beatles) [Karaoke and Vocal Versions]",
          "popularity": "0",
          "external-ids": [
            {
              "type": "upc",
              "id": "882387143422"
            }
          ],
          "href": "spotify:album:6yg9kW844I873hlx07N8d0",
          "artists": [
            {
              "href": "spotify:artist:5UloVKzUNJcjORzhhTWWiJ",
              "name": "The Karaoke Channel"
            }
          ],
          "availability": {
            "territories": "AD AR AT AU BE BG BO BR CA CH CL CO CR CY CZ DE DK DO EC EE ES FI FR GB GR GT HK HN HR HU IE IS IT LI LT LU LV MC MT MX MY NI NL NO NZ PA PE PH PL PT PY RO SE SG SI SK SV TR TW US UY"
          }
        },
        {
          "name": "Yellow Submarine (In the Style of Beatles) [Karaoke Version] - Single",
          "popularity": "0",
          "external-ids": [
            {
              "type": "upc",
              "id": "888002293985"
            }
          ],
          "href": "spotify:album:0kFoGOGkCcTenjG2Q9I1Rc",
          "artists": [
            {
              "href": "spotify:artist:4Z6WehLCUZYmz0RJL8CXCw",
              "name": "ProSource Karaoke"
            }
          ],
          "availability": {
            "territories": "AD AR AT AU BE BG BO BR CA CH CL CO CR CY CZ DE DK DO EC EE ES FI FR GB GR GT HK HN HR HU IE IS IT LI LT LU LV MC MT MX MY NI NL NO NZ PA PE PH PL PT PY RO SE SG SI SK SV TR TW US UY"
          }
        },
        {
          "name": "Yellow Submarine (In the Style of the Beatles) [Karaoke Version] - Single",
          "popularity": "0",
          "external-ids": [
            {
              "type": "upc",
              "id": "888003805378"
            }
          ],
          "href": "spotify:album:1PJjyNUgDN3niILXhq4iC2",
          "artists": [
            {
              "href": "spotify:artist:5aEMARkjW3SYYnGLTLgCks",
              "name": "Karaoke - Ameritz"
            }
          ],
          "availability": {
            "territories": "AD AR AT AU BE BG BO BR CA CH CL CO CR CY CZ DE DK DO EC EE ES FI FR GB GR GT HK HN HR HU IE IS IT LI LT LU LV MC MT MX MY NI NL NO NZ PA PE PH PL PT PY RO SE SG SI SK SV TR TW US UY"
          }
        },
        {
          "name": "Yellow Submarine (In the Style of the Beatles) [Karaoke] - EP",
          "popularity": "0",
          "external-ids": [
            {
              "type": "upc",
              "id": "887845013545"
            }
          ],
          "href": "spotify:album:2sdotXcdfaiBKAX3ANgkd3",
          "artists": [
            {
              "href": "spotify:artist:0uiGRZiDfG8wniUxPtKOte",
              "name": "All Star Karaoke"
            }
          ],
          "availability": {
            "territories": "AD AR AT AU BE BG BO BR CA CH CL CO CR CY CZ DE DK DO EC EE ES FI FR GB GR GT HK HN HR HU IE IS IT LI LT LU LV MC MT MX MY NI NL NO NZ PA PE PH PL PT PY RO SE SG SI SK SV TR TW US UY"
          }
        },
        {
          "name": "Yellow Submarine (In the Style of the Beatles) [Karaoke] - EP",
          "popularity": "0",
          "external-ids": [
            {
              "type": "upc",
              "id": "887845037121"
            }
          ],
          "href": "spotify:album:5zfwE1d17WC7VpgnbRkEH1",
          "artists": [
            {
              "href": "spotify:artist:6ytS4w81LDmRru88Ta9CBk",
              "name": "The Best Karaoke"
            }
          ],
          "availability": {
            "territories": "AD AR AT AU BE BG BO BR CA CH CL CO CR CY CZ DE DK DO EC EE ES FI FR GB GR GT HK HN HR HU IE IS IT LI LT LU LV MC MT MX MY NI NL NO NZ PA PE PH PL PT PY RO SE SG SI SK SV TR TW US UY"
          }
        },
        {
          "name": "Yellow Submarine (Originally Performed by the Beatles) [Karaoke Version]",
          "popularity": "0",
          "external-ids": [
            {
              "type": "upc",
              "id": "888831514237"
            }
          ],
          "href": "spotify:album:4IvDoknbGPwxXib3Hm1EIg",
          "artists": [
            {
              "href": "spotify:artist:76XE4h4VXk8KbLJallt9Ym",
              "name": "Mega Tracks Karaoke Band"
            }
          ],
          "availability": {
            "territories": "AD AR AT AU BE BG BO BR CA CH CL CO CR CY CZ DE DK DO EC EE ES FI FR GB GR GT HK HN HR HU IE IS IT LI LT LU LV MC MT MX MY NI NL NO NZ PA PE PH PL PT PY RO SE SG SI SK SV TR TW US UY"
          }
        },
        {
          "name": "Yellow Submarine: A Kid-Friendly Tribute to the Beatles, Vol.1",
          "popularity": "0",
          "external-ids": [
            {
              "type": "upc",
              "id": "803151102322"
            }
          ],
          "href": "spotify:album:5cTRjltY5qJEbauPpU9pBb",
          "artists": [
            {
              "href": "spotify:artist:2i4GVlEu6cffApP1QcjawY",
              "name": "Mr. Ray"
            }
          ],
          "availability": {
            "territories": "AD AR AT AU BE BG BO BR CA CH CL CO CR CY CZ DE DK DO EC EE ES FI FR GB GR GT HK HN HR HU IE IS IT LI LT LU LV MC MT MX MY NI NL NO NZ PA PE PH PL PT PY RO SE SG SI SK SV TR TW US UY"
          }
        },
        {
          "name": "The Karaoke Channel - Sing Yellow Submarine Like the Beatles",
          "popularity": "0",
          "external-ids": [
            {
              "type": "upc",
              "id": "889845487487"
            }
          ],
          "href": "spotify:album:0VfYzXTTSDHMkgYE4PRMu8",
          "artists": [
            {
              "href": "spotify:artist:5UloVKzUNJcjORzhhTWWiJ",
              "name": "The Karaoke Channel"
            }
          ],
          "availability": {
            "territories": "AD AR AT AU BE BG BO BR CA CH CL CO CR CY CZ DE DK DO EC EE ES FI FR GB GR GT HK HN HR HU IE IS IT LI LT LU LV MC MT MX MY NI NL NO NZ PA PE PH PL PT PY RO SE SG SI SK SV TR TW US UY"
          }
        },
        {
          "name": "Yellow Submarine (In the Style of the Beatles) [Performance Track with Demonstration Vocals]",
          "popularity": "0",
          "external-ids": [
            {
              "type": "upc",
              "id": "886788344419"
            }
          ],
          "href": "spotify:album:48f7xsqnVsS17tgd6pwqr6",
          "artists": [
            {
              "href": "spotify:artist:0GQkTwFb7D3ePIpnxwYavf",
              "name": "Done Again"
            }
          ],
          "availability": {
            "territories": "AD AR AT AU BE BG BO BR CA CH CL CO CR CY CZ DE DK DO EC EE ES FI FR GB GR GT HK HN HR HU IE IS IT LI LT LU LV MC MT MX MY NI NL NO NZ PA PE PH PL PT PY RO SE SG SI SK SV TR TW US UY"
          }
        },
        {
          "name": "Yellow Submarine (In the Style of the Beatles) [Performance Track with Demonstration Vocals] - Single",
          "popularity": "0",
          "external-ids": [
            {
              "type": "upc",
              "id": "882387136257"
            }
          ],
          "href": "spotify:album:4ahKWENsUPBzGzJIIIbAKD",
          "artists": [
            {
              "href": "spotify:artist:0GQkTwFb7D3ePIpnxwYavf",
              "name": "Done Again"
            }
          ],
          "availability": {
            "territories": "AD AR AT AU BE BG BO BR CA CH CL CO CR CY CZ DE DK DO EC EE ES FI FR GB GR GT HK HN HR HU IE IS IT LI LT LU LV MC MT MX MY NI NL NO NZ PA PE PH PL PT PY RO SE SG SI SK SV TR TW US UY"
          }
        },
        {
          "name": "Yellow Submarine - 26 Childrens' Songs",
          "popularity": "0.04",
          "external-ids": [
            {
              "type": "upc",
              "id": "0881969409918"
            }
          ],
          "href": "spotify:album:1j1rQljiP0zcWvOPE0UraW",
          "artists": [
            {
              "href": "spotify:artist:67BYPPPeYqRUFxplpTtaJm",
              "name": "Neva Eder"
            }
          ],
          "availability": {
            "territories": "AD AT BE BG CH CY CZ DE DK EE ES FI FR GB GR HR HU IE IS IT LI LT LU LV MC MT NL NO PL PT SE SI SK"
          }
        }
      ]
    }'''
        m.get('https://mager-spotify-web.p.mashape.com/search/1/album.json?q=yellow+submarine', text=good_data)

        res = requests.get('https://mager-spotify-web.p.mashape.com/search/1/album.json?q=yellow+submarine', headers={'X-Mashape-Key': my_secret_key})

        print(res.json())


class SearchAlbums:
    def __init__(self, q_string):
        self.q_string = q_string

    def run(self):
        url = 'https://mager-spotify-web.p.mashape.com/search/1/album.json?q={}'.format(self.q_string)

        res = requests.get(url, headers={'X-Mashape-Key': os.environ['MASHAPE_KEY']}).json()

        album = res['albums'][0]['name']
        artist = res['albums'][0]['artists'][0]['name']

        return artist, album

class SearchArtists:
    def __init__(self, q_string):
        self.q_string = q_string

    def run(self):
        url = 'https://mager-spotify-web.p.mashape.com/search/1/artist.json?q={}'.format(self.q_string)

        res = requests.get(url, headers={'X-Mashape-Key': os.environ['MASHAPE_KEY']}).json()

        if res.status != 200:
            return
        # album = res['albums'][0]['name']
        artist = res['artists'][0]['name']

        return artist



def main():
    call = SearchAlbums('thriller')
    res = call.run()
    print(res.text)


if __name__ == '__main__':
    main()
