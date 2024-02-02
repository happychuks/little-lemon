from django.urls import path
from . import views

app_name = "website"

# Also called url router
urlpatterns = [
    path('', views.home, name="home"),
    path('form/', views.form_view, name="form"),
    # path('menu/', views.menu, name="menu"),
    path('menus/', views.menu_by_id),
    path('about/', views.about, name="about"),
    path('booking/', views.booking_form_view, name = "booking"),
    path('drinks/<str:drink_name>', views.drinks, name="drink_name"),
]
