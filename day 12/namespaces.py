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


#How to modify a global variable

enemies = 1

print(f"enemy count: {enemies}")

def increase_enemy():
    #Avooid modifying variables using the global keyword 
    # global enemies
    # enemies += 1
    return enemies + 1

enemies = increase_enemy()
print(f"enemy count: {enemies}")


