import graphene
import graphene_django
from products.models import Product, Store


# class ProductType(graphene.ObjectType):
#     id = graphene.Int()
#     name = graphene.String()
class ProductType(graphene_django.DjangoObjectType):
    class Meta:
        model = Product
        exclude = []


class Query(graphene.ObjectType):
    my_string = graphene.String()
    products = graphene.List(ProductType)

    def resolve_my_string(self, *args, **kwargs):
        return 'Hello, darling!'

    def resolve_products(self, *args, **kwargs):
        products = Product.objects.all()
        return products


class CreateStoreMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String()

    id = graphene.Int()
    ok = graphene.Boolean()
    error = graphene.String()

    @classmethod
    def mutate(cls, *args, name=None, **kwargs):
        store = Store.objects.create(owner_id=1, name=name)
        return cls(id=store.id, ok=True, error=None)


class Mutation(graphene.ObjectType):
    create_store = CreateStoreMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
