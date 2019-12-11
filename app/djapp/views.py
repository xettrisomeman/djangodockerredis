from django.shortcuts import render
import redis

# if we are using redis without docker
# cache = redis.Redis(host="localhost", port=6379, db=0)

#with docker
cache = redis.Redis(host='redis')

def index(request):
    hits = cache.incr('hits')
    data={
        'hits':hits
    }
    return render(request ,'homepage.html' ,data)

