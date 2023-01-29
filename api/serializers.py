from rest_framework import serializers 
from base.models import Joke, Anime 

class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = ['name', 'description', '_id']

class JokeSerializer(serializers.ModelSerializer):
    joke_anime = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Joke
        fields = ['setup', 'punchline','joke_anime', 'author', '_id']

    def get_joke_anime(self, obj):
        try:
            animename = AnimeSerializer(obj.joke_anime, many=False).data
        except:
            animename = False

        return animename["name"]