import graphene
import graphql_jwt

import events.schema
import users.schema


# Query for getting data from the server
class Query(users.schema.Query, events.schema.Query, graphene.ObjectType):
    pass

class Mutation(users.schema.Mutation, events.schema.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

#create schema
schema = graphene.Schema(query=Query, mutation=Mutation)