from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser 
from rest_framework.response import Response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .serializers import JokeSerializer, AnimeSerializer
from base.models import Joke, Anime


@api_view(['GET'])
def getRoutes(request):
    routes = [ 
        {'GET': '/api/jokes'},
        {'GET': '/api/jokes/id'},
        # {'GET': '/api/jokes/id/vote'},

        # to get tokens for user to login users 
        {'POST': '/api/user/token'},
        {'POST': '/api/user/token/refresh'}
    ]

    return Response(routes)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getJokes(request):
    query = request.query_params.get('search')

    if query == None:
        query = ''

    jokes = Joke.objects.filter(setup__icontains=query).order_by('-added')

    page = request.query_params.get('page')
    paginator = Paginator(jokes, 5)

    try:
        jokes = paginator.page(page)
    except PageNotAnInteger:
        jokes = paginator.page(1)
    except EmptyPage:
        jokes = paginator.page(paginator.num_pages)


    # jokes = Joke.objects.all()
    serializer = JokeSerializer(jokes, many=True)

    return Response(serializer.data)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getJoke(request, pk):
    joke = Joke.objects.get(_id=pk)
    serializer = JokeSerializer(joke, many=False)

    return Response(serializer.data)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getAnimes(request):
    query = request.query_params.get('anime')

    if query == None:
        animes = Anime.objects.all().order_by('-added')

        page = request.query_params.get('page')
        paginator = Paginator(animes, 5)

        try:
            animes = paginator.page(page)
        except PageNotAnInteger:
            animes = paginator.page(1)
        except EmptyPage:
            animes = paginator.page(paginator.num_pages)

        serializer = AnimeSerializer(animes, many=True) 

    else:
        lowerName = query.lower()

        anime = Anime.objects.get(name=lowerName)
        jokes = anime.joke_set.all().order_by('-added')

        page = request.query_params.get('page')
        paginator = Paginator(jokes, 5)

        try:
            jokes = paginator.page(page)
        except PageNotAnInteger:
            jokes = paginator.page(1)
        except EmptyPage:
            jokes = paginator.page(paginator.num_pages)

        serializer = JokeSerializer(jokes, many=True) 
    
    return Response(serializer.data)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getAnime(request, pk):
    anime = Anime.objects.get(_id=pk)
    serializer = AnimeSerializer(anime, many=False)

    return Response(serializer.data)


# @api_view(['POST'])
# @permission_classes([IsAdminUser])
# def createJoke(request):
#     user = request.user

#     joke = Joke.objects.create(
#         author = 'Sample author',
#         setup = "Sample setup",
#         punchline = 'Sample description',
#         joke_category = 1
#     )

#     serializer = JokeSerializer(joke, many=False)

#     return Response(serializer.data)
