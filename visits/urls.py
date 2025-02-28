from django.urls import path
from . import views

urlpatterns = [

    path('visits', views.visits, name="visits"),
    path('visit/edit/<int:visit_id>/', views.visit_edit, name="visit_edit"),
    path('visit/edit/add', views.visit_add, name="visit_add"),
    path('visit/edit/change', views.visits, name="visit_change"),
    path('visit/edit/delete/<int:visit_id>/', views.delete_visit, name="visit_delete"),
    path('visit/view/<int:visit_id>/', views.view_visit, name="view_visit"),
    path('generate-prescription/<int:visit_id>/', views.generate_prescription_pdf, name="generate-prescription"),

]