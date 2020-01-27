import graphene

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