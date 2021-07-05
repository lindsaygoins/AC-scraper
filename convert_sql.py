

def convert_sql(file_name):
    f = open(file_name, 'r')
    line = f.read()
    pieces = line.split(',')
    count_name = 3
    count_category = 2
    for i, piece in enumerate(pieces):
        if count_name == 3:
            pieces[i] = piece[0] + "'" + piece[1:] + "'"
            count_name = 0
        elif count_category == 3:
            pieces[i] = "'" + piece + "'"
            count_category = 0
        count_name += 1
        count_category += 1
    pieces = ','.join(pieces)
    f.close()

    f = open("data/final/flowers.txt", "a")
    f.write(pieces)
    f.close()

convert_sql("data/final/final_flowers.txt")