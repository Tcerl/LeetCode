from django.db import models

class ArticleManager(models.Manager):
    """Custom Manager for Professional Logic"""
    def published(self):
        return self.filter(status='published')

    def by_author(self, user):
        return self.filter(author=user)

# Update models.py to use this manager
# (Actual edit below)
