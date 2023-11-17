from harvest import Melon, make_melon_type_lookup, make_melon_types, get_sellability_report


def open_and_read_file(file_path):
    """Open and read the file"""


    with open (file_path) as file:
        content = file.read().rstrip().split("\n")


    return content



def create_melons_report(melons):
    """Create melons"""

    
    melons_report = []
    
    for item in melons:
        data = item.split(" ")

        shape = int(data[1])
        color = int(data[3])
        type = data[5]
        harvested_by = data[8]
        field = int(data[-1])

        melon = Melon(
            melon_type = type,
            shape_rating = shape,
            color_rating = color,
            field = field,
            harvested_by = harvested_by 
        )

        melons_report.append(melon) 

    return melons_report    



data_from_file = open_and_read_file("harvest_log.txt")
 
melon_types = make_melon_types()
melons_by_id = make_melon_type_lookup(melon_types)
print(get_sellability_report(create_melons_report(data_from_file)))

