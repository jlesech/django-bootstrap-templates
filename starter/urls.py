from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='starter/index.html'), name='index'),
    url(r'^about/$', TemplateView.as_view(template_name='starter/about.html'), name='about'),
    url(r'^contact/$', TemplateView.as_view(template_name='starter/contact.html'), name='contact'),
)
