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
    def __init__(self, health, armor = 0, sheild_armor = 0, shields = 0, race = None, ground = True, attr={"light" : False, "armored" : False, "massive" : False, "bio" : False, "mech" : False, "psi" : False, "structure" : False, "heroic" : False, "gnd" : False}):
        self.armor = armor
        self.hp = health
        self.shield_armor = sheild_armor
        self.shield = shields
        self.race = race
        self.attributes = attr
        self.weapon = {}
        self.ground = ground  
        


    def weapons(self, name, damage, damage_scaling, cooldown, bonus_damage = 0, bonus_damage_attr = None, bonus_damage_scaling = 0, quanity = 1, target = None, spell = False):
        self.weapon[name] = {'dmg':[damage, damage_scaling], 'bonus':[bonus_damage,bonus_damage_scaling,bonus_damage_attr], 'qty': quanity, 'cooldown':cooldown, 'target':target, 'spell':spell}
        
    


if __name__=='__main__':
    units={'banshee':unit(140,race='terran', attr={'light':True,'mech':True})}
    units["banshee"].weapons('Backlash Rockets', 12, 1, 0.89, quanity=2)
    print(units["banshee"].hp)
    weapon_name = list(units['banshee'].weapon.keys())
    print(weapon_name)
    print(units['banshee'].weapon[weapon_name[0]])