from django.shortcuts import render

# Create your views here.
def conditional(request):
    d={'a':1000,'b':200}
    return render(request,'conditional.html',d)