import string
from aoc_utils import input_parse

input_data = input_parse("input_3.txt")

def points_by_table() -> list:
    points_table = [] 
    
    for letter in string.ascii_lowercase:
        points_table.append(letter)
    
    for letter in string.ascii_uppercase:
        points_table.append(letter)
    
    points_table.insert(0, "zero_points")

    return points_table


### PART I
def main_checker_rucksacks(rucksacks:str) -> int:
    rucksacks_list = rucksacks.split("\n")
    points_table = points_by_table()
    items_points = 0
    for rs in rucksacks_list:
        first_part = list(rs[:len(rs)//2])
        second_part = list(rs[len(rs)//2:])
        item = set(first_part).intersection(second_part).pop()
        item_points = points_table.index(item)
        items_points += item_points
    return items_points

print(f'Items: {main_checker_rucksacks(input_data)}')


### PART II
def _by_gropups(rksl, l):
    return zip(*[iter(rksl)]*l)
  
    
def badge_checker(rucksacks:str) -> int:
    rucksacks_list = rucksacks.split("\n")
    points_table = points_by_table()
    badge_points = 0    
    elven_groups = list(_by_gropups(rucksacks_list,3))
    
    for eg in elven_groups:
        rucksack_1, rucksack_2, rucksack_3 = set(eg[0]), set(eg[1]), set(eg[2])
        potential_badges = rucksack_1.intersection(rucksack_2)
        badge = set(potential_badges).intersection(rucksack_3).pop()
        badge_points += points_table.index(badge)
    return badge_points


print(f'Badge: {badge_checker(input_data)}')