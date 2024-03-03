from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^schools/$',
        views.SchoolListView.as_view(),
        name='school_list'),
    re_path(r'^schools/new/$', views.SchoolAddView.as_view(),
        name='new_school'),
    re_path(r'^schools/(?P<pk>\d+)/edit/$',
        views.SchoolUpdateView.as_view(),
        name='school_edit'),
    re_path(r'^schools/(?P<pk>\d+)/delete/$',
        views.SchoolDeleteView.as_view(),
        name='school_delete'),
    re_path(r'^courses/$',
        views.CourseListView.as_view(),
        name='course_list'),
    re_path(r'^courses/new/$', views.CourseAddView.as_view(),
        name='new_course'),
    re_path(r'^courses/(?P<pk>\d+)/edit/$',
        views.CourseUpdateView.as_view(),
        name='course_edit'),
    re_path(r'^courses/(?P<pk>\d+)/delete/$',
        views.CourseDeleteView.as_view(),
        name='course_delete'),
]
