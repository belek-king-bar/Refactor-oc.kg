from django.urls import path, include
from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

app_name = 'webauth'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signup/signup_complete/', TemplateView.as_view(template_name="registration/signup_complete.html"),
         name='signup_complete'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
]
