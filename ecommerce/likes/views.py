from django.shortcuts import render, redirect, reverse, get_object_or_404, Http404
from products.models import Product, Store
from likes.models import Like


def like_object(request, model_type, object_id):
    if request.method != 'POST':
        raise Http404('This method is not supported.')

    if model_type == 'products':
        my_model = Product
        redirect_url = reverse('products:product_details', kwargs={'product_id': object_id})
    elif model_type == 'stores':
        my_model = Store
        redirect_url = reverse('stores:store_details', kwargs={'store_id': object_id})
    else:
        raise Http404('Object is not likeable.')

    likeable_object = get_object_or_404(my_model, pk=object_id)
    like = likeable_object.likes.filter(user=request.user).first()
    if like is None:
        Like.objects.create(
            user=request.user,
            content_object=likeable_object
        )
    else:
        like.delete()

    print('\n' * 2)
    print('model_type', model_type)
    print('object_id', object_id)
    print('\n' * 2)
    # return redirect(reverse('??', kwargs={'??': object_id}))

    return redirect(redirect_url)
