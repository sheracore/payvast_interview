from rest_framework import serializers


class GoodSerializer(serializers.Serializer):
    # id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=50)
    price = serializers.IntegerField(required=False)
    weight = serializers.IntegerField()
    size = serializers.IntegerField()

    class Meta:
        fields = ('title', 'price', 'weight', 'size')
