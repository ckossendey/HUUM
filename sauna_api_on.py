
import requests
import huum_config

#


url = 'https://api.huum.eu/action/home/start'
myobj = {'targetTemperature' : 40}
#enter your username and password from app
usern = 'yourusername@something.bla'
passwo = 'thepassword of your app'
x = requests.post(url, data = myobj, auth=(usern,passw))
print(x.json())

