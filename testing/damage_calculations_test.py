import damage_calculations as dmg
import units_def as u
import reference as ref


# TODO: Following is not checcked
# import math
# import units_def as u
#
# class damage_calculation():
#     def ttk(hits_to_kill: int, cooldown: float):
#     def damage(self, weapon, defender: u.unit, weapon_upgrade: int,


def test_armor_mod():
    # Tests not flags
    assert dmg.damage_calculation.armor_mod(False, False, False) == 0
    # Tests each flag individually
    assert dmg.damage_calculation.armor_mod(True, False, False) == -2
    assert dmg.damage_calculation.armor_mod(False, True, False) == 2
    assert dmg.damage_calculation.armor_mod(False, False, True) == 2
    # Tests all flags together
    assert dmg.damage_calculation.armor_mod(True, True, True) == 2


def test_armor_calc():
    units = {}
    units['test'] = u.unit(140, armor=0)
    units['test2'] = u.unit(140, armor=2)
    damage = dmg.damage_calculation()
    # Tests units armor return
    assert damage.armor_calc(units['test'], 0) == 0
    assert damage.armor_calc(units['test2'], 0) == 2
    # Tests armor upgrades
    assert damage.armor_calc(units['test'], 2) == 2
    assert damage.armor_calc(units['test2'], 2) == 4
    # Tests flags
    assert damage.armor_calc(units['test'], 0, raven=True, guardian_shield=True) == 0
    assert damage.armor_calc(units['test2'], 0, raven=True) == 0
    assert damage.armor_calc(units['test'],2, ultra_armor=True) == 4


def test_post_armor_damage():
    damage = dmg.damage_calculation()
    assert damage.post_armor_damage(1,0) == 1
    assert damage.post_armor_damage(10,5) == 5
    assert damage.post_armor_damage(5,5) == 0.5
    assert damage.post_armor_damage(5,-2) == 7
    assert damage.post_armor_damage(0,2) == 0.5


def test_shield_armor():
    units = {}
    units['test'] = u.unit(140, armor=0)
    units['test2'] = u.unit(140, armor=2)
    damage = dmg.damage_calculation()
    # Tests units armor return
    assert damage.armor_calc(units['test'], 0) == 0
    assert damage.armor_calc(units['test2'], 0) == 2
    # Tests armor upgrades
    assert damage.armor_calc(units['test'], 2) == 2
    assert damage.armor_calc(units['test2'], 2) == 4
    # Tests flags
    assert damage.armor_calc(units['test'], 0, raven=True, guardian_shield=True) == 0
    assert damage.armor_calc(units['test2'], 0, raven=True) == 0
    assert damage.armor_calc(units['test'], 2, guardian_shield=True) == 4


def test_htb():
    damage = dmg.damage_calculation()
    # Check base damage without armor and mod is 0
    assert damage.htb(10,10,0) == [1,0]
    # Check armor effect
    assert damage.htb(10, 10, 5) == [2, 0]
    # Check the leftover damage and make sure armor works out the same
    assert damage.htb(3, 10, 0) == [4, 2]
    assert damage.htb(10, 10, 7) == [4, 2]


def test_htk():
    damage = dmg.damage_calculation()
    # Check base damage return
    assert damage.htk(10, 10, 0) == 1
    assert damage.htk(30, 10, 0) == 1
    # Check Armor effect
    assert damage.htk(10, 10, 5) == 2
    # Check armor effect if armor => damage
    assert damage.htk(10,10,10) == 20
    assert damage.htk(10,30,5) == 6


def test_ttk():
    assert dmg.damage_calculation.ttk(10,1) == 10
    assert dmg.damage_calculation.ttk(10,5) == 50
    assert dmg.damage_calculation.ttk(10, 0.1) == 1
    assert dmg.damage_calculation.ttk(10, 0.25) == 2.5


def test_damage():
    a = ref.Ref()
    damage = dmg.damage_calculation()
    units = a.units_list()
    attacker_name = 'Banshee'
    attacker = units[attacker_name]
    weapon_select = 'Backlash Rockets'
    weapon: u.unit.add_weapon = attacker.weapon.get(weapon_select)
    defender_name = 'Marine'
    defender = units[defender_name]
    assert damage.damage(weapon, defender,0) == 12

    pass
