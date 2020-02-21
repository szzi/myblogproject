from django.shortcuts import render
from .models import Portfolio

def portfolio(request): #portfolio.html 띄워주기
    portfolios = Portfolio.objects #객체가져오기
    return render(request,'portfolio.html',{'portfolios':portfolios})
# Create your views here.
