"""to_do2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('new_url/', views.new, name="new"),
    path('detail_url/<int:pk>', views.detail, name="detail"),

    path('edit_url/<int:post_pk>', views.edit, name="editname"),
    path('delete_url/<int:post_pk>', views.delete, name="deletename"),
    path('delete_comment_url/<int:post_pk>/<int:comment_pk>', views.delete_comment, name="delete_comment"),

    path('registration/signup', views.signup, name="signup"),
    path('registration/login', views.login, name="login"),
    path('registration/logout', views.logout, name="logout"),

    # path('accounts/', include('allauth.urls')),

    path('my_post_list_url', views.my_post_list, name="my_post_list")
]

