from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from .models import Woman
from .serializers import WomenSerializer
from rest_framework.views import APIView


class WomenAPIList(generics.ListAPIView):
    queryset = Woman.objects.all()
    serializer_class = WomenSerializer


class WomenAPIView(APIView):

    def get(self, request):
        w = Woman.objects.all()
        return Response({'posts': WomenSerializer(w, many=True).data})

    def post(self, request):
        serializer = WomenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)

        if not pk:
            return Response({'error': 'Method PUT not allowed'})

        try:
            instance = Woman.objects.get(pk=pk)
        except:
            return Response({'error': 'Method PUT not allowed'})

        serializator = WomenSerializer(data=request.data, instance= instance)
        serializator.is_valid(raise_exception=True)
        serializator.save()

        return Response({'post': serializator.data })

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)

        if not pk:
            return Response({'error': 'Method DELETE not allowed 1'})

        try:
            #instance = Woman.objects.get(pk=pk)
            instance = Woman.objects.get(pk=pk)
            print('pk', pk)
            instance.delete()
        except:
            return Response({'error': 'Method DELETE not allowed 2'})

        return Response({'delete': kwargs.get('pk') })




# class WomenAPIView(generics.ListAPIView):
#     queryset = Woman.objects.all()
#     serializer_class = WomenSerializer
