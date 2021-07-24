

def convert_sql(arr):
    i = 0
    check = []
    while i < len(arr):
        elem1 = arr[i][1]
        # elem2 = arr[i][2]
        # elem3 = arr[i][3]
        if "'" in elem1:
            index = elem1.index("'")
            elem1 = elem1[:index] + "'" + elem1[index:]
            check.append(elem1)
        # if "'" in elem2:
        #     index = elem2.index("'")
        #     elem2 = elem2[:index] + "'" + elem2[index:]
        # if "'" in elem3:
        #     index = elem3.index("'")
        #     elem3 = elem3[:index] + "'" + elem3[index:]
        #
        arr[i] = (arr[i][0], elem1, arr[i][2], str(arr[i][3]), arr[i][4], arr[i][5], arr[i][6], arr[i][7])
        # arr[i] = (arr[i][0], arr[i][1], str(arr[i][2]))
        i += 1
    print(check)
    return arr




arr = [(1,"Seaweed",600,1,0,0,9,6),(2,"Sea Grapes",900,1,0,0,5,8),(3,"Sea Cucumber",500,1,0,0,10,3),(4,"Sea Pig",10000,1,16,9,10,1),(5,"Sea Star",500,1,0,0,0,0),(6,"Sea Urchin",1700,1,0,0,4,8),(7,"Slate Pencil Urchin",2000,1,16,9,4,8),(8,"Sea Anemone",500,1,0,0,0,0),(9,"Moon Jellyfish",600,1,0,0,6,8),(10,"Sea Slug",600,1,0,0,0,0),(11,"Pearl Oyster",2800,1,0,0,0,0),(12,"Mussel",1500,1,0,0,5,11),(13,"Oyster",1100,1,0,0,8,1),(14,"Scallop",1200,1,0,0,0,0),(15,"Whelk",1000,1,0,0,0,0),(17,"Abalone",2000,1,16,9,5,0),(18,"Gigas Giant Clam",15000,1,0,0,4,8),(20,"Octopus",1200,1,0,0,0,0),(22,"Vampire Squid",10000,1,16,9,4,7),(23,"Firefly Squid",1400,1,21,4,2,5),(24,"Gazami Crab",2200,1,0,0,5,10),(25,"Dungeoness Crab",1900,1,0,0,10,4),(26,"Snow Crab",6000,1,0,0,10,3),(27,"Red King Crab",8000,1,0,0,10,2),(28,"Acorn Barnacle",600,1,0,0,0,0),(29,"Spider Crab",10000,0,0,0,2,3),(30,"Tiger Prawn",3000,1,16,9,5,8),(31,"Sweet Shrimp",1400,1,16,9,8,1),(32,"Mantis Shrimp",2500,1,16,9,0,0),(33,"Spiny Lobster",3000,1,21,4,9,11),(36,"Horseshoe Crab",1500,1,21,4,6,8),(37,"Sea Pineapple",1500,1,0,0,3,7),(38,"Spotted Garden Eel",1100,1,4,21,4,9),(39,"Flatworm",200,1,16,9,7,8),(40,"Venus' Flower Basket",5000,1,0,0,9,1)]
print(convert_sql(arr))