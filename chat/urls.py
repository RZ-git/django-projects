from django.conf.urls import url
from chat.views import views

view = views.ViewSet()

urlpatterns = [
    url(r'^$', view.index, name='index'),
    url(r'^hello_world/$', view.hello_world, name='hello_world'),
]
