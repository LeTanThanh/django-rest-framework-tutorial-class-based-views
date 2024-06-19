from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response

from ...models.snippet import Snippet
from ...serializers.snippet_serializer import SnippetSerializer


class SnippetDetailAPIView(APIView):
    def get(self, request, pk, format=None):
        snippet = self.get_snippet(pk=pk)
        serializer = SnippetSerializer(instance=snippet)
        data = serializer.data

        return Response(data=data)

    def get_snippet(self, pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404
