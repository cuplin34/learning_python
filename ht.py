import requests
from random import randint

#simple example of using a simple http scraping program
def the_joker():
    joke = input("What joke what you like to look for?\n")
    res = requests.get("https://icanhazdadjoke.com/search", headers={"Accept": "application/json"}, params={"term": joke})
    res = res.json()
    joke_len = res.get("total_jokes")
    if joke_len > 1:
        print(f"I have {joke_len} total {joke} jokes, heres one:")
        print(res.get("results")[randint(0,joke_len)].get("joke"))
    elif joke_len == 1:
        print(f"I have {joke_len} joke about {joke}, here it is:")
        print(res.get("results")[0].get("joke"))
    else: print("Sorry I have no jokes about that")

the_joker()