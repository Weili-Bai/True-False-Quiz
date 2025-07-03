import requests

para = {"amount": 10, "type": "boolean"}
request = requests.get(url="https://opentdb.com/api.php", params=para)
request.raise_for_status()
temp = request.json()
question_data = temp['results']
