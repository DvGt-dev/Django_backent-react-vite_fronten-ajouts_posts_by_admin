from django.shortcuts import render
from .models import Shape
import json

# Create your views here.
def home_view(request):
    shapes = [{"type": x.type, "color": x.color} for x in Shape.objects.all()]
    shape_json = json.dumps(shapes)
    context = {}
    return render(request, 'shapes/main.html', context)

