import requests
import json


url = "https://anime-jokes.p.rapidapi.com/jokes/"

headers = {
	"X-RapidAPI-Key": "ec3d81a68amsh03ca29edb107ce3p12a3a0jsn39d3eaecb565",
	"X-RapidAPI-Host": "anime-jokes.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers).text


x = response.replace("null", '"Unknown"')

i = json.loads(x)    
print(i[0])
