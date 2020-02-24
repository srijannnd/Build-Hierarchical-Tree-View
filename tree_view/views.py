from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from tree_view import helpers
from tree_view.db import database
from django.shortcuts import render
import json


# Tree View API
@api_view(["GET"])
def generate_tree(request):
    try:
        company = request.GET.get("company", "")
        company_obj = database["companies"].find_one({"alias": company})
        result = helpers.generate_tree(company_obj["capabilities"])
        return Response(status=status.HTTP_200_OK, data={"data": result, "success": True})
    except Exception as e:
        return Response(status=status.HTTP_404_NOT_FOUND, data={"message": str(e), "success": False})


# Tree View Template
def generate_tree_view(request, company):
    try:
        company_obj = database["companies"].find_one({"alias": company})
        result = helpers.generate_tree(company_obj["capabilities"])
        return render(request, 'index.html', {"result": json.dumps(result)})
    except Exception as e:
        return Response(status=status.HTTP_404_NOT_FOUND, data={"message": str(e), "success": False})
