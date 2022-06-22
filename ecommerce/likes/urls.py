from django.urls import path
from likes.views import like_object

app_name = 'likes'

urlpatterns = [
    path('<str:model_type>/<int:object_id>/like', like_object, name='like')
]