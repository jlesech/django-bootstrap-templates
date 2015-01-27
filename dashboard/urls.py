from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='dashboard/index.html'), name='index'),
    url(r'^reports/$', TemplateView.as_view(template_name='dashboard/reports.html'), name='reports'),
    url(r'^analytics/$', TemplateView.as_view(template_name='dashboard/analytics.html'), name='analytics'),
    url(r'^export/$', TemplateView.as_view(template_name='dashboard/export.html'), name='export'),
)
