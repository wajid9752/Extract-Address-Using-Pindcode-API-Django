from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from .models import Account
import requests
# Create your views here.




@api_view(['GET'])
def fetch_account(request):
    
    get_data = json.loads(request.body)
    print(get_data)
    request_user_id = get_data['user_id']
    hit_url=f"https://api.postalpincode.in/pincode/{request_user_id}"
    
    response = requests.get(hit_url)
    get_data=response.text

    get_Pst = json.loads(get_data)

    


    context={
        "status": "success",
        "code": 200,
        "data":{
            "data": get_Pst
        }
    }
    return Response(context)