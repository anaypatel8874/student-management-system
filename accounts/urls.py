from django.urls import path
from django.contrib.auth.views import (
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)

from . import views

urlpatterns = [

    path(
        "register/",
        views.register,
        name="register",
    ),

    path(
        "login/",
        views.UserLoginView.as_view(),
        name="login",
    ),

    path(
        "dashboard/",
        views.dashboard,
        name="dashboard",
    ),

    path(
        "dashboard/students/",
        views.students_page,
        name="students_page",
    ),

    path(
        "dashboard/teachers/",
        views.teachers_page,
        name="teachers_page",
    ),

    path(
        "dashboard/courses/",
        views.courses_page,
        name="courses_page",
    ),

    path(
        "dashboard/reports/",
        views.reports_page,
        name="reports_page",
    ),

    path(
        "dashboard/settings/",
        views.settings_page,
        name="settings_page",
    ),

    path(
        "profile/",
        views.profile,
        name="profile",
    ),

    path(
        "logout/",
        LogoutView.as_view(next_page="login"),
        name="logout",
    ),

    path(
        "password-reset/",
        PasswordResetView.as_view(
            template_name="accounts/password_reset.html",
            email_template_name="accounts/password_reset_email.html",
            subject_template_name="accounts/password_reset_subject.txt",
            success_url="/password-reset/done/",
        ),
        name="password_reset",
    ),

    path(
        "password-reset/done/",
        PasswordResetDoneView.as_view(
            template_name="accounts/password_reset_done.html",
        ),
        name="password_reset_done",
    ),

    path(
        "password-reset-confirm/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(
            template_name="accounts/password_reset_confirm.html",
            success_url="/password-reset/complete/",
        ),
        name="password_reset_confirm",
    ),

    path(
        "password-reset/complete/",
        PasswordResetCompleteView.as_view(
            template_name="accounts/password_reset_complete.html",
        ),
        name="password_reset_complete",
    ),

]
