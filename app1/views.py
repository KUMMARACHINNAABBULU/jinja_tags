from django.shortcuts import render

# Create your views here.
def tag(request):
    d={'a':10,'b':20,'c':30}
    return render(request,'tag.html',context=d)
def forloop(request):
    x={'l':[10,20,30],'v':(1,2,3)}
    return render(request,'forloop.html',context=x)