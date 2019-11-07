from rest_framework.viewsets import ModelViewSet

from .models import Link
from .serializers import LinkSerializer


class LinkViewSet(ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
