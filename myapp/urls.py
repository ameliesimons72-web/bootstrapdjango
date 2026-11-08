from django.urls import path
from django.views.generic import TemplateView

from myapp import views


urlpatterns = [
    path('', views.home, name='home'),
    path('tables-basic/', TemplateView.as_view(
        template_name='myapp/spark_admin/tables-basic.html',
    ), name='tables_basic'),
    path('ui-forms/', TemplateView.as_view(
        template_name='myapp/spark_admin/ui-forms.html',
    ), name='ui_forms'),
    path('ui-buttons/', TemplateView.as_view(
        template_name='myapp/spark_admin/ui-buttons.html',
    ), name='ui_buttons'),
    path('page-blank/', TemplateView.as_view(
        template_name='myapp/spark_admin/page-blank.html',
    ), name='page_blank'),
    path('page-login/', TemplateView.as_view(
        template_name='myapp/spark_admin/page-login.html',
    ), name='page_login'),
    path('page-404/', TemplateView.as_view(
        template_name='myapp/spark_admin/page-404.html',
    ), name='page_404'),
]
    