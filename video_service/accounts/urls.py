
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name='accounts'

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name='accounts/login.html'),name="login"),
    path('logout/',auth_views.LogoutView.as_view(),name="logout"),
    path('signup/',views.registerPage.as_view(),name="signup"),
    path('student/', views.StudentSignUpView.as_view(), name='student_signup'),
    path('teacher/', views.TeacherSignUpView.as_view(), name='teacher_signup'),

   
    
    
     

]

