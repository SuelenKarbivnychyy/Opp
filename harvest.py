############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color        
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

    def __repr__(self):

        return self.code
    # def __repr__(self):
    #     """Show info about Melon"""

    #     return f" First_harvest- {self.first_harvest}\nColor- {self.color}\nis_seedless- {self.is_seedless}\nis_bestseller- {self.is_bestseller}\nname- {self.name} "           

        

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

        

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        

        self.new_code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    melon1 = MelonType(
        code = "musk",
        first_harvest = 1998,
        color = "green",        
        is_seedless = True,
        is_bestseller = True,
        name = "Muskmelon"
    )

    melon2 = MelonType(
        code = "cas",
        first_harvest = 2003,
        color = "orange",        
        is_seedless = False,
        is_bestseller = False,
        name = "Casaba"
    )

    melon3 = MelonType(
        code = "cren",
        first_harvest = 1996,
        color = "green",
        is_seedless = False,
        is_bestseller = False,
        name = "Crenshaw"
    )

    melon4 = MelonType(
        code = "yw",
        first_harvest = 2013,
        color = "yellow",
        is_seedless = False,
        is_bestseller = True,
        name = "Yellow Watermelon"
    )
    
    all_melon_types.append(melon1)
    all_melon_types.append(melon2)
    all_melon_types.append(melon3)
    all_melon_types.append(melon4)
    melon1.add_pairing("Mint")
    melon2.add_pairing("Strawberries")
    melon2.add_pairing("Mint")
    melon3.add_pairing("Prosciutto")
    melon4.add_pairing("Ice cream")


    return all_melon_types

melons = make_melon_types()


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""


    for item in melon_types:        
        print(f"{item.name} pair well with:")
        for match in item.pairings:
            print(f"- {match}")
        print("\n")    
           
            

# print_pairing_info(make_melon_types())



def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes objects and returns a dictionary of melon type by code."""

    melons = {}

    for melon in melon_types:
        melons[melon.code] = melon
    # print(melons)    
  

    return melons


  



############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods

    def __init__(
        self, melon_type, shape_rating, color_rating, field, harvested_by
        ):

        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.harvested_by = harvested_by 

    def __repr__(self):

        return f"\n\n- Melon type: {self.melon_type}\n- Shape rating: {self.shape_rating}\n- Color rating: {self.color_rating}\n- Harvested from field {self.field}\n- Harvested by {self.harvested_by}"        


    def is_sellable(self):
        """
        Return True if a melon is sellable or False otherwise.
        A melon is sellable if it's shape and color ratings are greater than 5, and it didnt came from field 3.
        """

        if self.shape_rating > 5 and self.color_rating > 5 and self.field != 3:
            return True
        
        return False




def make_melons(melon_types):
    """Returns a list of Melon objects."""

    melons = []

    melon_id = make_melon_type_lookup(melon_types)


    melon1 = Melon(
        melon_type = melon_id["yw"],
        shape_rating = 8,
        color_rating = 7,
        field = 2,
        harvested_by = "sheila"
    )

    melon2 = Melon(
        melon_type = melon_id["yw"],
        shape_rating = 3,
        color_rating = 4,
        field = 2,
        harvested_by = "sheila"
    )

    melon3 = Melon(
        melon_type = melon_id["yw"],
        shape_rating = 9,
        color_rating = 8,
        field = 3,
        harvested_by = "sheila"
    )

    melon4 = Melon(
        melon_type = melon_id["cas"],
        shape_rating = 10,
        color_rating = 6,
        field = 35,
        harvested_by = "sheila"
    )

    melon5 = Melon(
        melon_type = melon_id["cren"],
        shape_rating = 8,
        color_rating = 9,
        field = 35,
        harvested_by = "Michael"
    )

    melon6 = Melon(
        melon_type = melon_id["cren"],
        shape_rating = 8,
        color_rating = 2,
        field = 35,
        harvested_by = "Michael"
    )

    melon7 = Melon(
        melon_type = melon_id["cren"],
        shape_rating = 2,
        color_rating = 3,
        field = 4,
        harvested_by = "Michael"
    )

    melon8 = Melon(
        melon_type = melon_id["musk"],
        shape_rating = 6,
        color_rating = 7,
        field = 4,
        harvested_by = "Michael"
    )

    melon9 = Melon(
        melon_type = melon_id["yw"],
        shape_rating = 7,
        color_rating = 10,
        field = 3,
        harvested_by = "Sheila"
    )

    all_melons = (melon1, melon2, melon3, melon4, melon5, melon6, melon7, melon8, melon9)
    melons.extend(all_melons)

    return melons

harvested_melons = make_melons(melons)



def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    
    for melon in melons:
        if melon.is_sellable():
            print(f"Harvested by {melon.harvested_by} from Field {melon.field} (CAN BE SOLD)")
        else:
            print(f"Harvested by {melon.harvested_by} from Field {melon.field} (NOT SELLABLE)")    

# get_sellability_report(harvested_melons)




