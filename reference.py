import units_def as u


class ref:
    def __init__(self) -> None:
        self.units_list()
        pass
    def units_list(self):
        self.units={}
        # Banshee
        self.units['banshee'] = u.unit(140,race='terran', attr={'light':True,'mech':True}, ground=False)
        self.units["banshee"].add_weapon('Backlash Rockets', 12, 1, 0.89, quantity=2, target='gnd')
        # Marine
        self.units['Marine'] = u.unit(45, race='terran')
        # Marauder
        
    def main(self):
        # units = {'banshee':u.unit(140,race='terran', attr={'light':True,'mech':True}, ground=False)}
        # units["banshee"].add_weapon('Backlash Rockets', 12, 1, 0.89, quanity=2, target='gnd')
        # self.units_list()
        print(self.units["banshee"].hp)
        weapon_name = list(self.units['banshee'].weapon.keys())
        print(weapon_name)
        print(self.units['banshee'].weapon[weapon_name[0]])
        


if __name__=='__main__':
   r=ref()
   r.main()
    