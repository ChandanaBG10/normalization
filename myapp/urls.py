from django.urls import path

from .views import *


urlpatterns = [

    # Frontend Pages
    path('', upload_page),

    path('dashboard/', dashboard_page),

    path('review/', review_page),

    path('approve-page/<int:id>/', approve_page),

    path('reject-page/<int:id>/', reject_page),

    # APIs
    path('api/upload/sap/', upload_sap),

    path('api/upload/utility/', upload_utility),

    path('api/upload/travel/', upload_travel),

    path('api/records/', get_records),

    path('api/approve/<int:id>/', approve_record),

    path('api/reject/<int:id>/', reject_record),
]