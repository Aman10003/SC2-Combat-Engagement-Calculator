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
    def __init__(self, health, armor = 0, sheild_armor = 0, shields = 0, race = None, attr={"light" : False, "armored" : False, "massive" : False, "bio" : False, "mech" : False, "psi" : False, "structure" : False, "heroic" : False, "gnd" : False}):
        self.armor = armor
        self.hp = health
        self.shield_armor = sheild_armor
        self.shield = shields
        self.race = race
        self.attributes = attr

    def weapons(self):
        self.weapon
    


if __name__=='__main__':
    units={'banshee':unit(140,race='terran', attr={'light':True,'mech':True})}
    print(units["banshee"].hp)