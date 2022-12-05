from aoc_utils import input_parse


input_parsed = input_parse("input_5.txt")
initial_schema = {
    "1": ["S", "M", "R", "N", "W", "J", "V", "T"],
    "2": ["B", "W", "D", "J", "Q", "P", "C", "V"],
    "3": ["B", "J", "F", "H" , "D", "R", "P" ],
    "4": ["F", "R", "P", "B", "M", "N", "D"], 
    "5": ["H", "V","R", "P", "T", "B"],
    "6": ["C", "B", "P", "T"], 
    "7": ["B", "J", "R", "P","L"], 
    "8": ["N", "C", "S", "L", "T", "Z", "B", "W"], 
    "9": ["L", "S", "G"]
}


def crate_printer(schema):
    crate = []
    for c in schema.keys():
        crate.append(schema[c][-1])
    print("Crane schema: ","".join(crate))


def crate_movement(schema, movement, ver):
    initial_schema = schema
    ls_movement = movement.split("\n")
    for mv in ls_movement:
        quantity, mv_from, mv_to = mv.split(" ")[1], mv.split(" ")[3],mv.split(" ")[-1]
        to_move = schema[mv_from][-int(quantity):]
        if to_move and ver == 1:
            to_move.reverse()
        schema[mv_from] = schema[mv_from][:len(schema[mv_from])-int(quantity)]
        schema[mv_to] = schema[mv_to] + to_move
    crate_printer(schema)
    

initial_schema = crate_movement(initial_schema, input_parsed,2)

initial_schema = {
    "1": ["S", "M", "R", "N", "W", "J", "V", "T"],
    "2": ["B", "W", "D", "J", "Q", "P", "C", "V"],
    "3": ["B", "J", "F", "H" , "D", "R", "P" ],
    "4": ["F", "R", "P", "B", "M", "N", "D"], 
    "5": ["H", "V","R", "P", "T", "B"],
    "6": ["C", "B", "P", "T"], 
    "7": ["B", "J", "R", "P","L"], 
    "8": ["N", "C", "S", "L", "T", "Z", "B", "W"], 
    "9": ["L", "S", "G"]
}


crate_movement(initial_schema, input_parsed,1)