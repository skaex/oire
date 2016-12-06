from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^semesters/$',
         views.SemesterListView.as_view(),
         name='semester_list'),
  url(r'^semesters/new/$', views.SemesterAddView.as_view(),
    name='new_semester'),
  url(r'^semesters/(?P<pk>\d+)/edit/$',
           views.SemesterUpdateView.as_view(),
           name='semester_edit'),
  url(r'^semesters/(?P<pk>\d+)/delete/$',
           views.SemesterDeleteView.as_view(),
           name='semester_delete'),
  url(r'^sections/$',
         views.SectionListView.as_view(),
         name='section_list'),
  url(r'^sections/new/$', views.SectionAddView.as_view(),
    name='new_section'),
  url(r'^sections/(?P<pk>\d+)/edit/$',
           views.SectionUpdateView.as_view(),
           name='section_edit'),
  url(r'^sections/(?P<pk>\d+)/delete/$',
           views.SectionDeleteView.as_view(),
           name='section_delete'),

]