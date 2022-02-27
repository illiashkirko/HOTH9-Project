from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import FilterFoodSerializer
from .models import FilteredFood
from .backend import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render


# class FilterFoodView(viewsets.ModelViewSet):
#     serializer_class = FilterFoodSerializer
#     queryset = FilteredFood.objects.all()
#     # queryset[1] = {"hall": "deneve", "filters": "no eggs", "foods": "not eggs"}
#     print(queryset[0].hall)

# def index(request):
#     return HttpResponse(json.dumps(response_data), content_type="application/json")
class FilterFoodView(APIView):
    serializer_class = FilterFoodSerializer
  
    # def get(self, request):
    #     array = filteroptions([request.query_params["filter"]])
    #     print(request.data)
    #     print(request.query_params)
    #     return Response([{'filteredArray': array}]);
  
    def post(self, request):
        myinput = [request.data["filter"]]
        array = filteroptions(myinput)

        # serializer = FilterFoodSerializer(data=request.data)
        # if serializer.is_valid(raise_exception=True):
        #     serializer.save()
        return  Response([{'out': array}])