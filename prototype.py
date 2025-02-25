class Attributes:
    def __init__(self, light: bool = False, armored: bool = False, massive: bool = False, 
                 bio: bool = False, mech: bool = False, psi: bool = False, 
                 structure: bool = False, heroic: bool = False, ground: bool = False):
        self.light = light
        self.armored = armored
        self.massive = massive
        self.bio = bio
        self.mech = mech
        self.psi = psi
        self.structure = structure
        self.heroic = heroic
        self.ground = ground

class Unit:
    def __init__(self, health: int, armor: int = 0, shield_armor: int = 0, shields: int = 0, 
                 race: str = None, ground: bool = True, attr: Attributes = None):
        self.attributes = attr if attr else self.default_attr()
        self.armor = armor
        self.hp = health
        self.shield_armor = shield_armor
        self.shield = shields
        self.race = race
        self.ground = ground  
        self.weapon = {}

    def default_attr(self) -> Attributes:
        # Returns default attributes.
        return Attributes()

    def add_weapon(self, name: str, damage: int, damage_scaling: float, cooldown: float, 
                   bonus_damage: int = 0, bonus_damage_attr: Attributes = None, 
                   bonus_damage_scaling: float = 0, quantity: int = 1, 
                   target: str = None, spell: bool = False):
        # Generates unit's weapon stats.
        self.weapon[name] = {
            'dmg': [damage, damage_scaling],
            'bonus': [bonus_damage, bonus_damage_scaling, bonus_damage_attr],
            'qty': quantity,
            'cooldown': cooldown,
            'target': target,
            'spell': spell
        }

if __name__ == '__main__':
    units = {'banshee': Unit(140, race='terran', attr=Attributes(light=True, mech=True), ground=False)}
    units["banshee"].add_weapon('Backlash Rockets', 12, 1, 0.89, quantity=2, target='gnd')
    
    # Display unit stats
    print(units["banshee"].hp)
    print(vars(units['banshee'].attributes))  # Use vars to print attributes as a dictionary
    print(units['banshee'].attributes.light)
    weapon_name = list(units['banshee'].weapon.keys())
    print(weapon_name)
    print(units['banshee'].weapon[weapon_name[0]])