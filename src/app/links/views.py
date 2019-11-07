from rest_framework.viewsets import ModelViewSet

from .models import Link
from .serializers import LinkSerializer


class LinkViewSet(ModelViewSet):
    queryset = Link.objects.order_by('id')
    serializer_class = LinkSerializer
