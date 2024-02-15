from django.shortcuts import render
from rest_framework import viewsets ,status
from rest_framework.decorators import action
from rest_framework.response import Response 

# Create your views here.
from .models import Organization , Item, Pricing
from .serializers import OrganizationSerializer , ItemSerializer , PricingSerializer

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
        
    @action(detail=False, methods=["GET"],url_path='show_org')
    def get_org(self , request):
        queryset = Organization.objects.all()
        if queryset:
            serializer = OrganizationSerializer(queryset,many = True)
            return Response(serializer.data)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=["POST"],url_path='create_org')
    def add_org(self, request):
        dataReceived = request.data  

        serializer = OrganizationSerializer(data = dataReceived )
        
        if Organization.objects.filter(**dataReceived).exists():
            raise Exception("Duplicate Data")

        if serializer.is_valid():           
            serializer.save()
            serializer_data = serializer.data
            return Response(serializer_data)
        else:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @action(detail=True , methods=['PUT'],url_path='modify_org')
    def update_org(self,request,pk=None):
        queryset = Organization.objects.get(pk=pk)
        serializer = OrganizationSerializer(instance = queryset, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        
    @action(detail=True , methods=['DELETE'],url_path='delete_org')
    def remove_org(self,request,pk=None):
        queryset = Organization.objects.get(pk=pk)  
        queryset.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    
    
    
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
        
    @action(detail=False, methods=["GET"],url_path='show_item')
    def get_item(self , request):
        queryset = Item.objects.all()
        if queryset:
            serializer = ItemSerializer(queryset,many = True)
            return Response(serializer.data)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=["POST"],url_path='create_item')
    def add_item(self, request):
        dataReceived = request.data  

        serializer = ItemSerializer(data = dataReceived )
        
        if Item.objects.filter(**dataReceived).exists():
            raise Exception("Duplicate Data")

        if serializer.is_valid():           
            serializer.save()
            serializer_data = serializer.data
            return Response(serializer_data)
        else:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @action(detail=True , methods=['PUT'],url_path='modify_item')
    def update_item(self,request,pk=None):
        queryset = Item.objects.get(pk=pk)
        serializer = ItemSerializer(instance = queryset, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        
    @action(detail=True , methods=['DELETE'],url_path='delete_item')
    def remove_item(self,request,pk=None):
        queryset = Item.objects.get(pk=pk)  
        queryset.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    
    
    
    
class PricingViewSet(viewsets.ModelViewSet):
    queryset = Pricing.objects.all()
    serializer_class = PricingSerializer
        
    @action(detail=False, methods=["GET"],url_path='show_price')
    def get_price(self , request):
        queryset = Pricing.objects.all()
        if queryset:
            serializer = PricingSerializer(queryset,many = True)
            return Response(serializer.data)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=["POST"],url_path='create_price')
    def Add_price(self, request):
        dataReceived = request.data  

        serializer = PricingSerializer(data = dataReceived )
        
        if Pricing.objects.filter(**dataReceived).exists():
            raise Exception("Duplicate Data")

        if serializer.is_valid():           
            serializer.save()
            serializer_data = serializer.data
            return Response(serializer_data)
        else:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @action(detail=True , methods=['PUT'],url_path='modify_price')
    def update_price(self,request,pk=None):
        queryset = Pricing.objects.get(pk=pk)
        serializer = PricingSerializer(instance = queryset, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        
    @action(detail=True , methods=['DELETE'],url_path='delete_price')
    def remove_price(self,request,pk=None):
        queryset = Pricing.objects.get(pk=pk)  
        queryset.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    
    
class TotalPrice(viewsets.ModelViewSet):
        
    @action(detail=False, methods=["GET"],url_path='total_price')
    def calculate_price(self,request):
        print(request)
        distance = request.GET.get('total_distance')
        Zone = request.GET.get('zone')
        Organization_id = request.GET.get('organization')
        Item_Id = request.GET.get('item_id')
        
        queryset = Pricing.objects.get(organization = Organization_id , item_id = Item_Id  , zone = Zone)
        print(queryset)
        if queryset:
            serializer = PricingSerializer(queryset)
            base_distance = serializer.data.get('base_distance_in_km')
            _km_price = serializer.data.get('km_price')
            _fix_price = serializer.data.get('fix_price')
            print(_fix_price)
            
            calculation = _fix_price + (int(distance) - base_distance)*(_km_price)
            return Response({'total_price': calculation })
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)