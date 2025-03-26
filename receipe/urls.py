from django.urls import path
from . import views

urlpatterns = [
    path('',views.Receipe,name="receipe"),
    path('create/',views.index,name="index"),
    path('delete-receipe/<id>/',views.delete_food,name="delete"),
    path('update-receipe/<id>/',views.update_food,name="update"),
    path('login/',views.login_page,name="login"),
    path("register/",views.register_page,name="register"),
    path('logout/',views.logout_page,name="logout"),
    path('food/',views.food,name="food"),
    path('order/<id>/',views.order_food,name="order"),
    path('myorder/',views.myorder,name="myorder"),
    path('cancel/<id>',views.cancel_order,name="cancel")
]
