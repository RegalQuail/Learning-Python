import json
from urllib.request import urlopen
from tabulate import tabulate

url = "https://ipinfo.io/json"
response = urlopen(url)
data = json.load(response)

table = [["IP-Adress:", data["ip"]],
          ["Server:", data["org"]],
          ["City:", data["city"]],
          ["Country:", data["country"]],
          ["Region:", data["region"]]]

print(tabulate(table))