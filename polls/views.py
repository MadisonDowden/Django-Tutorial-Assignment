from django.shortcuts import render


def index(request):
    context = {
        "page_title": "Polls App",
        "welcome_message": "Welcome to the Polls App!",
        "description": "This page is displaying dynamic data from a Django view.",
        "courses": [
            "Python",
            "Django",
            "HTML",
            "CSS"
        ]
    }

    return render(request, "polls/index.html", context)