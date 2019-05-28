from django.conf.urls import url
from . import views

app_name='shop'
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^about/$',views.about,name='about'),
    url(r'^faqs/$',views.faqs,name='faqs'),
    url(r'^icons/$',views.icons,name='icons'),
    url(r'^typography/$',views.typography,name='typography'),
    url(r'^contact/$',views.contact,name='contact'),
]