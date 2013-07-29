from suds.client import Client
from ConfigParser import ConfigParser


config = ConfigParser()
config.readfp(open('test.conf'))
username = config.get('CREDENTIALS', 'username')
password = config.get('CREDENTIALS', 'password')

server_url = config.get('SERVER', 'url')

client = Client(server_url)
result = client.service.mc_issue_get(username, password, 78544)
import ipdb
ipdb.set_trace()
print result

