"""
URL configuration for careerjunctionmain project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
   
        path('',login_page,name='login_page'),
        path('login_view/',login_view,name='login_view'),
        path('admin_home/',admin_home,name='admin_home'),
        path('officer_home/',officer_home,name='officer_home'),
        path('logout_view/',logout_view,name='logout_view'),
        path('add_officer/',add_officer,name='add_officer'),
        path('view_officer/',view_officer,name='view_officer'),
        path('view_case/',view_case,name='view_case'),
        path('delete_case/<int:id>',delete_case,name='delete_case'),
        path('case_search/',case_search,name='case_search'),
        path('add_case/',add_case,name='add_case'),
        path('assign_case/',assign_case,name='assign_case'),
        path('view_assigned_case/',view_assigned_case,name='view_assigned_case'),
        path('add_case_details/<int:case_id>',add_case_details,name='add_case_details'),
        path('create_person_info/',create_person_info,name='create_person_info'),
        path('edit_assigned_case_get/',edit_assigned_case_get,name='edit_assigned_case_get'),
        path('add_case_info/<int:case_id>',add_case_info,name='add_case_info'),
        path('update_case_info/<int:id>',update_case_info,name='update_case_info'),
        path('device_create/<int:id>',device_create,name='device_create'),
        path('device_list_case/<int:case_id>',device_list_case,name='device_list_case'),
        path('device_delete/<int:pk>',device_delete,name='device_delete'),
        path('device_update/<int:case_id>',device_update,name='device_update'),
        path('case_all_list/',case_all_list,name='case_all_list'),
        path('view_case_detail/<int:case_id>',view_case_detail,name='view_case_detail'),
        path('chatbot/',chatbot,name='chatbot'),
        path('chatbot1/',chatbot1,name='chatbot1'),
        path('chatbot_view1/',chatbot_view1,name='chatbot_view1'),
        path('chatbot_view/',chatbot_view,name='chatbot_view'),
        path('pdfChatUpload/',pdfChatUpload,name='pdfChatUpload'),
        path('update_person_info/<int:case_id>',update_person_info,name='update_person_info'),
        path('edit_assigned_case/<int:id>',edit_assigned_case,name='edit_assigned_case'),
        #path('update_assign_case/',update_assign_case,name='update_assign_case'),
        path('delete-user/<int:user_id>/', delete_user, name='delete-user'),
        path('file_list/<int:id>', file_list, name='file_list'),
        path('upload_file/<int:id>', upload_file, name='upload_file'),
        path('evidence_edit/<int:id>', evidence_edit, name='evidence_edit'),
        path('delete_file/', delete_file, name='delete_file'),
        path('case_close/<int:id>', case_close, name='case_close'),
        path('case_open/<int:id>', case_open, name='case_open'),
        path('date_wise_case_chart_data/', date_wise_case_chart_data, name='date_wise_case_chart_data'),
        path('case_distribution_by_type/', case_distribution_by_type, name='case_distribution_by_type'),
        path('case_assignment_chart_data/', case_assignment_chart_data, name='case_assignment_chart_data'),
        path('person_info_completion_chart_data/', person_info_completion_chart_data, name='person_info_completion_chart_data'),
        path('case_status_breakdown_chart_data/', case_status_breakdown_chart_data, name='case_status_breakdown_chart_data'),
        path('case_distribution_by_type_chart_data/', case_distribution_by_type_chart_data, name='case_distribution_by_type_chart_data'),
        path('case_status_breakdown/', case_status_breakdown, name='case_status_breakdown'),
        path('case_open_by_admin/<int:id>', case_open_by_admin, name='case_open_by_admin'),
        path('case_close_by_admin/<int:id>', case_close_by_admin, name='case_close_by_admin'),

]
