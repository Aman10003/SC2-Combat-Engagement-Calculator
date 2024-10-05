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
    def __init__(self, health, armor = 0, shield_armor = 0, shields = 0, race = None, ground = True, attr=None):
        # Merges attributes so that all ones that aren't true is false
        if attr is None:
            attr = self.default_attr()
        else:
            # Merge the provided attributes with the default ones
            default_attributes = self.default_attr()
            default_attributes.update(attr)  # Update defaults with provided attributes
            attr = default_attributes
        # Sets units stats
        self.armor = armor
        self.hp = health
        self.shield_armor = shield_armor
        self.shield = shields
        self.race = race
        self.attributes = attr
        self.weapon = {}
        self.ground = ground  
        
    def default_attr(self, light = False, armored = False, massive = False, bio = False, mech = False, psi = False, structure = False, heroic = False, ground = False):
        # return {"light" : light, "armored" : armored, "massive" : massive, "bio" : bio, "mech" : mech, "psi" : psi, "structure" : structure, "heroic" : heroic, "gnd" : ground}
        return {
            "light": light,
            "armored": armored,
            "massive": massive,
            "bio": bio,
            "mech": mech,
            "psi": psi,
            "structure": structure,
            "heroic": heroic,
            "gnd": ground
        }

    def add_weapon(self, name: str, damage: int, damage_scaling: int, cooldown: float, 
                   bonus_damage: int = 0, bonus_damage_attr: str = None, 
                   bonus_damage_scaling: int = 0, quantity: int = 1, 
                   target: str = None, spell: bool = False, ranged: bool = True):
        # Generates unit's weapon stats.
        self.weapon[name] = {
            'dmg': [damage, damage_scaling],
            'bonus': [bonus_damage, bonus_damage_scaling, bonus_damage_attr],
            'qty': quantity,
            'cooldown': cooldown,
            'target': target,
            'spell': spell,
            'ranged': ranged
        }



if __name__=='__main__':
    units={'Banshee':unit(140,race='terran', attr={'light':True,'mech':True}, ground=False)}
    units["Banshee"].add_weapon('Backlash Rockets', 12, 1, 0.89, quantity=2, target='gnd')
    print(units["Banshee"].hp)
    print(units['Banshee'].attributes)
    weapon_name = list(units['Banshee'].weapon.keys())
    print(weapon_name)
    print(units['Banshee'].weapon[weapon_name[0]])