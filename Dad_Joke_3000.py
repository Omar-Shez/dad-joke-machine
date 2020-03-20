import requests
import pyfiglet
from termcolor import colored
#where the dad jokes are coming from
url = "https://icanhazdadjoke.com/search"
#displays name of program with effects
intro_message = colored(pyfiglet.figlet_format("DAD JOKE 3000"),
    color="yellow", attrs=["blink"])
print(intro_message)

topic = input("Let me tell you a joke! Give me a topic: ")
#the http response from the website
response = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term": topic, "limit": 1})
#save the request in a variable
data = response.json()
#save the jokes from the request in a variable
x = (data["results"])
#if input came back with no jokes
if len(x) == 0:
    print("Sorry no jokes about", topic)
else:
    #data from jokes comes back as dictionary
    #so it pulls it from the dictionary
    dad_joke = x[0]
    print("I've got", data["total_jokes"], "jokes about", topic, "Here it is:")
    print(dad_joke["joke"])
