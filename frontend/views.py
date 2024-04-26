from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html")

def snap_gpt(request):
    data = request.GET.get('data')
    return render(request, "interact.html", context={
        "data": data
    })