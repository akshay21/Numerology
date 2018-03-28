name = 'akshay'

def name_to_sum(name):
    numeric_dict = {"a":1,"i":1,"j":1,"q":1,"y":1,
                "b":2,"k":2,"r":2,
                "c":3,"g":3,"l":3,"s":3,
                "d":4,"m":4,"t":4,
                "e":5,"h":5,"n":5,"x":5,
                "u":6,"v":6,"w":6,
                "o":7,"z":7,
                "f":8,"p":8}

    num_code = [numeric_dict.get(x, 0) for x in list(name.lower())]
    sm = sum(num_code)
    if sm == 0:
        return 0
    if sm%9 == 0:
        return 9
    else:
        return num_code, sm%9

ncode, tot = name_to_sum(name)

# output to be printed back to the screen
print(ncode)
print(tot)