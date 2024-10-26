from django.urls import path
from django.contrib.auth import views as auth_views
from .views import login, logout, change_password, dashboard, homepage, register, access_denied
from .forms import CustomPasswordResetForm
urlpatterns = [
    path('', homepage, name="homepage"),
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
    path('register/', register, name="register"),
    path('change_password/', change_password, name="change_password"),
    path('access_denied/', access_denied, name="access_denied"),
    path('dashboard/', dashboard, name="dashboard"),
    # path('new_job/', new_job),
    # path('list_job', list_job),
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='userapp/password_reset_form.html',
        form_class=CustomPasswordResetForm,
    ), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='userapp/password_reset_done.html',
    ), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='userapp/password_reset_confirm.html',
    ), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='userapp/password_reset_complete.html',
    ), name='password_reset_complete'),
]
