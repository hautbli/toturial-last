from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from cards.models import Card
from cards.serializers import CardSerializer
from cards.permissions import IsOwner


class CardViewSet(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def get_permissions(self):
        if self.action == "create":
            return [AllowAny()]
        elif self.action in ["update" , "destroy"]:
            return [IsOwner()]
        return super().get_permissions() # 나머지는 부모에 잇는 메소드 기냥..