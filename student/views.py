from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    return render(request, 'website-pages/home.html')
    
    # return HttpResponse("<center><h1>This is the Home </h1></center>")

def contact(request):
    return render(request, 'website-pages/contact.html')
    return HttpResponse("<center><h1>This is the Contact </h1></center>")
def about(request):
    return render(request, 'website-pages/about.html')

def students(request):
    return render(request, 'student/pages/index.html')

    # return HttpResponse("<center><h1>This is the Students page </h1></center>")

def details(request, id):
    return render(request, 'student/pages/studdetail.html', {'studentid': str(id)})

    # return HttpResponse("<center><h1>This is the details <code> " + str(id) + "</code></h1></center>")


# Create your views here.
