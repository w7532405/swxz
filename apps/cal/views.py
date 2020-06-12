from django.shortcuts import render

# Create your views here.
def cal(request):
    return render(request,'detail/cal/index.html')