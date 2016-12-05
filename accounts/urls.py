from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .forms import OireAuthenticationForm, OirePasswordChangeForm, OirePasswordResetForm, OireSetPasswordForm

urlpatterns = [
    # Login and logout urls
    url(r'^login/$',
        auth_views.login,
        {'authentication_form': OireAuthenticationForm},
        name='login'),
    url(r'^logout/$',
        auth_views.logout,
        name='logout'),

    # Change password urls
    url(r'^password-change/$',
        auth_views.password_change,
        {'password_change_form': OirePasswordChangeForm},
        name='password_change'),
    url(r'^password-change/done/$',
        auth_views.password_change_done,
        name='password_change_done'),

    # Reset password urls
    url(r'^password-reset/$',
        auth_views.password_reset,
        {'password_reset_form': OirePasswordResetForm},
        name='password_reset'),
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
        auth_views.password_reset_confirm,
        {'set_password_form': OireSetPasswordForm},
        name='password_reset_confirm'),
    url(r'^password-reset/done/$',
        auth_views.password_reset_done,
        name='password_reset_done'),
    url(r'^password-reset/complete/$',
        auth_views.password_reset_complete,
        name='password_reset_complete'),

]