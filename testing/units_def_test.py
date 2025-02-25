import units_def as u


def test_unit_gen():
    units = {'Banshee': u.unit(140, race='terran', attr=u.Attributes(light=True, mech=True), ground=False)}
    units["Banshee"].add_weapon('Backlash Rockets', 12, 1, 0.89, quantity=2, target='gnd')
    assert units["Banshee"].hp == 140
    assert units['Banshee'].armor == 0
    assert units['Banshee'].race == 'terran'


def test_attr():
    units = {'Banshee': u.unit(140, race='terran', attr=u.Attributes(light=True, mech=True), ground=False)}
    units["Banshee"].add_weapon('Backlash Rockets', 12, 1, 0.89, quantity=2, target='gnd')
    assert units['Banshee'].attributes.light is True
    assert units['Banshee'].attributes.armored is False
    assert units['Banshee'].attributes.massive is False
    assert units['Banshee'].attributes.bio is False
    assert units['Banshee'].attributes.mech is True
    assert units['Banshee'].attributes.psi is False
    assert units['Banshee'].attributes.structure is False
    assert units['Banshee'].attributes.heroic is False
    assert units['Banshee'].attributes.ground is False


def test_weapon_add():
    units = {'Banshee': u.unit(140, race='terran', attr=u.Attributes(light=True, mech=True), ground=False)}
    units["Banshee"].add_weapon('Backlash Rockets', 12, 1, 0.89, quantity=2, target='gnd')
    weapon_name = list(units['Banshee'].weapon.keys())
    assert weapon_name == ['Backlash Rockets']


def test_weapon_damage():
    units = {'Banshee': u.unit(140, race='terran', attr=u.Attributes(light=True, mech=True), ground=False)}
    units["Banshee"].add_weapon('Backlash Rockets', 12, 1, 0.89, quantity=2, target='gnd')
    assert units['Banshee'].weapon['Backlash Rockets']['dmg'] == [12, 1]


def test_weapon_stats():
    units = {'Banshee': u.unit(140, race='terran', attr=u.Attributes(light=True, mech=True), ground=False)}
    units["Banshee"].add_weapon('Backlash Rockets', 12, 1, 0.89, quantity=2, target='gnd')
    weapon_name = list(units['Banshee'].weapon.keys())
    assert units['Banshee'].weapon[weapon_name[0]] == {'dmg': [12, 1], 'bonus': [0, 0, None], 'qty': 2,
                                                       'cooldown': 0.89, 'target': 'gnd', 'spell': False,
                                                       'ranged': True}
