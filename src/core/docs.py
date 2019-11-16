from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser


SchemaView = get_schema_view(
   openapi.Info(title='Link To API', default_version='v1'),
   public=True,
   authentication_classes=(SessionAuthentication,),
   permission_classes=(IsAdminUser,),
)
