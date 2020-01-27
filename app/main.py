import graphene
from fastapi import FastAPI
from starlette.graphql import GraphQLApp

from app.graphql.query import Query

app = FastAPI()
app.add_route("/graphiql", GraphQLApp(schema=graphene.Schema(query=Query)))