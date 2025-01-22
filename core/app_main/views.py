
from django.shortcuts import render, redirect
from . import viix_api


def main(request):
    return render(request, "app_main/index.html", context={
        "title": "Viix AI-search for AI-tools",
        "description": "AI-search for AI-tools. Combined with AI, it can revolutionize the workplace. Viix brings comprehensive, accurate, and search-based AI"})


def ai_search(request):
    api = viix_api.get_api()
    if request.method == "POST":

        button_value = request.POST.get("search_action_btn")

        if button_value:
            query = request.POST.get("query", "")
            print(f"ai_search query:{query}")
            api.ai_search(search_request=query)

    return render(request, "app_main/ai-search.html", context={
        "title": "Viix Search engine powered by AI",
        "description": "Search engine powered by AI. Tired of ads clogging up your search results? Get Answers. Not ads."
        })


def add_text(request):
    api = viix_api.get_api()
    if request.method == "POST":
        button_value = request.POST.get("submit_txt_btn")

        if button_value:
            txt = request.POST.get("input_txt_field", "")
            print(f"add_text:{txt}")
            api.text_to_index(txt)
            return redirect(to="app_main:ai-search")

    return render(request, "app_main/add-text.html", context={
        "title": "viix add_text: AI-search",
        "description": "add_text: viix AI-search for AI-tools"})


def add_page(request):
    api = viix_api.get_api()
    if request.method == "POST":
        button_value = request.POST.get("submit_url_btn")

        if button_value:
            txt = request.POST.get("input_url_field", "")
            print(f"add_page:{txt}")
            api.page_to_index(txt)
            return redirect(to="app_main:ai-search")

    return redirect(to="app_main:ai-search")
    return render(request, "app_main/add-page.html", context={
        "title": "viix add_page: AI-search",
        "description": "add_page: viix AI-search for AI-tools"})
