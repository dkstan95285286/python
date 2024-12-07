from django.http import HttpResponse
from django.shortcuts import render

def home(responce):
    # return HttpResponse("hello , you are at django homepage")
      return render(responce, 'website/index.html')

def about(responce):
    # return HttpResponse("hello , you are at django about page")
      return render(responce, 'website/about.html')


def contact(responce):
    # return HttpResponse("hello , you are at django contact page")
      return render(responce, 'website/contact.html')