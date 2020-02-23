from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response


# Create your views here.
@api_view(["GET"])
def generate_tree(request):
    try:
        return Response(status=status.HTTP_200_OK, data={"message": "Demo API", "success": True})
    except Exception as e:
        return Response(status=status.HTTP_404_NOT_FOUND, data={"message": str(e), "success": False})
