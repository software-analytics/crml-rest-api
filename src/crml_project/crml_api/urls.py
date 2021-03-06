from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^review/$', views.ReviewApiView.as_view()),
    url(r'^predict/$', views.Predict),
    url(r'^review/(?P<id>[a-zA-Z0-9]+)$', views.ReviewApiView.as_view()),
    url(r'^models/$', views.MLModels)
    
]
