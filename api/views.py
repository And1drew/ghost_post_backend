from django.shortcuts import render
from rest_framework import viewsets, status
from api.serializers import BoastOrRoastSerializer
from boastOrRoast.models import BoastOrRoast
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.


class BoastOrRoastViewSet(viewsets.ModelViewSet):
    queryset = BoastOrRoast.objects.all()
    serializer_class = BoastOrRoastSerializer

    @action(detail=True, methods=['get','post'])
    def like(self, request, pk=None):
        post = self.get_object()
        post.up_votes += 1
        post.vote_score = post.up_votes - post.down_votes
        post.save()
        return Response({'status': 'like post'})


    @action(detail=True, methods=['get','post'])
    def dislike(self, request, pk=None):
        post = self.get_object()
        post.down_votes += 1
        post.vote_score = post.up_votes - post.down_votes
        post.save()
        return Response({'status': 'dislike post'})


    @action(detail=False, methods=['get'])
    def voteScoreOrder(self, request):
        posts = BoastOrRoast.objects.order_by('vote_score').reverse()  
        serializer = BoastOrRoastSerializer(posts, many=True)
        return Response(serializer.data)