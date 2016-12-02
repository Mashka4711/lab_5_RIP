from django.conf.urls import url, include
from first_test.views import home,CompaniesView,CompanyView
from django.contrib import admin

urlpatterns = [
    url(r'^admin', admin.site.urls),
    url(r'^$',home),
    url(r'^home$', home),
    url(r'^company/$',CompaniesView.as_view()),
    url(r'^company/(?P<id>\d+)$',CompanyView.as_view(),name='company_url')
]