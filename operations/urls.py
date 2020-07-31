from django.urls import path
from . import views

urlpatterns = [
    path("",views.emp_form,name="form"),
    path("<int:id>/",views.emp_form,name="update_employee"),
    path("list/",views.emp_list,name="list"),
    path("delete/<int:id>/",views.emp_delete,name="del")
]
