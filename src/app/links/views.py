from django.db.utils import IntegrityError

from rest_framework.generics import get_object_or_404
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from .models import Link
from .serializers import LinkSerializer, LinkAnonymousSerializer


class LinkViewSet(ModelViewSet):
    queryset = Link.objects.order_by('id')
    serializer_class = LinkSerializer
    pagination_class = PageNumberPagination

    def get_serializer_class(self):
        if not self.request.user.is_authenticated:
            return LinkAnonymousSerializer

        return super().get_serializer_class()

    def get_permissions(self):
        if self.action == 'create':
            return []

        return super().get_permissions()

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_staff:
            queryset = queryset.filter(creator=self.request.user)

        return queryset

    def perform_create(self, serializer):
        if not self.request.user.is_authenticated:
            serializer.save()
            return

        # Handle unique together, because creator is not required in serializer
        try:
            serializer.save(creator=self.request.user)
        except IntegrityError as e:
            if 'unique constraint' not in str(e).lower():
                raise e

            raise ValidationError({
                'url': ['This url is already exists for this user'],
            })

    @action(['get'], False, 's/(?P<code>[^/.]+)', permission_classes=[])
    def search(self, request, code):
        link = get_object_or_404(Link, code=code)
        serializer = self.get_serializer(link)
        return Response(serializer.data)
