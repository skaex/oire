from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^schools/$',
        views.SchoolListView.as_view(),
        name='school_list'),
    url(r'^schools/new/$', views.SchoolAddView.as_view(),
        name='new_school'),
    url(r'^schools/(?P<pk>\d+)/edit/$',
        views.SchoolUpdateView.as_view(),
        name='school_edit'),
    url(r'^schools/(?P<pk>\d+)/delete/$',
        views.SchoolDeleteView.as_view(),
        name='school_delete'),
    url(r'^courses/$',
        views.CourseListView.as_view(),
        name='course_list'),
    url(r'^courses/new/$', views.CourseAddView.as_view(),
        name='new_course'),
    url(r'^courses/(?P<pk>\d+)/edit/$',
        views.CourseUpdateView.as_view(),
        name='course_edit'),
    url(r'^courses/(?P<pk>\d+)/delete/$',
        views.CourseDeleteView.as_view(),
        name='course_delete'),
]
