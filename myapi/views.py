from django.db.models import Q
from django.shortcuts import redirect
from rest_framework import viewsets
from .models import waifu
from .serializers import waifuSerializer, imageSerializer


class waifuViewSet(viewsets.ModelViewSet):
    serializer_class = waifuSerializer
    #queryset = waifu.objects.all()

    def get_queryset(self):
        queryset = waifu.objects.all()
        name = self.request.query_params.get('name',None)
        search_String = self.request.query_params.get('search',None)
        popularity = self.request.query_params.get('popularity','false')
        like = self.request.query_params.get('like','false')
        trash = self.request.query_params.get('trash','false')
        likeCount = self.request.query_params.get('likeCount','false')
        trashCount = self.request.query_params.get('TrashCount','false')
        if search_String is not None:
            queryset = queryset.filter( Q(name__contains=search_String)  | Q(orName__contains=search_String) | Q(roName__contains=search_String))
        if name == 'true':
            return queryset.order_by('name')
        elif popularity=='true':
            return queryset.order_by('popularity')
        elif like == 'true':
            return queryset.order_by('like')
        elif trash == 'true':
            return queryset.order_by('trash')
        elif likeCount == 'true':
            return queryset.order_by(likeCount)
        elif trashCount == 'true':
            return queryset.order_by(trashCount)
        return queryset
class imageViewSet(viewsets.ModelViewSet):
    serializer_class = imageSerializer
    '''
    def dispatch(self, request, *args, **kwargs):
        print(request)
        id = str(request).split("/image/", 2)[1].split('/', 1)[0]
        response = redirect('https://mywaifulist.moe/api/waifu/12755/gallery?page=0')
        response["x-requested-with"] = "XMLHttpRequest"
        return response
        '''
    def get_queryset(self):
        queryset = waifu.objects.all()
        request = str(self.request)
        id = request.split("/image/", 2)[1].split('/', 1)[0]
        try :
            int(id)
            return queryset
        except:
            return ""
