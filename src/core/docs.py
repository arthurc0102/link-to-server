from rest_framework.permissions import IsAdminUser


config = {
    'title': 'API Document',
    'permission_classes': [IsAdminUser],
}
