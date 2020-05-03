import graphene

import boardgames_calculator.games_api.schema

class Query(boardgames_calculator.games_api.schema.Query, graphene.ObjectType):
  pass

schema = graphene.Schema(query=Query)
