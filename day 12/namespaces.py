#Local scope

# def drink_potion():
#     potion_strenght = 2
#     print(potion_strenght)

# drink_potion()

#Global scope

player_health = 10

def drink_potion():
    potion_strenght = 2
    print(player_health)

drink_potion()