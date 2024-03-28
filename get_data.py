import requests
import json
url = 'https://api.jsonbin.io/v3/b/65d77e13266cfc3fde8ddeb7/latest/'
headers = {
    'X-Master-Key': '$2a$10$vaoE2zeHNzxtHNFsBwBw7uMzvHzDdHKlB2xwIn0yBJy3.0fKO0JhG',
    'X-Bin-Meta': 'false'
}
req = requests.get(url, headers=headers)

data = json.loads(req.text)