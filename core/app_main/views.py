
from django.shortcuts import render, redirect

# def main(request):
#     return redirect('app_main:ai-search')


def ai_search(request):
    return render(request, "app_main/ai-search.html", context={})
