from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def base(request):
    return render(request, 'base.html', {'name' : 'Friends!!'})

def result(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    res = val1 + val2
    return render(request, 'result.html',{'result' : res})