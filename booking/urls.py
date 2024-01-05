from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index),
    path('logins',views.logins),
    path('register',views.register),
    path('book',views.book),
    path('search',views.search),
    path('viewticket/search2',views.search2),
    path('viewticket/',views.viewtickets),
]
