from django.shortcuts import render
from django.http import HttpResponse


from . import models, forms


# Create your views here.
def hello_world(request):
    return HttpResponse("hello")


def blog_all(request):
    post = models.Post.objects.all()
    return render(request, "index.html", {"post": post})


def main(request):
    events = models.Events.objects.all()
    mainpage = models.Mainpage.objects.all()
    return render(request, "main.html", {"events": events, 'mainpage': mainpage})


def service(request):
    menu = models.Menu.objects.all()
    servicepage = models.Servicepage.objects.all()
    return render(request, "service.html", {"menu": menu, 'servicepage': servicepage})


def about(request):
    about = models.About.objects.all()
    aboutpage = models.Aboutpage.objects.all()
    return render(request, "about.html", {"about": about, 'aboutpage': aboutpage})


def order(request):
    method = request.method
    if method == "POST":
        form = forms.Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, "add_form.html", {"form": form})
        else:
            form = forms.Form()
        return render(request, 'add_form.html', {'form': form})


    orderpage = models.Orderpage.objects.all()
    form = models.Form.objects.all()
    return render(request, "add_form.html", {"form": form, 'orderpage': orderpage})

def form(request):
    method = request.method
    if method == "POST":
        form = forms.Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, "form.html", {"form": form})

    else:
        form = forms.Form()
    return render(request, "form.html", {"form": form})
