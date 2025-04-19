from django.urls import path
from .views import VerificationView, VerificationStatusView, UpdateVerificationStatusView

urlpatterns = [
    path('verification/', VerificationView.as_view(), name='verification'),
    path('verification-status/', VerificationStatusView.as_view(), name='verification-status'),
    path('update-verification-status/', UpdateVerificationStatusView.as_view(), name='update-verification-status'),
]