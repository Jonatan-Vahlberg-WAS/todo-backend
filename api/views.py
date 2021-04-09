
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import ListSerializer, TaskSerializer, MyListSerializer
from .models import List, Task
# Create your views here.
class ListViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = List.objects.all().order_by("title")
    serializer_class = MyListSerializer