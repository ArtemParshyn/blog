from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from .models import Comment, Blog, User
from .serializers import BlogSerializer, UserSerializer, CommentSerializer
from rest_framework.response import Response


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ["get", "post"]


class BlogModelViewSet(ModelViewSet):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    http_method_names = ["get", "post", "delete", "path"]

    def create(self, request, *args, **kwargs):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentModelViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    http_method_names = ["get", "post", "delete", "path"]

    def create(self, request, *args, **kwargs):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
