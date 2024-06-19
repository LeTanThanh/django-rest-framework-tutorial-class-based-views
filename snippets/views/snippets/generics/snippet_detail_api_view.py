from rest_framework.generics import RetrieveUpdateDestroyAPIView

from ....models.snippet import Snippet
from ....serializers.snippet_serializer import SnippetSerializer


class SnippetDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
