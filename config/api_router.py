from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from jobzill.applications.baseuser.api.views import CreateUserView

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

# router.register("createuser", CreateUserView)

app_name = "api"
urlpatterns = router.urls
