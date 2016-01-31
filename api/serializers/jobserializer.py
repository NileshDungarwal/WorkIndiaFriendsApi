from rest_framework import serializers
from api.models.job import Job
from api.models.sector import Sector
from api.models.branch import Branch
from api.models.jobbranches import JobBranches
from api.serializers.branchserializer import BranchSerializer
from api.serializers.sectorserializer import SectorSerializer
from api.serializers.jobbranchesserializer import JobBranchesSerializer


class JobSerializer(serializers.ModelSerializer):
    branches = JobBranchesSerializer(many=True)
    sector = SectorSerializer(default=True)

    class Meta:
        model = Job
        fields = (
            'id',
            'designation',
            'min_salary',
            'max_salary',
            'shift_timing',
            'branches',
            'sector'
        )

    def create(self, validated_data):
        print(validated_data)
        branches = validated_data.pop('branches')
        print("reached")
        sector = validated_data.pop('sector')
        s = Sector.objects.get(name=sector['name'])
        print(s.name)
        j = Job.objects.create(sector=s,**validated_data)
        for branch in branches:
            b = Branch.objects.get(id=branch['id'])
            jobBranches = JobBranches.objects.create(job=j,branch=b)
            jobBranches.save()
        return j

    def update(self, instance, validated_data):
        instance.designation = validated_data['designation']
        sector = validated_data.pop('sector')
        instance.sector = Sector.objects.get(name= sector['name'])
        branches = validated_data.pop('branches')
        instance.branches.clear()
        branch_ids = [branch['id'] for branch in branches]
        for branch in instance.branches:
            if branch.id not in branch_ids:
                branch.delete() # remove
        instance_branch_ids = [branch['id'] for branch in instance.branches]
        for branch in branches:
            if branch.id not in instance_branch_ids:
                b = Branch.objects.get(id=branch.id)
                instance.branches.add(b) # add
        instance.save()
        return instance


        # for branch in branches:
        #     if branch['id'] not in instance.branches.keys:
        #         b = Branch.objects.get(id=branch['id'])
        #         instance.branches.add(b)
        #     job.save()
        instance.save()
        return instance
