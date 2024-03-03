from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$',
        views.ReportListView.as_view(),
        name='report_list'),
    re_path(r'^evaluate/sections/(?P<section>\d+)/$',
        views.EvaluationSubmitView.as_view(),
        name='submit_evaluation'),
    re_path(r'^credits/$',
        views.CreditsView.as_view(),
        name='credits'),
    re_path(r'^sections/(?P<section>\d+)/evaluations/(?P<evaluation>\d+)/$',
        views.ReportDetailView.as_view(),
        name='detail_report'),

]
