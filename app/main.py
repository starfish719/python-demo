import graphene
from fastapi import FastAPI
from starlette.graphql import GraphQLApp

class Hoge(graphene.ObjectType):
  id = graphene.ID()
  name = graphene.String()

class Fuga(graphene.ObjectType):  
  hello = graphene.String(name=graphene.String(default_value="stranger"))
  goodbye = graphene.String()

  def resolve_hello(self, info, name):
    return "Hello " + name
  
  def resolve_goodbye(root, info):
    return 'See ya!'

class Query(graphene.ObjectType):
  hoge = graphene.Field(Hoge)
  fuga = graphene.Field(Fuga)

  def resolve_hoge(root, info):
    return Hoge(id = "abcdefg1234567", name = "hoge_name")

  def resolve_fuga(root, info):
    return Fuga()


app = FastAPI()
app.add_route("/graphiql", GraphQLApp(schema=graphene.Schema(query=Query)))