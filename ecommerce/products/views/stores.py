from django.shortcuts import render, Http404, get_object_or_404
from products.models import Store


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
