from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('role/', RoleView.as_view(), name='role'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('admin-only/', AdminOnlyView.as_view(), name='admin_only'),
    path('teacher-only/', TeacherOnlyView.as_view(), name='teacher_only'),
    path('student/', StudentOnlyView.as_view(), name='student_only'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
