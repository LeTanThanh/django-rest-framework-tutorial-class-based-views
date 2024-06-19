from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from .views.snippets.snippet_list_api_view import SnippetListAPIView

urlpatterns = [
    path("", SnippetListAPIView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
