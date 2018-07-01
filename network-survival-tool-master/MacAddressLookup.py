def macid_lookup(mac):
    import pprint
    import requests
    MAC_URL = 'http://macvendors.co/api/%s'
    r = requests.get(MAC_URL % mac)
    pprint.pprint(r.json())

if _name_=='_main_'

macid_lookup(input("what's the MAC address you want to look up? "))
