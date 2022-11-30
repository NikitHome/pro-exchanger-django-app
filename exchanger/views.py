from django.shortcuts import render

def index(request): 
    return render(request, 'exchanger/index.html')

def contacts(request): 
    return render(request, 'exchanger/contacts.html')

def partners(request): 
    return render(request, 'exchanger/partners.html')

def cooperation(request): 
    return render(request, 'exchanger/cooperation.html')

def exchange_rules(request): 
    return render(request, 'exchanger/exchange_rules.html')

def exchange(request):
    return render(request, 'exchanger/exchange.html')