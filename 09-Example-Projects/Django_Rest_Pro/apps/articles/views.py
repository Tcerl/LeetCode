from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Article
from .serializers import ArticleSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    """Complete CRUD and Business Logic for Articles"""
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Senior Logic: Custom QuerySet
    def get_queryset(self):
        """Optimize query and add filtering"""
        qs = super().get_queryset()
        author_id = self.request.query_params.get('author')
        if author_id:
            qs = qs.filter(author_id=author_id)
        # Use select_related to fix N+1 issue
        return qs.select_related('author')

    def perform_create(self, serializer):
        """Attach currentUser to article"""
        serializer.save(author=self.request.user)

    # Custom Action: Mark as Published
    def partial_update(self, request, *args, **kwargs):
        """Override partial update for extra logic"""
        response = super().partial_update(request, *args, **kwargs)
        # Add Activity Notification here
        return response
