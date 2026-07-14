from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .forms import StudentForm

from .forms import RegisterForm


# -----------------------------
# Register View
# -----------------------------
def register(request):

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Registration Successful! Please login."
            )

            return redirect("login")

    else:

        form = RegisterForm()

    return render(
        request,
        "accounts/register.html",
        {
            "form": form
        }
    )


# -----------------------------
# Login View
# -----------------------------
class UserLoginView(LoginView):

    template_name = "accounts/login.html"

    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("dashboard")


# -----------------------------
# Dashboard
# -----------------------------
@login_required
def dashboard(request):

    context = {

        "active_page": "dashboard",

        "total_users": User.objects.count(),

        "total_students": User.objects.count(),

        "username": request.user.username,

        "email": request.user.email,

        "first_name": request.user.first_name,

    }

    return render(
        request,
        "accounts/dashboard.html",
        context
    )


def dashboard_section_context(request, active_page, page_title, section_label, search_placeholder, cards, table_label, table_title, headings, rows):
    return {
        "active_page": active_page,
        "page_title": page_title,
        "section_label": section_label,
        "search_placeholder": search_placeholder,
        "cards": cards,
        "table_label": table_label,
        "table_title": table_title,
        "headings": headings,
        "rows": rows,
    }


@login_required
def students_page(request):
    context = dashboard_section_context(
        request,
        "students",
        "Students",
        "Manage Students",
        "Search students",
        [
            {"label": "Total Students", "value": User.objects.count(), "icon": "fa-solid fa-user-graduate", "color": "blue"},
            {"label": "Active", "value": "86", "icon": "fa-solid fa-circle-check", "color": "green"},
            {"label": "Pending", "value": "12", "icon": "fa-solid fa-clock", "color": "orange"},
            {"label": "Inactive", "value": "4", "icon": "fa-solid fa-user-slash", "color": "red"},
        ],
        "Directory",
        "Student List",
        ["ID", "Name", "Branch", "Status"],
        [
            ["101", "Anay Patel", "CSE", "Active"],
            ["102", "Rahul Kumar", "IT", "Active"],
            ["103", "Priya Singh", "ECE", "Pending"],
            ["104", "Akash Sharma", "ME", "Inactive"],
        ],
    )
    return render(request, "accounts/dashboard_section.html", context)


@login_required
def teachers_page(request):
    context = dashboard_section_context(
        request,
        "teachers",
        "Teachers",
        "Faculty",
        "Search teachers",
        [
            {"label": "Total Teachers", "value": "24", "icon": "fa-solid fa-chalkboard-user", "color": "blue"},
            {"label": "Departments", "value": "6", "icon": "fa-solid fa-building-columns", "color": "green"},
            {"label": "On Leave", "value": "2", "icon": "fa-solid fa-calendar-minus", "color": "orange"},
            {"label": "New Hires", "value": "3", "icon": "fa-solid fa-user-plus", "color": "red"},
        ],
        "Directory",
        "Teacher List",
        ["ID", "Name", "Subject", "Status"],
        [
            ["T01", "Dr. Meera Shah", "Database", "Active"],
            ["T02", "Prof. Arjun Mehta", "Python", "Active"],
            ["T03", "Neha Verma", "Networking", "On Leave"],
            ["T04", "Karan Joshi", "Mathematics", "Active"],
        ],
    )
    return render(request, "accounts/dashboard_section.html", context)


@login_required
def courses_page(request):
    context = dashboard_section_context(
        request,
        "courses",
        "Courses",
        "Academics",
        "Search courses",
        [
            {"label": "Total Courses", "value": "35", "icon": "fa-solid fa-book-open", "color": "blue"},
            {"label": "Running", "value": "28", "icon": "fa-solid fa-play", "color": "green"},
            {"label": "Drafts", "value": "5", "icon": "fa-solid fa-pen", "color": "orange"},
            {"label": "Archived", "value": "2", "icon": "fa-solid fa-box-archive", "color": "red"},
        ],
        "Catalog",
        "Course List",
        ["Code", "Course", "Faculty", "Status"],
        [
            ["CSE101", "Database Lab", "Dr. Meera Shah", "Running"],
            ["CSE204", "Django Project", "Prof. Arjun Mehta", "Running"],
            ["IT118", "Networking", "Neha Verma", "Draft"],
            ["MTH210", "Applied Mathematics", "Karan Joshi", "Running"],
        ],
    )
    return render(request, "accounts/dashboard_section.html", context)


@login_required
def reports_page(request):
    context = dashboard_section_context(
        request,
        "reports",
        "Reports",
        "Insights",
        "Search reports",
        [
            {"label": "Attendance", "value": "96%", "icon": "fa-solid fa-chart-simple", "color": "blue"},
            {"label": "Pass Rate", "value": "88%", "icon": "fa-solid fa-ranking-star", "color": "green"},
            {"label": "Pending Fees", "value": "14", "icon": "fa-solid fa-receipt", "color": "orange"},
            {"label": "Alerts", "value": "5", "icon": "fa-solid fa-triangle-exclamation", "color": "red"},
        ],
        "Reports",
        "Recent Reports",
        ["Report", "Owner", "Updated", "Status"],
        [
            ["Attendance Summary", "Admin", "Today", "Ready"],
            ["Branch Performance", "Academic", "Yesterday", "Ready"],
            ["Fee Pending List", "Accounts", "2 days ago", "Review"],
            ["Placement Report", "Training", "Last week", "Ready"],
        ],
    )
    return render(request, "accounts/dashboard_section.html", context)


@login_required
def settings_page(request):
    context = dashboard_section_context(
        request,
        "settings",
        "Settings",
        "Preferences",
        "Search settings",
        [
            {"label": "Role", "value": "Admin", "icon": "fa-solid fa-user-shield", "color": "blue"},
            {"label": "Theme", "value": "Auto", "icon": "fa-solid fa-palette", "color": "green"},
            {"label": "Alerts", "value": "On", "icon": "fa-solid fa-bell", "color": "orange"},
            {"label": "Security", "value": "Good", "icon": "fa-solid fa-lock", "color": "red"},
        ],
        "System",
        "Settings Overview",
        ["Setting", "Current Value", "Area", "Status"],
        [
            ["Profile", request.user.username, "Account", "Active"],
            ["Email", request.user.email or "Not set", "Account", "Optional"],
            ["Notifications", "Enabled", "System", "Active"],
            ["Dashboard Theme", "Toggle available", "Display", "Active"],
        ],
    )
    return render(request, "accounts/dashboard_section.html", context)
# -----------------------------
# Profile
# -----------------------------
@login_required
def profile(request):

    return render(
        request,
        "accounts/profile.html",
        {
            "active_page": "profile",
        }
    )
from django.shortcuts import render, redirect

def home(request):
    return redirect("login")
@login_required
def add_student(request):

    if request.method == "POST":

        form = StudentForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Student Added Successfully!"
            )

            return redirect("students_page")

    else:

        form = StudentForm()

    return render(
        request,
        "accounts/add_student.html",
        {
            "form": form
        }
    )