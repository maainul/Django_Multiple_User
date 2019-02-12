from django.urls import include, path
# from django.contrib import admin
from useraccount.views import useraccount, hr_department, fin_department

urlpatterns = [
    # path('admin/', admin.site.urls),
    #path('', include('classroom.urls')),
    path('', include('useraccount.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', useraccount.SignUpView.as_view(), name='signup'),
    path('accounts/signup/hr_department/', hr_department.HRDepartmentSignUpView.as_view(), name='student_signup'),
    path('accounts/signup/fin_department/', fin_department.FinanceDepartmentSignUpView.as_view(), name='teacher_signup'),
]

