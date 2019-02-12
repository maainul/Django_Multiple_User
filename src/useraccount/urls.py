from django.urls import include, path

from .views import useraccount, hr_department, fin_department

urlpatterns = [
    path('', useraccount.home, name='home'),
    

    path('hr_department/', include(([

    path('', hr_department.hr_department_home, name='hr_department_home'),

    path('', hr_department.HRDepartmentSignUpView.as_view(), name='hr_department_home'),

    ], 'useraccount'), namespace='hr_department')),
    
    path('fin_department/', include(([

    path('', fin_department.fin_department_home, name='fin_department_home'),
    path('', fin_department.FinanceDepartmentSignUpView.as_view(), name='fin_department_home'),
    
    ], 'useraccount'), namespace='fin_department')),
]
