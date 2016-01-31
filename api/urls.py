from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'WorkIndiaFriendsApi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^test/', 'api.views.test_api', name='test'),

    url(r'^companies/(?P<pk>[0-9]+$)', 'api.controllers.companyController.company_detail', name='company_detail'),
    url(r'^companies/$', 'api.controllers.companyController.company_list', name='company_list'),

    url(r'^companies/(?P<companyId>[0-9]+)/branches/(?P<branchId>[0-9]+$)', 'api.controllers.branchController.branch_detail', name='branch_detail'),
    url(r'^companies/(?P<companyId>[0-9]+)/branches/$', 'api.controllers.branchController.branch_list', name='branch_list'),
    
    url(r'^locations/(?P<pk>[0-9]+$)', 'api.controllers.locationController.location_detail', name='location_detail'),
    url(r'^locations/$', 'api.controllers.locationController.location_list', name='location_list'),
    
    url(r'^sectors/(?P<pk>[0-9]+$)', 'api.controllers.sectorController.sector_detail', name='sector_detail'),
    url(r'^sectors/$', 'api.controllers.sectorController.sector_list', name='sector_list'),

    url(r'^jobs/(?P<pk>[0-9]+$)', 'api.controllers.jobController.job_detail', name='job_detail'),
    url(r'^jobs/$', 'api.controllers.jobController.job_list', name='job_list'),

    #url(r'^mobile/jobs/(?P<pk>[0-9]+$)', 'api.controllers.jobController.job_detail', name='job_detail'),
    url(r'^mobile/jobs/$', 'api.controllers.jobListMobileController.job_list', name='job_list'),
]