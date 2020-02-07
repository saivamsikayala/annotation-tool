from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name="home"),
    path('image_metadata',views.image_metadata,name="imageMetadata"),
    path('annotate',views.handle_annotation,name="handleAnnotation"),

]