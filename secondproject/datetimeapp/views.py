from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def datetimefun(request):
    date=datetime.datetime.now()
    msg='<h1>Hello friend good evening!!</h1><hr>'
    msg=msg+'<h1>The current time is:'+str(date)+'</h1>'
    return HttpResponse(msg)
