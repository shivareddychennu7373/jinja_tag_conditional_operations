from django.shortcuts import render

# Create your views here.
def hai(request):
    d={'a':10}
    return render(request,"hai.html",d)
def bye(request):
    d={'a':10,'b':20}
    return render(request,"bye.html",d)
def first(request):
    menu={'a':100,'b':15,'c':1000}
    return render(request,'first.html',menu)