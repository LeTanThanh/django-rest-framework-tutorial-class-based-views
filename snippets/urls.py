from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

# from .views.snippets.snippet_list_api_view import SnippetListAPIView
from .views.snippets.mixins.snippet_list_api_view import SnippetListAPIView

# from .views.snippets.snippet_detail_api_view import SnippetDetailAPIView
from .views.snippets.mixins.snippet_detail_api_view import SnippetDetailAPIView

urlpatterns = [
    path("", SnippetListAPIView.as_view()),
    path("<int:pk>/", SnippetDetailAPIView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
