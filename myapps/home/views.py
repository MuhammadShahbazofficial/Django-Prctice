from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hi I'm Shobii Khan.")
    
def download(request):
    return HttpResponse("You can download it.")

def html(request):
     
     student = [
        {'name': 'zaid umer', 'age': '20'},
        {'name': 'hamza latif', 'age': '22'},
        {'name': 'faizan maher', 'age': '24'},
        {'name': 'nadeem ahmad', 'age': '21'},
        {'name': 'shahabaz', 'age': '25'},
    ]


     return render(request, "index.html", context = {'student' : student})
#context keyword is used for the rendring the backend data into  Html page(static page).
