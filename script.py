from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport

def getApplications(client, offset):
    query = gql(
    """
    query {
        applications(limit: 100, offset: """+str(offset)+""") {
            nodes {
                name,
			    environments (limit: 100) {
                    nodes {
                        name
                    }
			    }
                pipelines (limit: 100) {
                    nodes {
                        name
                    }
                }
            }
        }
    }
    """
    )

    result = client.execute(query)

    return result['applications']['nodes']

# Create a transport to the harness graqhql endpoint
transport = AIOHTTPTransport(url="https://app.harness.io/gateway/api/graphql?accountId=TEyxLP87RquOEph_GrbYvQ", headers={'x-api-key': 'YOUR_API_KEY='})

# Create a GraphQL client using the defined transport
client = Client(transport=transport, fetch_schema_from_transport=True)

# Get initial application list
applications = getApplications(client, 0)

# Loop to get remaining as long as amount return is less than 100
newApplications = applications
offset = 0
while (len(newApplications) >= 100):
    offset = offset + 100
    newApplications = getApplications(client, offset)

    applications = applications + newApplications
    

print(applications)