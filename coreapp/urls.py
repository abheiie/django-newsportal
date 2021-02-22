from django.urls import path
from .views import home_view, article_category, article_detail, login_form_view, login_view, logout_view, register_form_view, register_view


app_name = "coreapp"


urlpatterns = [
    path('', home_view, name = 'home_view' ),
    path('article/<int:id>', article_detail, name="article_detail" ),
    path('<str:category>', article_category, name = "article_category"),
    path('login/', login_form_view, name = 'login_form_view' ),

    #register
    path('register/', register_form_view, name='register_form_view'), 
    path('register_view/', register_view, name='register_view'), 
    path('login_view/', login_view, name='login_view'), 
    #logout
    path('logout/', logout_view, name='logout_view'),


]

