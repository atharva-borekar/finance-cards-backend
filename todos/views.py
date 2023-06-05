from django.http import JsonResponse
from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import APIException, NotFound
from .serializers import TodoSerializer
from .models import Todo


@api_view(['GET'])
def apiOverview(request):
    apiUrls = {
        'getAll': '/',
        'Detail View': '/<str:pk>/',
        'Create': '/create',
        'Update': '/update/<str:pk>',
        'Delete': '/delete/<str:pk>'
    }
    return Response(apiUrls)


@api_view(['GET'])
def todoList(request):
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def todoCreate(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({"message": 'Todo Created Successfully'})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # {
    #     "title": "TODO 2",
    #     "description": "TODO 2 description"
    # }


@api_view(['PUT'])
def todoUpdate(request, pk):
    try:
        todo = Todo.objects.get(id=pk)
        if todo:
            serializer = TodoSerializer(instance=todo, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"message": "Todo updated successfully!"})
            # {
            #     "title": "TODO 2",
            #     "description": "TODO 2 description"
            # }
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            raise NotFound('Todo not found')
    except Exception as e:
        response = JsonResponse({"message": e.args})
        return response


@api_view(['DELETE'])
def todoDelete(request, pk):
    todo = Todo.objects.get(id=pk)
    if todo is None:
        return JsonResponse({"message": "Todo not found!"}, 204)
    todo.delete()
    # {
    #     "title": "TODO 2",
    #     "description": "TODO 2 description"
    # }
    return JsonResponse({"message": "Todo #f{id} deleted successfully!"}, 200)
