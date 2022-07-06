import graphene
from products.models import Product


class ProductTypes(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()


class Query(graphene.ObjectType):
    my_string = graphene.String()
    products = graphene.List(ProductTypes)

    def resolve_my_string(self):
        return 'Hello, world!'

    def resolve_my_products(self):
        products = Product.objects.all()
        return [ProductTypes(product) for product in products]



schema = graphene.Schema(query=Query)
