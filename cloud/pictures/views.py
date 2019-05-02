from django.shortcuts import render
from rest_framework.views import APIView
from pictures.models import *
from rest_framework.response import Response
from rest_framework          import generics, status, exceptions
from django.http import HttpResponseRedirect


# class CreateUserAPIView(generics.CreateAPIView):
#     serializer_class = CreateUserSerializer
#     permission_classes = [AllowAny]

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         # We create a token that will be used for future auth
#         token = Token.objects.create(user=serializer.instance)
#         token_data = {"token": token.key}
#         return Response(
#             {**serializer.data, **token_data},
#             status=status.HTTP_201_CREATED,
#             headers=headers
#         )

import os
class ShowNGOChild(APIView):
    def get(self, request, format=None):
        maps = ChildNGOMap.objects.all()
        mapTuple = []
        for x in maps:
            mapTuple.append([x.child.name, x.ngo.id])

        print("*****")
        print(os.getcwd() + '/html/ngo-child.html')
        # return HttpResponseRedirect(os.getcwd() + '/html/ngo-child.html',{
        #     "map": mapTuple
        # })
        # return Response({
        #     "text": mapTuple
        # }, status=status.HTTP_200_OK)

        return render(request, 'pictures/ngo-child.html', {
            "map": mapTuple
        })


