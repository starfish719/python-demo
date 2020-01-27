import graphene

import app.graphql.schema.sample_schema

class Query(graphene.ObjectType):
  hoge = graphene.Field(sample_schema.Hoge)
  fuga = graphene.Field(sample_schema.Fuga)

  def resolve_hoge(root, info):
    return sample_schema.Hoge(id = "abcdefg1234567", name = "hoge_name")

  def resolve_fuga(root, info):
    return sample_schema.Fuga()