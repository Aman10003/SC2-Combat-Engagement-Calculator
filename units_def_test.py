import units_def as u

def test_unit_gen():
    units={'banshee':u.unit(140,race='terran', attr={'light':True,'mech':True}, ground=False)}
    units["banshee"].add_weapon('Backlash Rockets', 12, 1, 0.89, quantity=2, target='gnd')
    assert units["banshee"].hp == 140
    assert units['banshee'].armor == 0
    assert units['banshee'].race == 'terran'

def test_attr():
    units={'banshee':u.unit(140,race='terran', attr={'light':True,'mech':True}, ground=False)}
    units["banshee"].add_weapon('Backlash Rockets', 12, 1, 0.89, quantity=2, target='gnd')
    assert units['banshee'].attributes == {'light': True, 'armored': False, 'massive': False, 'bio': False, 'mech': True, 'psi': False, 'structure': False, 'heroic': False, 'gnd': False}



def test_weapon_add():
    units={'banshee':u.unit(140,race='terran', attr={'light':True,'mech':True}, ground=False)}
    units["banshee"].add_weapon('Backlash Rockets', 12, 1, 0.89, quantity=2, target='gnd')
    weapon_name = list(units['banshee'].weapon.keys())
    assert weapon_name == ['Backlash Rockets']
    print(units['banshee'].weapon[weapon_name[0]])

def test_weapon_stats():
    units={'banshee':u.unit(140,race='terran', attr={'light':True,'mech':True}, ground=False)}
    units["banshee"].add_weapon('Backlash Rockets', 12, 1, 0.89, quantity=2, target='gnd')
    weapon_name = list(units['banshee'].weapon.keys())
    assert units['banshee'].weapon[weapon_name[0]] == {'dmg': [12, 1], 'bonus': [0, 0, None], 'qty': 2, 'cooldown': 0.89, 'target': 'gnd', 'spell': False}