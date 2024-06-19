from rest_framework.generics import ListCreateAPIView

from ....models.snippet import Snippet
from ....serializers.snippet_serializer import SnippetSerializer


class SnippetListAPIView(ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
