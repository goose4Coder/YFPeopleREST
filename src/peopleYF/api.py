from rest_framework import routers
from members import api_views
router = routers.DefaultRouter()
router.register(r'tags', api_views.MemberTagViewset)