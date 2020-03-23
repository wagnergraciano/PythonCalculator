import requests

data = {
  'elemento': 'd'
}

response = requests.post('http://localhost:5000/lista', data=data)