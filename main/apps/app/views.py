# -*- coding: utf-8 -*-

"""This module should contains all the views of your app. An api is also a view"""

################################# API SECTION #################################

# from .models import MyModel
# from .serializers import MySerializer
# from rest_framework import viewsets, permissions
# from rest_framework.decorators import detail_route, list_route, api_view, permission_classes
# from rest_framework.response import Response
# from rest_framework.reverse import reverse

# @api_view(('GET',))
# @permission_classes([permissions.IsAuthenticated])
# def api_root(request, format=None): #This is an example of what you can do with rest_framework Response object
#     return Response({
#         "myapi": reverse('profile-list', request=request, format=format), # simply transform the reverse to an url
#         "dump": MySerializer(MyModel.objects.filter(user=request.user), many=True, context={"request": request}).data
#         # We put many=True because this will return a queryset. If you perform an objects.get query put many=False
#     })
# # This will generate a JSON containing {"myapi": "an-url-to-another-api", "dump": {all info fetched by the queryset rendered with MySerializer}}

# class MyViewSet(viewsets.ModelViewSet):
#     """
#     This viewset does stuff
#     it does so much cool
#     am -- cool stuff
#     """
#     model = MyModel
#     serializer_class = MySerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def get_queryset(self):
#         return MyModel.objects.filter(owner=self.request.user)

#     def list(self, request):
#         return super(MyViewSet, self).list(request)

#     def create(self, request):
#         return super(MyViewSet, self).create(request)

#     def retrieve(self, request, pk=None):
#         return super(MyViewSet, self).retrieve(request, pk)

#     def update(self, request, pk=None):
#         return super(MyViewSet, self).update(request, pk)

#     def partial_update(self, request, pk=None):
#         return super(MyViewSet, self).partial_update(request, pk)

#     def destroy(self, request, pk=None):
#         return super(MyViewSet, self).destroy(request, pk)

#     @detail_route(methods=['post'])
#     def my_detail(self, request, pk=None):
#         pass

#     @list_route()
#     def my_list(self, request):
#         pass

#     def perform_create(self, serializer):
#         # do something before save
#         serializer.save(user=self.request.user) # save
#         # do something after save

#     def perform_update(self, serializer):
#         # do something before update
#         serializer.save(user=self.request.user) # update
#         # do something after update

#     def perform_destroy(self, instance):
#         # do something before delete
#         instance.delete() # delete
#         # do something after delete


################################ VIEWS SECTION ################################

# def my_view(request):
#     if request.method == "POST":
#         #do_stuff with request.POST
#         return {"data": mydata}
#     else:
#         return {}
