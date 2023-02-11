from django.urls import path
from . import views
# import outer modules

urlpatterns = [
    path('', views.index, name="home_users"),
    path('', views.index_test, name="index_test"),
    # path('', views.login, name="login"),
    # path('', views.register, name="register"),
    # path('home_dentist/', views_dentist.index_test, name="home_dentist"),
    # path('hello/<str:username>', views.hello, name="hello"),
    # path('projects/', views.projects, name="projects"),
    # path('projects/<int:id>', views.project_detail, name="project_detail"),
    # path('tasks/', views.tasks, name="tasks"),
    # path('create_task/', views.create_task, name="create_task"),
    # path('create_project/', views.create_project, name="create_project"),
]