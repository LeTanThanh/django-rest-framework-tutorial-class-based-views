from rest_framework.mixins import RetrieveModelMixin
from rest_framework.mixins import UpdateModelMixin
from rest_framework.mixins import DestroyModelMixin

from rest_framework.generics import GenericAPIView

from ....models.snippet import Snippet
from ....serializers.snippet_serializer import SnippetSerializer


class SnippetDetailAPIView(RetrieveModelMixin,
                           UpdateModelMixin,
                           DestroyModelMixin,
                           GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
