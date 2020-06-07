import requests

data = {
    'client': 'user1',
    'filename': '1588167250_doggo.jpeg_user1'
}

response = requests.get('http://localhost:8080/download', data)
f = open('poza.jpeg', 'wb')
f.write(response.content)
f.close()
