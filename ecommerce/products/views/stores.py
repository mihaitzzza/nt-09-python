from django.shortcuts import render, Http404, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from products.models import Store
from likes.models import Like


def get_all_stores(request):
    stores = Store.objects.all()

    return render(request, 'products/stores.html', {
        'stores': stores
    })


def get_store(request, store_id):
    # store = Store.objects.filter(id=store_id).first()
    # try:
    #     store = Store.objects.get(id=store_id)
    # except Store.DoesNotExist:
    #     raise Http404('Unavailable store.')
    store = get_object_or_404(Store, id=store_id)

    return render(request, 'products/store.html', {
        'store': store
    })


@login_required
def like_store(request, store_id):
    if request.method != 'POST':
        raise Http404('This method is not supported.')

    store = get_object_or_404(Store, pk=store_id)
    like = store.likes.filter(user=request.user).first()
    if like is None:
        Like.objects.create(
            user=request.user,
            content_object=store
        )
    else:
        like.delete()

    return redirect(reverse('stores:store_details', kwargs={'store_id': store.id}))
