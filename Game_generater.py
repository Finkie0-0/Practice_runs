import random
games = ("FCPrimal","Hades","Wiz","ROR2","DC","DID","Forager","WatchDogs","Borderlands","SOD")
length = 1
picked_game = "".join(random.sample(games,length))
print(f"YOU WILL PLAY: {picked_game}")
