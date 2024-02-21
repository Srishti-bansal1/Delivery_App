from django.shortcuts import render
from rest_framework import viewsets ,status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response 

# Create your views here.
from .models import Organization , Item, Pricing, SignUpModel
from .serializers import OrganizationSerializer , ItemSerializer , PricingSerializer, SignupSerializer, LoginSerializer

from rest_framework_simplejwt.tokens import RefreshToken

class SignupViewSet(viewsets.ModelViewSet):
    queryset = SignUpModel.objects.all()
    serializer_class = SignupSerializer

    @action(detail=False, methods=["GET"],url_path='show_user')
    def get_user(self , request):
        queryset = SignUpModel.objects.all()
        if queryset:
            serializer = SignupSerializer(queryset,many = True)
            return Response(serializer.data)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=["POST"],url_path='create_user')
    def add_org(self, request):
        dataReceived = request.data  

        serializer = SignupSerializer(data = dataReceived )
        
        if SignUpModel.objects.filter(**dataReceived).exists():
            raise Exception("Duplicate Data")

        if serializer.is_valid():           
            serializer.save()
            serializer_data = serializer.data
            return Response(serializer_data)
        else:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @action(detail=True , methods=['PUT'],url_path='modify_user')
    def update_user(self,request,pk=None):
        queryset = SignUpModel.objects.get(pk=pk)
        serializer = SignupSerializer(instance = queryset, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        
    @action(detail=True , methods=['DELETE'],url_path='delete_user')
    def remove_user(self,request,pk=None):
        queryset = SignUpModel.objects.get(pk=pk)  
        queryset.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    
class LoginVeiwSet(viewsets.ModelViewSet):

    @action(detail=False, methods=["GET"],url_path='user_access')
    def users_access(self , request):
        _email = request.GET.get('email')
        _password = request.GET.get('password')

        queryset = SignUpModel.objects.get(email = _email)
        if queryset:
            serializer = LoginSerializer(queryset)
        else:
            return Response({'message':'check detail again'}, status= status.HTTP_205_RESET_CONTENT)
        Password = serializer.data.get('password')
        if Password == _password:
            _refresh = RefreshToken()
            token = _refresh.for_user(queryset)
            return Response({"refresh": str(token), "access": str(token.access_token)}) 
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    @action(detail=False , methods=['PATCH'],url_path='update')
    def updated(self,request):
        Email = request.GET.get('email')
        print(Email)
        new_password = request.GET.get('password')
        print(new_password)
        
        queryset = SignUpModel.objects.get(email = Email)
        print(queryset)
        if not queryset:
            return Response({'message' :'Unable to get account.'},status=status.HTTP_404_NOT_FOUND)
        
        serializer = SignupSerializer(queryset)
        serializer_data = serializer.data
        serializer_data["password"] = new_password
        serializer = SignupSerializer(instance = queryset,data= serializer_data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_304_NOT_MODIFIED)
    


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
    

@api_view(['GET'])   
def SignUp(request):
    return render(request,'signup.html', {'signUp': SignUp})

@api_view(['GET'])   
def Login(request):
    return render(request,'login.html', {'login': Login})

@api_view(['GET'])   
def Reset(request):
    return render(request,'reset.html', {'reset': Reset})
