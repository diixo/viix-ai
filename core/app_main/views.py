
from django.shortcuts import render, redirect

def main(request):
    return render(request, "app_main/index.html", context={})


def ai_search(request):
    return render(request, "app_main/ai-search.html", context={})
