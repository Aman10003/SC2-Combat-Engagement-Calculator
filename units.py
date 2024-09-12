# class attribute:
#     def __init__(self, l = False, arm = False, mass = False, bio = False, mech = False, psi = False, structure = False, heroic = False):
#         self.light = l
#         self.armored = arm
#         self.massive = mass
#         self.bio = bio
#         self.mech = mech
#         self.psi = psi
#         self.structure = structure
#         self.heroic = heroic

class unit:
    def __init__(self, armor, health, shields = 0, attr={"light" : False, "armored" : False, "massive" : False, "bio" : False, "mech" : False, "psi" : False, "structure" : False, "heroic" : False, "gnd" : False, "race": None}):
        self.armor = armor
        self.hp = health
        self.shield = shields
        self.attributes = attr