class Vertebrate:
    def __init__(self, backBone=True):
        self.has_backBone=backBone
    def vertebrate_info(self):
        print(f"Vertebrates have a backboon")

class Aquatic:
    def __init__(self, habitat="Water"):
        self.habitate=habitat
    def aquatric_info(self):
        print(f"Aquatic animals live in water")

class Fish(Vertebrate , Aquatic):
    def __init__(self, specie ,backbone=True, habitat="Water"):
        super().__init__(backbone=backbone)
        self.habitate=habitat
        self.species=species

     def fish_info(self):
         print(f"The {self.species} is a type of fish found in {self.habitate}")

     def swim(self):
         print(f"The fish is swimming")

goldfish=Fish("Golden Fish")
print(goldfish.has_backBone)
goldfish.swim()