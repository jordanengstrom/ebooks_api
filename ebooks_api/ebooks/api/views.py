from rest_framework import generics
from rest_framework import mixins

from ebooks_api.ebooks.models import Ebook
from ebooks_api.ebooks.api.serializers import EbookSerializer

class EbookListCreateAPIView(mixins.CreateModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

