import requests
from bs4 import BeautifulSoup

class Temperature(object):
    def __init__(self):
        self.place = place
    
    def __repr__(self):
        temperature = self.weather()
        return str(f"It is currently {temperature} in {self.place}")
    
    def weather(self):
        url = f"https://www.google.com/search?&q=weather in {self.place}"
        req = requests.get(url)
        scrape = BeautifulSoup(req.text, "html.parser")
        temperature = scrape.find("div", class_="BNeawe").text
        return temperature

if __name__ == "__main__":
    print(Temperature("France"))
