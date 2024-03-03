from django.urls import re_path
from django.contrib.auth import views as auth_views
from . import views
from .forms import OirePasswordChangeForm, OirePasswordResetForm, OireSetPasswordForm

urlpatterns = [
    # User management urls
    re_path(r'^users/$',
        views.UserListView.as_view(),
        name='user_list'),
    re_path(r'^users/new/$',
        views.UserAddView.as_view(),
        name='new_user'),
    re_path(r'^users/(?P<pk>\d+)/edit/$',
           views.UserUpdateView.as_view(),
           name='user_edit'),

    # Login and logout urls
    re_path(r'^login/$',
        views.OireLoginView.as_view(),
        name='login'),

    re_path(r'^logout/$',
        auth_views.LogoutView.as_view(),
        name='logout'),

    # Change password urls
    re_path(r'^password-change/$',
        auth_views.PasswordChangeView.as_view(),
        {'password_change_form': OirePasswordChangeForm},
        name='password_change'),
    re_path(r'^password-change/done/$',
        auth_views.PasswordChangeDoneView.as_view(),
        name='password_change_done'),

    # Reset password urls
    re_path(r'^password-reset/$',
        views.OirePasswordResetView.as_view(),
        name='password_reset'),
    re_path(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
        auth_views.PasswordResetConfirmView.as_view(),
        {'set_password_form': OireSetPasswordForm},
        name='password_reset_confirm'),
    re_path(r'^password-reset/done/$',
        auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done'),
    re_path(r'^password-reset/complete/$',
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete'),

]
