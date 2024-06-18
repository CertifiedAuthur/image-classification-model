import requests

resp = requests.post("https://flask-pytorch-tutorial-6cd23d0171a2.herokuapp.com/predict", files={'file': open('seven.jpeg', 'rb')})

print(resp.text)