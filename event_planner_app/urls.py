from django.conf.urls import url

from event_planner_app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
