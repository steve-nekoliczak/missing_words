from rest_framework import viewsets

from ..serializers import DocumentSerializer
from ..models.document import Document


class DocumentViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()
