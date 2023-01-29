from django.shortcuts import render, redirect
import requests
import json
import random

from .models import Submission

jokes = [
    {"setup":"What do you call a guy who gets drunk off of one glass of jungle juice?","punchline":"a one punch man","joke_anime":"one punch man","author":"Unknown","_id":16},
    {"setup":"Why did Akainu win the Marineford War?","punchline":"Because he had an Ace up his sleeve.","joke_anime":"one piece","author":"HappyTheFries","_id":15},
    {"setup":"We should have known that Doflamingo was behind so much","punchline":"I mean after all, this whole time he has been ... pulling the strings.","joke_anime":"one piece","author":"Unknown","_id":14},
    {"setup":"Why would Nami make a terrible vet?","punchline":"Because she is a cat burglar!","joke_anime":"one piece","author":"HappyTheFries","_id":13},
    {"setup":"What do skeletons say before they begin dinning?","punchline":"Bone Appetite!","joke_anime":"one piece","author":"HappyTheFries","_id":12}
]

# Create your views here.
def home(request):
    
    # url = "https://anime-jokes.p.rapidapi.com/jokes/"
    # headers = {
    #     "X-RapidAPI-Key": "ec3d81a68amsh03ca29edb107ce3p12a3a0jsn39d3eaecb565",
    #     "X-RapidAPI-Host": "anime-jokes.p.rapidapi.com"
    # }

    # response = requests.request("GET", url, headers=headers).text

    # replacedNull = response.replace("null", '"Unknown"')
    # jokes = json.loads(replacedNull)  
     
    joke = random.choice(jokes)
    setup = joke["setup"]
    punchline = joke['punchline']

    success = ''
    if request.method == "POST":
        name = request.POST.get("name")
        joke = request.POST.get("joke")
        anime = request.POST.get("anime")

        try:
            submitted = Submission(name=name, joke=joke, anime=anime)
            submitted.save()
            success = "Successfully sent! Thanks for submitting :)"
            return render(request, "index.html", {'setup': setup, 'punchline': punchline, 'success': success})
        except:
            success = ''
            return render(request, "index.html", {'setup': setup, 'punchline': punchline, 'success': success})
    
    return render(request, "index.html", {'setup': setup, 'punchline': punchline, 'success': success})



