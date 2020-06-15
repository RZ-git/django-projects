from django.http.response import HttpResponse
from django.shortcuts import render


class ViewSet:
    """ View関数クラス """

    @staticmethod
    def index(request):
        return render(request, 'index.html')

    @staticmethod
    def hello_world(request):
        return render(request, 'hello_world.html')
