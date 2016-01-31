from rest_framework import serializers
from api.models.branch import Branch
from api.models.location import Location
from api.serializers.locationserializer import LocationSerializer


class BranchSerializer(serializers.ModelSerializer):
    location = LocationSerializer(default=True)
    id = serializers.IntegerField(required=False, read_only=False)
    class Meta:
        model = Branch
        fields = (
            'id',
            'contact_person',
            'address',
            'phone_no',
            'landmark',
            'location'
        )
        # extra_kwargs = {
        #     "id": {
        #         "read_only": False,
        #         "required": False,
        #     },
        # }

    def create(self, validated_data):
        print(validated_data)
        company = self.context.get("company")
        location = validated_data.pop('location')
        l = Location.objects.get(name= location['name'])
        branch = Branch.objects.create(location=l, company=company, **validated_data)
        return branch

    def update(self, instance, validated_data):
        instance.contact_person = validated_data['contact_person']
        instance.address = validated_data['address']
        instance.phone_no = validated_data['phone_no']
        instance.landmark = validated_data['landmark']
        location = validated_data.pop('location')
        instance.location = Location.objects.get(name= location['name'])
        instance.save()
        return instance