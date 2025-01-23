
from django.shortcuts import render, redirect
from . import viix_api


def main(request):
    return render(request, "app_main/index.html", context={
        "title": "Viix AI-search for AI-tools",
        "description": "AI-search for AI-tools. Combined with AI, it can revolutionize the workplace. Viix brings comprehensive, accurate, and search-based AI"})


def ai_search(request):
    api = viix_api.get_api()
    result = None
    results_amount = ""
    query = ""

    if request.method == "POST":
        if request.POST.get("search_action_btn"):
            query = request.POST.get("query", "")

            if query:
                result = api.ai_search(query)
                results_amount = str(len(result)) if result is not None else "0"
                print(f"ai_search query:{query}, result.sz={results_amount}")

    return render(request, "app_main/ai-search.html", context={
        "title": "Viix Search engine powered by AI",
        "description": "Search engine powered by AI. Tired of ads clogging up your search results? Get Answers. Not ads.",
        "content_list": result,
        "results_amount": results_amount,
        "search_request": query,
        "classify_categories": []
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
