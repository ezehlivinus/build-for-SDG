from django.urls import path, include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls

from .api_views import *

router = DefaultRouter()
router = DefaultRouter(trailing_slash=False)


# router.register(r'on-covid-19/'f'{sufix}/', estimation, basename='on-covid-19')


schema_view = get_swagger_view(title='Covid19 API Estimator')

sufix = 'json'
urlpatterns = [
    # url(r'', include(router.urls)),
    path(r'on-covid-19/'f'{sufix}', EstimationList.as_view(), name='estimation'),
    path('docs/', include_docs_urls(title='Bookkeeping API')),
    path('swagger-docs/', schema_view),
]