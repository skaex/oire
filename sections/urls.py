from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^semesters/$',
        views.SemesterListView.as_view(),
        name='semester_list'),
    re_path(r'^semesters/new/$', views.SemesterAddView.as_view(),
        name='new_semester'),
    re_path(r'^semesters/(?P<pk>\d+)/edit/$',
        views.SemesterUpdateView.as_view(),
        name='semester_edit'),
    re_path(r'^semesters/(?P<pk>\d+)/delete/$',
        views.SemesterDeleteView.as_view(),
        name='semester_delete'),
    re_path(r'^helpers/$',
        views.HelperListView.as_view(),
        name='helper_list'),
    re_path(r'^sections/$',
        views.SectionListView.as_view(),
        name='section_list'),
    re_path(r'^sections/new/$', views.SectionAddView.as_view(),
        name='new_section'),
    re_path(r'^sections/(?P<pk>\d+)/edit/$',
        views.SectionUpdateView.as_view(),
        name='section_edit'),
    re_path(r'^sections/(?P<pk>\d+)/delete/$',
        views.SectionDeleteView.as_view(),
        name='section_delete'),
    re_path(r'^section/open/(?P<section>\d+)/$',
        views.SectionOpenView.as_view(),
        name='section_open'),
    re_path(r'^section/close/(?P<section>\d+)/$',
        views.SectionCloseView.as_view(),
        name='section_close'),
    re_path(r'^sections/load/$',
        views.SectionLoadView.as_view(),
        name='load_sections'),

    re_path(r'^presections/$',
        views.PreSectionListView.as_view(),
        name='presection_list'),
    re_path(r'^presections/new/$', views.PreSectionAddView.as_view(),
        name='new_presection'),
    re_path(r'^presections/(?P<pk>\d+)/edit/$',
        views.PreSectionUpdateView.as_view(),
        name='presection_edit'),
    re_path(r'^presections/(?P<pk>\d+)/delete/$',
        views.PreSectionDeleteView.as_view(),
        name='presection_delete'),
    re_path(r'^presections/(?P<presection>\d+)/refresh/$',
        views.PreSectionRefreshView.as_view(),
        name='presection_refresh'),
    re_path(r'^presections/load/$',
        views.PreSectionLoadView.as_view(),
        name='load_presections'),
    ]
