# CW 1

import urllib.request
import json
import ssl

serviceurl = 'https://nominatim.openstreetmap.org/search.php?'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Podaj nazwę miejsca: ')
    if len(address) < 1: break

    parms = dict()
    parms['q'] = address
    parms['addressdetails'] = 1
    parms['format'] = 'geojson'
    parms['limit'] = 1
    parms['accept-language'] = 'pl'

    url = serviceurl + urllib.parse.urlencode(parms)

    print('Pobieranie', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Pobrano:', len(data))

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'features' not in js or len(js['features']) == 0:
        print('==== Błąd pobierania ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    location = js['features'][0]['properties']['display_name']

    try:
        state = js['features'][0]['properties']['address']['state']
        country_code = js['features'][0]['properties']['address']['country_code']
        if country_code == 'us':
            print('Stan: ', state)
            print('Lokalizacja: ', location)
        else:
            print('Lokalizacja: ', location)
    except:
        print('Lokalizacja: ', location)
