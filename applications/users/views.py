from django.shortcuts import render

def index(request):
    context = dict()
    title = 'Home'
    context['title'] = title
    return render(request, "basic/index.html", context)

def about(request):
    context = dict()
    title = 'About'
    context['title'] = title
    return render(request, "basic/about.html", context)

def services(request):
    context = dict()
    title = 'Services'
    context['title'] = title
    return render(request, "basic/services.html", context)

def portfolio(request):
    context = dict()
    title = 'Portfolio'
    context['title'] = title
    return render(request, "basic/portfolio.html", context)

# def contact(request):
#     context = dict()
#     return render(request, "basic/contact.html", context)

def testimony(request):
    context = dict()
    title = 'Testimony'
    context['title'] = title
    return render(request, "basic/testimony.html", context)