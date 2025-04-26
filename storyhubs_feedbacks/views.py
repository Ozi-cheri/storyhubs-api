from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from storyhubs_api.permissions import IsOwnerOrReadOnly
from .models import StoryhubsFeedback
from .serializers import StoryhubsFeedbackSerializer


class StoryhubsFeedbackList(generics.ListCreateAPIView):
    serializer_class = StoryhubsFeedbackSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = StoryhubsFeedback.objects.annotate(
        likes_count=Count('likes', distinct=True),
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__followed__owner__profile',
        'likes__owner__profile',
        'owner__profile',
    ]
    search_fields = [
        'owner__username',
        'story_title',
        'story_creator',
        'category',
    ]
    ordering_fields = [
        'likes_count',
        'likes__created_at',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class StoryhubsFeedbackDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StoryhubsFeedbackSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = StoryhubsFeedback.objects.annotate(
        likes_count=Count('likes', distinct=True),
    ).order_by('-created_at')