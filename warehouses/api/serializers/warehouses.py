from rest_framework import serializers


class WarehouseSerializer(serializers.Serializer):
    # id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=50)
    is_full = serializers.BooleanField(required=False)

    class Meta:
        fields = ('title', 'is_full')
