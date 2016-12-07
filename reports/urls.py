from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',
        views.ReportListView.as_view(),
        name='report_list'),
    url(r'^evaluate/sections/(?P<section>\d+)/$',
        views.EvaluationSubmitView.as_view(),
        name='submit_evaluation'),
    url(r'^credits/$',
        views.CreditsView.as_view(),
        name='credits'),
    url(r'^sections/(?P<section>\d+)/evaluations/(?P<evaluation>\d+)/$',
        views.ReportDetailView.as_view(),
        name='detail_report'),

]
