from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

from ..models.profile import Profile
from ..serializers import ProfileSerializer

# Create your views here.
class Profiles(generics.ListCreateAPIView):
    
    permission_classes=(IsAuthenticated,)

    serializer_class = ProfileSerializer
    def get(self, request):
        """Index request"""
        # Get all the profiles:
        # shows = Profile.objects.all()
        # Filter the shows by owner, so you can only see your owned mangos
        profiles = Profile.objects.filter(owner=request.user.id)
        # Run the data through the serializer
        data = ProfileSerializer(profiles, many=True).data
        return Response({ 'profiles': data })

    def post(self, request):
        """Create request"""
        # Add user to request data object
        request.data['owner'] = request.user.id
        # Serialize/create show, modified to accommodate array
        profile = ProfileSerializer(data=request.data)
        # If the show data is valid according to our serializer...
        if profile.is_valid():
            # save the created show & send a response
            profile.save()
            return Response({ 'profile': profile.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(profile.errors, status=status.HTTP_400_BAD_REQUEST)

# class MangoDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes=(IsAuthenticated,)
#     def get(self, request, pk):
#         """Show request"""
#         # Locate the mango to show
#         mango = get_object_or_404(Mango, pk=pk)
#         # Only want to show owned mangos?
#         if request.user != mango.owner:
#             raise PermissionDenied('Unauthorized, you do not own this mango')

#         # Run the data through the serializer so it's formatted
#         data = MangoSerializer(mango).data
#         return Response({ 'mango': data })

#     def delete(self, request, pk):
#         """Delete request"""
#         # Locate mango to delete
#         mango = get_object_or_404(Mango, pk=pk)
#         # Check the mango's owner against the user making this request
#         if request.user != mango.owner:
#             raise PermissionDenied('Unauthorized, you do not own this mango')
#         # Only delete if the user owns the  mango
#         mango.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#     def partial_update(self, request, pk):
#         """Update Request"""
#         # Locate Mango
#         # get_object_or_404 returns a object representation of our Mango
#         mango = get_object_or_404(Mango, pk=pk)
#         # Check the mango's owner against the user making this request
#         if request.user != mango.owner:
#             raise PermissionDenied('Unauthorized, you do not own this mango')

#         # Ensure the owner field is set to the current user's ID
#         request.data['mango']['owner'] = request.user.id
#         # Validate updates with serializer
#         data = MangoSerializer(mango, data=request.data['mango'], partial=True)
#         if data.is_valid():
#             # Save & send a 204 no content
#             data.save()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         # If the data is not valid, return a response with the errors
#         return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
