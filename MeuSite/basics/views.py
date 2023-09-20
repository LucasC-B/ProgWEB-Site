from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'basics/homePage.html')

def about(request):
    return render(request, 'basics/aboutPage.html')