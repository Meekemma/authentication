from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from .serializers import RegisterSerializer,changePasswordSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


# Custom serializer for obtaining JWT token with additional claims
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class =MyTokenObtainPairSerializer   


@api_view(['POST'])
def registerUsers(request):
    """
    API endpoint to register users.
    """
    if request.method == 'POST':
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def changePasswordView(request):
    """
    API endpoint to change the password of the authenticated user.
    """
    if request.method == 'PUT':
        serializer=changePasswordSerializer(data=request.data, context={'user':request.user})
        if serializer.is_valid():
            return Response({'detail': 'password changed successfully'}, status=status.HTTP_200_OK)
        return Response({"error": "Failed to changed password", "details": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    



@api_view(['GET'])
@permission_classes([IsAdminUser])
def UserList(request):
    """
    API endpoint to get a list of all users (admin access required).
    """
    users=User.objects.all()
    serializer=RegisterSerializer(users, many=True)
    return Response(serializer.data)





@api_view(['PUT', 'DELETE'])
@permission_classes([IsAdminUser])
def UserDetail(request, pk):
    """
    API endpoint to update or delete a user by their ID (admin access required).
    """
    try:
        user = User.objects.get(id=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = RegisterSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "User successfully updated"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response({"detail": "User successfully deleted"}, status=status.HTTP_204_NO_CONTENT)
