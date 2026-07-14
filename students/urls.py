from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Student Management"
admin.site.site_title = "SMS Admin"
admin.site.index_title = "Admin Panel Overview"

urlpatterns = [

    path("admin/", admin.site.urls),

    path("", include("accounts.urls")),

]
