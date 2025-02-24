import requests
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from config import settings
from models.models import UserData
from .serializers import WebHookSerializer


class HandleWebhookAPIView(APIView):
    def post(self, request):
        print('restart')
        serializer = WebHookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        sum = serializer.validated_data['sum']
        phone = serializer.validated_data['phone']
        userdata , created = UserData.objects.get_or_create(phone=phone)
        print(userdata.phone)
        print(userdata.telegram_id)
        userdata.last_balance = int(float(sum))
        userdata.save()
        if userdata.telegram_id:
            response = requests.post(
                url=f"https://api.telegram.org/bot{settings.BOT_TOKEN}/sendMessage",
                json={
                    "chat_id": userdata.telegram_id,
                    "text": f"Sizning LoftBurger dagi keshbekingiz {userdata.last_balance} so'mni tashkil etadi"
                }
            )
            print(response.status_code)
            print(response.text)
        return Response({
            "status" : response.status_code,
            'text' : response.text
        })
    
# Create your views here.
