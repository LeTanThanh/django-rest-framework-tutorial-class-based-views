from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from ...models.snippet import Snippet
from ...serializers.snippet_serializer import SnippetSerializer


class SnippetListAPIView(APIView):
    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(instance=snippets, many=True)
        data = serializer.data

        return Response(data=data)

    def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            data = serializer.data

            return Response(data=data, status=status.HTTP_201_CREATED)

        data = serializer.errors
        return Response(data=data, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
