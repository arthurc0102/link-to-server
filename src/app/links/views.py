from django.db.utils import IntegrityError

from rest_framework.exceptions import ValidationError
from rest_framework.viewsets import ModelViewSet

from .models import Link
from .serializers import LinkSerializer


class LinkViewSet(ModelViewSet):
    queryset = Link.objects.order_by('id')
    serializer_class = LinkSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_staff:
            queryset = queryset.filter(creator=self.request.user)

        return queryset

    def perform_create(self, serializer):
        # Handle unique together, because creator is not required in serializer
        try:
            serializer.save(creator=self.request.user)
        except IntegrityError as e:
            if 'unique constraint' not in str(e).lower():
                raise e

            raise ValidationError({
                'url': ['This url is already exists for this user'],
            })
