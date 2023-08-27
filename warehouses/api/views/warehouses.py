from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from django.db.models import QuerySet
from rest_framework.exceptions import ValidationError
from ..serializers import WarehouseSerializer

from ...models import Warehouse


class WarehouseViewSet(GenericViewSet):
    queryset = QuerySet().none()
    serializer_class = WarehouseSerializer

    def create(self, request):
        data = request.data
        if not data:
            raise ValidationError({"data": "should include body"})
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        result = Warehouse(Warehouse.__name__).insert(**data)
        return Response(result, status=status.HTTP_201_CREATED)

    def list(self):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def retrieve(self, request, pk=None):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, pk=None):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, pk=None):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, pk=None):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)