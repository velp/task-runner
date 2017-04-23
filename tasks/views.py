import json
from django.views import View
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from tasks.models import Task


class TasksView(View):

    def get(self, request, *args, **kwargs):
        data = list()
        for task in Task.objects.all().order_by('create_time'):
            data.append(task.serialize)
        return HttpResponse(json.dumps(data))

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        task = Task()
        task.save()
        return HttpResponse(json.dumps(task.serialize))