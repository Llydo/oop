import sys, time, random
from os import system, name
from oop import *

surname_list = ["Baratheon", "Greystone", "Storm-Blossom", "Skull-Splitter", "The Bard"]

typewrite(f"{Colour.Yellow}Welcome to Code Nation RPG{Colour.End}\n")

clear()
player_one = Character()
typewrite(f"{Colour.Yellow}What is your name?{Colour.End}\n")
p_one_name = input(f"{Colour.Red}> {Colour.End}")
player_one.create(p_one_name, random.choice(surname_list))

typewrite(f"{Colour.Yellow}Excellent!\nYour Name is {Colour.Green}{player_one.access_name()}{Colour.Yellow}...{Colour.End}")

