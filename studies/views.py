from rest_framework import generics

from .models import Certification, Titulation
from .serializers import CertificationSerializer, TitulationSerializer


class TitulationList(generics.ListAPIView):
    queryset = Titulation.objects.all()
    serializer_class = TitulationSerializer


class TitulationDetail(generics.RetrieveAPIView):
    queryset = Titulation.objects.all()
    serializer_class = TitulationSerializer


class CertificationList(generics.ListAPIView):
    queryset = Certification.objects.all()
    serializer_class = CertificationSerializer


class CertificationDetail(generics.RetrieveAPIView):
    queryset = Certification.objects.all()
    serializer_class = CertificationSerializer
