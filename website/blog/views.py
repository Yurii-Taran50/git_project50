from django.shortcuts import render
import random
import datetime


def randNum():
    return random.randint(1, 10)


def index(request):
    list = ["first", "second", "next", 100, 300]
    context = {
        "title": "Blog",
        "number": 100,
        "data": list,
        "randnum": randNum,
        "now": datetime.datetime.now(),
        "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,"
    }
    return render(request, "blog/index.html", context)
