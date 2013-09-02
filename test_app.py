from ConfigParser import ConfigParser

from mantisbt.client import MantisClient


config = ConfigParser()
config.readfp(open('test.conf'))
username = config.get('CREDENTIALS', 'username')
password = config.get('CREDENTIALS', 'password')

server_url = config.get('SERVER', 'url')

client = MantisClient(username, password, server_url)
result = client.get_users_projects()
issues = client.project_get_issues(result[0])
import ipdb
ipdb.set_trace()
print result

