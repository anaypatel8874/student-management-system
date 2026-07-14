from django.urls import path
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
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

    # Student CRUD
    path("students/", views.student_list, name="student_list"),
    path("students/add/", views.add_student, name="add_student"),

    # Other Pages
    path("dashboard/students/", views.students_page, name="students_page"),
    path("dashboard/teachers/", views.teachers_page, name="teachers_page"),
    path("dashboard/courses/", views.courses_page, name="courses_page"),
    path("dashboard/reports/", views.reports_page, name="reports_page"),
    path("dashboard/settings/", views.settings_page, name="settings_page"),

    path("profile/", views.profile, name="profile"),

    # Password Reset
    path(
        "password-reset/",
        auth_views.PasswordResetView.as_view(
            template_name="accounts/password_reset.html"
        ),
        name="password_reset",
    ),

    path(
        "password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="accounts/password_reset_done.html"
        ),
        name="password_reset_done",
    ),

    path(
        "password-reset-confirm/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="accounts/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),

    path(
        "password-reset-complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="accounts/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
]