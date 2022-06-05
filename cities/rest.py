from rest_framework.viewsets import ModelViewSet
from rest_framework import serializers

from cities.models import City


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"


class CityViewSet(ModelViewSet):
    model = City
    serializer_class = CitySerializer

    def get_queryset(self):
        states = self.request.query_params.get("states")
        print(states)
        if states:
            return City.objects.filter(state_id__in=states.split(","))
        return City.objects.all().order_by("id")
