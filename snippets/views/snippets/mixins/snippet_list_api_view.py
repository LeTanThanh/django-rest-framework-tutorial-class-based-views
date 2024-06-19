from rest_framework.mixins import ListModelMixin
from rest_framework.mixins import CreateModelMixin
from rest_framework.generics import GenericAPIView

from ....models.snippet import Snippet
from ....serializers.snippet_serializer import SnippetSerializer


class SnippetListAPIView(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
