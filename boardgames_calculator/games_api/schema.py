import graphene

from graphene_django.types import DjangoObjectType

from boardgames_calculator.games_api.models import Boardgame, Category

class BoardgameType(DjangoObjectType):
  class Meta:
    model = Boardgame

class CategoryType(DjangoObjectType):
  class Meta:
    model = Category

class Query(object):
  boardgame = graphene.Field(
    BoardgameType,
    id=graphene.Int(),
    name=graphene.String()
  )

  all_boardgames = graphene.List(BoardgameType)

  def resolve_all_boardgames(self, info, **kwargs):
    return Boardgame.objects.all()

  def resolve_boardgame(self, info, **kwargs):
    id = kwargs.get('id')
    name = kwargs.get('name')

    if id is not None:
      return Boardgame.objects.get(pk=id)

    if name is not None:
      return Boardgame.objects.get(name=name)

    return None
