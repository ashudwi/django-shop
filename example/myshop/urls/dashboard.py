# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url, include

from shop.dashboard.routers import DashboardRouter
from shop.dashboard.views import FileUploadView

from myshop.dashboard import ProductsViewSet, ProfileViewSet

router = DashboardRouter(trailing_slash=False, root_template_name='myshop/dashboard.html')
router.register('products', ProductsViewSet)
router.register('profile', ProfileViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^upload/$', FileUploadView.as_view(), name='fileupload')
]
