from django.shortcuts import render, HttpResponse


# Create your views here.
def home(request):
    peoples = [
        {"name": "John", "age": 30},
        {"name": "Himanshu", "age": 20},
        {"name": "Doe", "age": 25},
        {"name": "Smith", "age": 14},
        {"name": "Jane", "age": 8},
        ]
    
    # Context is for passing data from the view to the template
    return render(request, 'home.html', context={'page':'Home', "peoples": peoples})

def contact(request):
    context = {'page':'Contact Us'}
    return render(request, 'contact.html', context)

def about(request):
    context = {'page':'About Us'}
    return render(request, 'about.html', context)