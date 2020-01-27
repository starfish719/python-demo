import graphene

from app.graphql.schema.sample_schema import Hoge, Fuga

class Query(graphene.ObjectType):
  hoge = graphene.Field(Hoge)
  fuga = graphene.Field(Fuga)

  def resolve_hoge(root, info):
    return Hoge(id = "abcdefg1234567", name = "hoge_name")

  def resolve_fuga(root, info):
    return Fuga()