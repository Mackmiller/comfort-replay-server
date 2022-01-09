from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import generics

class RegisterData(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    parser_classes = (FormParser, MultiPartParser)

    def post(self, request):
        for file in request.FILES.values():
            print(file)

        return Response({"success": "Good job, buddy"})