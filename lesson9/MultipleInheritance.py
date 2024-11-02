class Vertebrate:
    def __init__(self, backBone=True):
        self.has_backBone = backBone

    def vertebrate_info(self):
        print("Vertebrates have a backbone")


class Aquatic:
    def __init__(self, habitat="Water"):
        self.habitat = habitat  # Fixed variable name

    def aquatic_info(self):
        print("Aquatic animals live in water")


class Fish(Vertebrate, Aquatic):
    def __init__(self, species, backbone=True, habitat="Water"):
        Vertebrate.__init__(self, backBone=backbone)  # Use class name directly
        Aquatic.__init__(self, habitat=habitat)  # Call the parent class's init
        self.species = species  # Fixed variable name

    def fish_info(self):
        print(f"The {self.species} is a type of fish found in {self.habitat}")

    def swim(self):
        print("The fish is swimming")


goldfish = Fish("Goldfish")
print(goldfish.has_backBone)
goldfish.swim()