from rest_framework import serializers
from api.models.job import Job
from api.models.sector import Sector
from api.models.branch import Branch
from api.models.jobbranches import JobBranches
from api.serializers.branchserializer import BranchSerializer
from api.serializers.sectorserializer import SectorSerializer


class JobBranchesSerializer(serializers.ModelSerializer):
    branch = BranchSerializer(default=True)
    id = serializers.IntegerField(required=False, read_only=False)

    class Meta:
        model = Job
        fields = (
            'id',
            'branch',
        )