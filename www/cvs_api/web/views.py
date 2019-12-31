# Create your views here.
from web.models import Cvs
from web.serializers import CvsSerializer

from rest_framework import generics, viewsets


# Create your views here.
class CvsViewSet(viewsets.ModelViewSet):
    queryset = Cvs.objects.all()
    serializer_class = CvsSerializer
    def get_queryset(self):
        # return  Cvs.objects.filter(article_time="12月31日")
        queryset = Cvs.objects.all()
        article_time = self.request.query_params.get('article_time', None)
        if article_time:
            queryset = queryset.filter(article_time=article_time)
        return queryset

# class CvsList(generics.ListAPIView):
#     serializer_class = CvsSerializer

#     def get_queryset(self):
#         return Cvs.objects.filter(article_time="12月30日")
        # queryset = Cvs.objects.all()
        # console.log(self.request)
        # article_time = self.request.query_params.get('article_time', None)
        # if username:
        #     queryset = queryset.filter(article_time=article_time)
        # return queryset