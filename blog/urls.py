from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register_page, name="register"),
    path("login/", views.login_page, name="login"),
    path("logout/", views.logout_User, name="logout"),
    path("create-post", views.create_post, name="create-post"),
    path("view-post/<int:post_id>", views.view_post, name="view-post"),
    path("edit-post/<int:post_id>", views.edit_post, name="edit-post"),
    path("delete-post/<int:post_id>", views.delete_post, name="delete-post"),
]
