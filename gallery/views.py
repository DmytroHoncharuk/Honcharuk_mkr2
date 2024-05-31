from django.shortcuts import render, get_object_or_404
from .models import Image, Category

def gallery_view(request):
    categories = Category.objects.all()
    return render(request, 'gallery.html', {'categories': categories})

def image_detail(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    return render(request, 'image_detail.html', {'image': image})
