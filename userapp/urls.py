from django.urls import path
from .views import login, logout, pass_change, dashboard, homepage

urlpatterns = [
    path('', homepage, name=""),
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
    path('pass_change/', pass_change),
    path('dashboard/', dashboard, name="dashboard"),
    #path('new_job/', new_job),
    #path('list_job', list_job),
]