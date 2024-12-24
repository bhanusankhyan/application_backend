from django.urls import path

from . import views

urlpatterns = [
    path("signup", views.signup, name="signup"),
    path("csrf", views.csrf, name="csrf"),
    path("login", views.login, name="login"),
    path("create_category", views.createCategory, name="create_category"),
    path("create_sub_category", views.createSubCategory, name="create_sub_categories"),
    path("categories", views.getCategories, name="categories"),
    path('sub_categories', views.getSubCategories, name="sub_categories"),
    path('create_application', views.createApplication, name="create_application"),
    path('get_application/search', views.getApplication, name="get_application"),
    path('get_applications', views.getApplications, name="get_applications"),
    path('download_application', views.downloadApplication, name="download_applications"),
    path('user_data', views.getUserData, name="user_data"),
    path('completed_tasks', views.getCompletedTasks, name="completed_tasks"),
    path('remaining_tasks', views.getRemainingTasks, name="remaining_tasks"),
]
