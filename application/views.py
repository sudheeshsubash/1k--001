from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def listprojects(request):
    return render(request, 'listprojects.html')


def projects(request, id):
    return render(request, 'project.html')


def listmembers(request):
    return render(request, 'listmembers.html')


def members(request, id):
    return render(request, 'member.html')


