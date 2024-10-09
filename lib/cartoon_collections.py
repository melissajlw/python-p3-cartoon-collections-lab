def roll_call_dwarves(dwarves):
    i = 1
    for dwarf in dwarves:
        print(f"{i}. {dwarf}")
        i += 1

def summon_captain_planet(lst):
    new_lst = []
    for item in lst:
        new_lst.append(f"{item[0].upper()}{item[1::]}!")
    return new_lst

def long_planeteer_calls(lst):
    for item in lst:
        if len(item) > 4:
            return True
    return False

def find_the_cheese(lst):
    cheeses = ["cheddar", "gouda", "camembert"]
    for item in lst:
        if item in cheeses:
            return item
    return None
