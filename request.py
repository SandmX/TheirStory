import requests

from define import *


api = URL + '/hello/Sandm'

r = requests.get(api)
print(r.text)
