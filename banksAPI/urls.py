from django.urls import path
from banksAPI.views import bank_list, branch_list, ifsc_details

urlpatterns = [
    path('banks/', bank_list),
    path('branches/<str:bank_id>/', branch_list),
    path('ifsc/<str:ifsc_code>/', ifsc_details, name='ifsc-details'),
]
