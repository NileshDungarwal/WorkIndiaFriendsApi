from rest_framework import serializers
from api.models.jobbranches import JobBranches
from api.models.sector import Sector
from api.models.branch import Branch
from api.serializers.branchserializer import BranchSerializer
from api.serializers.sectorserializer import SectorSerializer


class JobMobileSerializer(serializers.ModelSerializer):
    company_name = serializers.StringRelatedField(read_only=True,source="branch.company.name")
    job_sector = serializers.StringRelatedField(read_only=True,source="job.sector.name")
    min_salary = serializers.StringRelatedField(read_only=True,source="job.min_salary")
    max_salary = serializers.StringRelatedField(read_only=True,source="job.max_salary")
    location = serializers.StringRelatedField(read_only=True,source="branch.location.name")
    landmark = serializers.StringRelatedField(read_only=True,source="branch.landmark")
    # branches = BranchSerializer(many=True, read_only=True)
    # sector = SectorSerializer(default=True, read_only=True)

    class Meta:
        model = JobBranches
        fields = (
            'id',
            'company_name',
            'job_sector',
            'min_salary',
            'max_salary',
            'location',
            'landmark',
        )