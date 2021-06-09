from django.shortcuts import render

# Create your views here.

def loginimpl(request):
    id = request.POST['id'];
    pwd = request.POST['pwd'];
    print(id,pwd);
    return render(request, 'js04.html');

def regimpl(request):
    id = request.POST['id'];
    pwd = request.POST['pwd'];
    name = request.POST['name'];
    age = request.POST['age'];
    return render(request, 'registerok.html');