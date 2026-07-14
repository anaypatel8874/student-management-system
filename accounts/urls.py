from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    # Home
    path("", views.home, name="home"),

    # Authentication
    path("register/", views.register, name="register"),
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),

    # Dashboard
    path("dashboard/", views.dashboard, name="dashboard"),

    # Other Pages
    path("dashboard/students/", views.students_page, name="students_page"),
    path("dashboard/teachers/", views.teachers_page, name="teachers_page"),
    path("dashboard/courses/", views.courses_page, name="courses_page"),
    path("dashboard/reports/", views.reports_page, name="reports_page"),
    path("dashboard/settings/", views.settings_page, name="settings_page"),

    path("profile/", views.profile, name="profile"),
]
