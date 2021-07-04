# Houseware -> Housewares
# Tool -> Tools
# Accessory -> Equipment
# Fence -> Other

def convert_categories(file_name):
    f = open(file_name, 'r')
    line = f.read()
    pieces = line.split(',')
    for i, piece in enumerate(pieces):
        if piece == "Houseware":
            pieces[i] = "Housewares"
        elif piece == "Tool":
            pieces[i] = "Tools"
        elif piece == "Accessory":
            pieces[i] = "Equipment"
        elif piece == "Fence":
            pieces[i] = "Other"
    pieces = ','.join(pieces)
    f.close()

    f = open("../data/missed_diy_changed.txt", "a")
    f.write(pieces)
    f.close()

convert_categories("../data/missed_diy.txt")