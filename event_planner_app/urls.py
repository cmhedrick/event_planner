from django.conf.urls import url

from event_planner_app import views

urlpatterns = [
    url(r'^$', views.IndexPageView.as_view()),
    url(r'^all-employees/$', views.EmployeeListAllView.as_view()),
    #url(r'^all-clients/$', views.ClientListAllView.as_view()),
    #url(r'^all-events/$', views.EventListAllView.as_view()),
]
