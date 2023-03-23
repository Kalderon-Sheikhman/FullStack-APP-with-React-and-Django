from rest_framework.generics import ListAPIView
from rest_framework import permissions

from .models import Certification
from .serializers import CertificationSerializer


class CertificationListView(ListAPIView):
  permission_classes = (permissions.AllowAny, )
  queryset = Certification.objects.all()
  serializer_class = CertificationSerializer
  pagination_class = None