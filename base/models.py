from django.db import models

class Joke(models.Model):
    setup = models.CharField(max_length=500)
    punchline = models.CharField(max_length=500, null=True, blank=True)
    joke_anime = models.ForeignKey('Anime', on_delete=models.CASCADE, null=True)
    author = models.CharField(max_length=200, null=True, blank=True)
    added = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.setup)[:100] 

class Anime(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    added = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.name

class Submission(models.Model):
    name = models.CharField(max_length=200)
    joke = models.TextField(null=True, blank=True)
    anime = models.CharField(max_length=200)
    added = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.joke


    