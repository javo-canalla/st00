from django.urls import path
from .views import login, logout, change_password, dashboard, homepage, register, forgot_password, access_denied

urlpatterns = [
    path('', homepage, name="homepage"),
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
    path('register/', register, name="register"),
    path('change_password/', change_password, name="change_password"),
    path('forgot_password/', forgot_password, name="forgot_password"),
    path('access_denied/', access_denied, name="access_denied"),
    path('dashboard/', dashboard, name="dashboard"),
    # path('new_job/', new_job),
    # path('list_job', list_job),
]
