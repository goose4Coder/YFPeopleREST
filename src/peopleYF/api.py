from rest_framework import routers
from members import api_views
router = routers.DefaultRouter()
router.register(r'tags', api_views.MemberTagViewset)
router.register(r'members', api_views.MemberViewset)
router.register(r'clubs', api_views.ClubViewset)