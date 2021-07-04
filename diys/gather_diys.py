import equipment, fences, housewares, miscellaneous, others, tools, wall_floor_rugs, wall_mounts

def gather_diys():
    diy = dict()

    diy["Accessory"] = equipment.get_accessories()
    diy["Fence"] = fences.get_fences()
    diy["Houseware"] = housewares.get_housewares()
    diy["Miscellaneous"] = miscellaneous.get_misc()
    diy["Other"] = others.get_others()
    diy["Tool"] = tools.get_tools()
    diy["Wall/Floor/Rug"] = wall_floor_rugs.get_wall_floor_rugs()
    diy["Wall-Mounted"] = wall_mounts.get_wall_mounts()

    return diy

def create_file():
    diy = gather_diys()
    f = open("../data/diy.txt", "a")
    for key in diy:
        for item in diy[key]:
            query = "(" + item + "," + key + "," + "0" + "," + "0" + ")" + ","
            f.write(query)
    f.close()

create_file()