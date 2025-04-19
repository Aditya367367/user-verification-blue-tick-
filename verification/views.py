from django.core.mail import send_mail
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from .models import Verification
from .serializers import VerificationSerializer


class VerificationView(APIView):
    def post(self, request):
        serializer = VerificationSerializer(data=request.data)
        if serializer.is_valid():
            verification = serializer.save()

            # Send a dummy email (prints to console)
            send_mail(
                subject="New Verification Submission",
                message=f"A new verification form has been submitted by {verification.email}.\n\n"
                        f"Details:\n"
                        f"Type: {verification.type}\n"
                        f"Document Type: {verification.doc_type}\n"
                        f"Document Number: {verification.doc_number}\n"
                        f"Status: Pending\n\n"
                        f"Please review the submission in the admin panel.",
                from_email="no-reply@example.com",
                recipient_list=["backend-team@example.com"],#add emails and all credentials in setting
                fail_silently=False,
            )

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print("Validation Errors:", serializer.errors)  
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerificationStatusView(APIView):
    def get(self, request):
        user_email = request.query_params.get('email')
        if not user_email:
            return Response({"error": "Email parameter is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            verification = Verification.objects.get(email=user_email)
            return Response({"status": verification.status}, status=status.HTTP_200_OK)
        except Verification.DoesNotExist:
            return Response({"error": "Verification record not found."}, status=status.HTTP_404_NOT_FOUND)


class UpdateVerificationStatusView(APIView):
    def post(self, request):
        email = request.data.get("email")
        status_value = request.data.get("status")

        if status_value not in [0, 1]: 
            return Response({"error": "Invalid status value."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            verification = Verification.objects.get(email=email)
            verification.status = status_value
            verification.save()
            return Response({"message": "Verification status updated successfully."}, status=status.HTTP_200_OK)
        except Verification.DoesNotExist:
            return Response({"error": "Verification record not found."}, status=status.HTTP_404_NOT_FOUND)