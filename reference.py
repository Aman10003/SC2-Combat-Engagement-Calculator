import units_def as u


class ref:
    def __init__(self) -> None:
        self.units_list()
        pass

    # Reference list of all
    def units_list(self):
        self.units={}
        # Terran
        # Banshee
        self.units['Banshee'] = u.unit(140,race='terran', attr=u.Attributes(light=True, mech=True), ground=False)
        self.units["Banshee"].add_weapon('Backlash Rockets', 12, 1, 0.89, quantity=2, target='gnd')
        # Marine
        self.units['Marine'] = u.unit(45, race='terran', attr=u.Attributes(light=True, bio=True))
        self.units["Marine"].add_weapon("Guass Rifle", 6, 1, 0.61, target="both")
        # Marauder
        self.units['Marauder'] = u.unit(45, race='terran', attr=u.Attributes(armored=True, bio=True))
        self.units['Marauder'].add_weapon("Punisher Grenades", 10, 1, 1.07, 10, u.Attributes(armored=True), 1, target="gnd")

        # Protoss
        # Adept
        self.units['Adept'] = u.unit(70, 1, 1, 70, race='protoss', attr=u.Attributes(light=True, bio=True))
        self.units['Adept'].add_weapon('Glaive Cannon', 10, 1, 1.61, 12, u.Attributes(light=True), 1, target='gnd')
        # Zerg
        # Ultralisk
        return self.units
        
        
    #Function is used for internal testing only
    def main(self):
        # self.units_list()
        print(self.units["Banshee"].hp)
        weapon_name = list(self.units['Banshee'].weapon.keys())
        print(weapon_name)
        print(self.units['Banshee'].weapon[weapon_name[0]])
        


if __name__=='__main__':
   r=ref()
   r.main()
    