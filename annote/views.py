from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
#from django.views.decorators.csrf import csrf_exempt

from .models import AnnoteModel

import json

#@csrf_exempt
@api_view(['GET', 'PATCH'])
@permission_classes((AllowAny, ))
def image_metadata(request):
    """
    Return image metadata.
    """
    if request.method == 'GET':
        try:
            image_metadata = AnnoteModel.objects.get(pk=1)
            return Response(image_metadata.content)
        except AnnoteModel.DoesNotExist:
            return Response({})

    elif request.method == 'PATCH':
        print(type(request.data['content']))
        try:
            image_metadata = AnnoteModel.objects.get(pk=1)
        except AnnoteModel.DoesNotExist:
            image_metadata = AnnoteModel()
        image_metadata.content = request.data['content']
        image_metadata.save()
        return Response(image_metadata.content, status=status.HTTP_201_CREATED)

#@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny, ))
def handle_annotation(request):
    #print ('------------ fsdfa: {}'.format(request.body))
    if request.method == 'POST':
        #print(request.FILES)
        dic = json.loads(request.data['annotate'])
        print(dic)
        for i in dic.keys():
            filename = i
        count=len(dic[filename]['regions'])
        for i in range(count):
            i = str(i)
            attempt = AnnoteModel()
            #attempt.shape = dic[filename]['regions'][i]['shape_attributes']['name']
            attempt.width = dic[filename]['regions'][i]['shape_attributes']['width']
            attempt.height = dic[filename]['regions'][i]['shape_attributes']['height']
            attempt.xcoordinate = dic[filename]['regions'][i]['shape_attributes']['x']
            attempt.ycoordinate = dic[filename]['regions'][i]['shape_attributes']['y']
            attempt.filename = filename
            attempt.image = request.FILES['image']
            attempt.attribute=request.POST.get('region')
            attempt.garbage = request.POST.get('garbage')
            #attempt.attribute = dic[filename]['regions'][i]['region_attributes']['name']
            attempt.save()

        #print ('---- JSON DATA ----\nDATA: {}',dic)
        #print(json_data)

    return Response({})

def index(request):
    return render(request, 'index.html')

def SaveAnnotate(request):
    return HttpResponse(":)")

# def parseJSON(dic,request):
#     for i in dic.keys():
#         filename = i
#     count=len(dic[filename]['regions'])
#     for i in range(count):
#         i = str(i)
#         attempt = AnnoteModel()
#         attempt.shape = dic[filename]['regions'][i]['shape_attributes']['name']
#         attempt.width = dic[filename]['regions'][i]['shape_attributes']['width']
#         attempt.height = dic[filename]['regions'][i]['shape_attributes']['height']
#         attempt.xcoordinate = dic[filename]['regions'][i]['shape_attributes']['x']
#         attempt.ycoordinate = dic[filename]['regions'][i]['shape_attributes']['y']
#         attempt.filename = filename
#         attempt.image = request.data['imagefile']
#         attempt.save()

