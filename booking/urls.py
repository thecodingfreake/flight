from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index),
    path('logins',views.logins),
    path('register',views.register),
    path('book',views.book),
    path('search',views.search),
    path('viewticket/',views.viewtickets),
]
