from django.db import models
from django.contrib.auth.models import User
from storyhubs_feedbacks.models import StoryhubsFeedback


class Like(models.Model):
    """
    Allows users to 'like' feedback.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        StoryhubsFeedback, related_name='likes', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'post']

    def __str__(self):
        return f'{self.owner} {self.post}'
