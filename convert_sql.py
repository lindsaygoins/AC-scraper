

def convert_sql(file_name):
    f = open(file_name, 'r')
    line = f.read()
    pieces = line.split(',')
    rugs = pieces[:545]
    wall_floor = pieces[545:]

    count_name = 5
    count_category = 4
    count_size = 3
    for i, rug in enumerate(rugs):
        if count_name == 5:
            rugs[i] = rug[0] + '"' + rug[1:] + '"'
            count_name = 0
        elif count_category == 5:
            rugs[i] = '"' + rug + '"'
            count_category = 0
        elif count_size == 5:
            rugs[i] = '"' + rug + '"'
            count_size = 0
        count_name += 1
        count_category += 1
        count_size += 1

    count_name = 4
    count_category = 3
    for i, w_f in enumerate(wall_floor):
        if count_name == 4:
            wall_floor[i] = w_f[0] + '"' + w_f[1:] + '"'
            count_name = 0
        elif count_category == 4:
            wall_floor[i] = '"' + w_f + '"'
            count_category = 0
        count_name += 1
        count_category += 1

    pieces = rugs + wall_floor
    pieces = ','.join(pieces)
    f.close()


    f = open("data/final/items.txt", "a")
    f.write(pieces)
    f.close()

convert_sql("data/lyrics saharah_items.txt")