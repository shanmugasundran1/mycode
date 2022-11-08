#!/usr/bin/env python3
"""Alta3 Research
   Star Wars API HTTP response parsing"""

# pprint makes dictionaries a lot more human readable
from pprint import pprint
import json
# requests is used to send HTTP requests (get it?)
import requests

# The following URL is constructed incorrectly. It should be api/people/4/
# URL= "https://swapi.dev/api/luke/force"

URL= "https://swapi.dev/api/people/4/"


def main():
    """sending GET request, checking response"""

    # SWAPI response is stored in "resp" object
    resp= requests.get(URL)

    if resp.status_code==200:
    # convert the JSON content of the response into a python dictionary
         vader= resp.json()
         pprint(vader)


#         print(f"{vader.json()['name']} was born in the year {vader.json()['birth_year']}. His eyes are now {vader.json()['eye_colour']} and his hair color is {vader.json()['hair_colour']}")

    else:
        print("Not a valid url")

if __name__ == "__main__":
    main()

