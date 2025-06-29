from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import obtain_auth_token  # Optional, for direct login view

@api_view(['GET'])
def public_api(request):  # 🔧 Fixed name from public_view to public_api
    return Response({"message": "This is a public API endpoint."})

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def protected_view(request):
    return Response({"message": f"Hello, {request.user.username}. You are authenticated."})
