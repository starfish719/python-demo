import graphene
from fastapi import FastAPI
from starlette.graphql import GraphQLApp

import app.graphql.query

app = FastAPI()
app.add_route("/graphiql", GraphQLApp(schema=graphene.Schema(query=query.Query)))