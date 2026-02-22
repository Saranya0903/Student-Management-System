from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
#authentication
path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
path('logout/', views.logout_user, name='logout'),

# Dashboard
path('', views.dashboard, name='dashboard'),

# Student URLs
# Students
path('students/', views.student_list, name='student_list'),
path('students/add/', views.add_student, name='add_student'),
path('students/<int:id>/', views.student_detail, name='student_detail'),
path('students/update/<int:id>/', views.update_student, name='update_student'),
path('students/delete/<int:id>/', views.delete_student, name='delete_student'),

# Achievement URLs
    path('achievements/add/<int:student_id>/', views.add_achievement, name='add_achievement'),
    path('achievements/update/<int:id>/', views.update_achievement, name='update_achievement'),
    path('achievements/delete/<int:id>/', views.delete_achievement, name='delete_achievement'),
    path('achievements/pending/', views.pending_achievements, name='pending_achievements'),
]