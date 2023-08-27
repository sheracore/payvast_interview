from django.db.models import QuerySet

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.exceptions import ValidationError

from ..serializers import GoodSerializer
from ...models import Good


class GoodViewSet(GenericViewSet):
    queryset = QuerySet().none()
    serializer_class = GoodSerializer

    def create(self, request):
        data = request.data
        if not data:
            raise ValidationError({"data": "should include body"})
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        result = Good(Good.__name__).insert(**data)
        return Response(result, status=status.HTTP_201_CREATED)

    def list(self, request):
        result = Good(Good.__name__).filter()
        return Response(result, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        result = Good(Good.__name__).filter(id=pk)
        return Response(result, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        try:
            Good(Good.__name__).delete(id=pk)
        except Exception:
            raise ValidationError({"pk": "given pk does not exists"})
        return Response(status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        return self._update(request, pk=pk)

    def update(self, request, pk=None):
        return self._update(request, pk=pk)

    def _update(self, request, pk=None):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        result = Good(Good.__name__).update(id=pk, **request.data)
        return Response(result, status=status.HTTP_200_OK)
