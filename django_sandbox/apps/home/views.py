from django.shortcuts import render


def view_homepage(request):
    context = {

    }
    return render(request, 'home/home.html', context)