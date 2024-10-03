import units_def as u
import reference as ref
from nicegui import ui
import math

class functions:

    #Creates the gui to use
    def gui(self):
        # ui.label('Hello NiceGUI!')
        # ui.markdown("#Main")
        ui.label('Attacker')
        attacker: u.unit = ui.select(units)
        ui.label('Weapon')
        weapon: u.unit.add_weapon = ui.select(attacker.weapon)
        ui.label('Attack Upgrade')
        weapons_upgrades = ui.toggle([0,1,2,3])
        ui.label('Defender')
        defender: u.unit = ui.select(units)
        ui.label('Armor Upgrade')
        armor_upgrade = ui.toggle([0,1,2,3])
        if defender.race == 'protoss':
            ui.label('Shield Upgrade')
            shield_armor = ui.toggle([0,1,2,3])
            # Guardian Shield only works against ranged attacks
            if attacker.weapon['ranged']:
                guardian_shield = ui.checkbox('Guardian Shield (+2 Armor)')
        if attacker.race == 'terran':
            raven = ui.checkbox('Seeker Missle (+2 Armor)')
        if defender == 'Ultralisk':
            ultra_armor = ui.checkbox("Chitinous Plating (+2 Armor)")
        pre_armor_damage = self.damage(attacker, weapon, defender, weapons_upgrades)
        armor_mod = self.armor_calc(defender, armor_upgrade, raven, guardian_shield, ultra_armor)
        shield_armor_mod = self.shield_armor_calc(shield_armor, raven, guardian_shield)
        post_shield_armor_damage = self.post_armor_damage(pre_armor_damage, shield_armor_mod)
        post_armor_damage = self.post_armor_damage(pre_armor_damage, armor_mod)
        leftover_damage = 0
        if defender.shield > 0:
            [htbs, leftover_damage] = self.htb(post_shield_armor_damage, defender.shield)
            if leftover_damage > 0:
                leftover_damage = leftover_damage - armor_mod
                if leftover_damage < 0.5:
                    leftover_damage = 0.5
            ui.label('Hits to break shields %i', htbs)
            ttbs = self.ttk
        htk = self.htk(post_armor_damage, defender.hp, leftover_damage)
        
        



    def units_list(self):
        self.units_ref = ref.ref.units_list()
        
    # Hits to break shields
    # The leftover_damage calculation may be wrong. Liquidpedia isn't clear
    def htb(damage: float, shields: int):
        hits_to_break = math.ceil(shields / damage)
        leftover_damage = damage - (shields % damage)
        
        
    # Hits to kill
    # TODO: Zerg regen
    def htk(damage: float, hp: int, leftover_damage: float):
        hp = hp - leftover_damage
        return math.ceil(hp / damage)

    def ttk(self, hits_to_kill: int, cooldown: float):
        # calculates attacks to kill
        # Does not work for shields yet
        return  hits_to_kill / cooldown


    #Functions to calculate armor
    # Calculated armor for hp
    def armor_calc(self, defender: u.unit, armor_upgrade: int, raven: bool = False, guardian_shield: bool = False, ultra_armor: bool = False):
        armor = defender.armor
        armor = armor + armor_upgrade
        armor = armor + self.armor_mod(raven, guardian_shield, ultra_armor)
        return armor
        
    # Calculates shield armor
    def shield_armor_calc(self, shield_armor_upgrade: int, raven: bool = False, guardian_shield: bool = False):
        return shield_armor_upgrade + self.armor_mod(raven, guardian_shield)

    # Generate armor modify value
    def armor_mod(self, raven: bool = False, guardian_shield: bool = False, ultra_armor: bool = False):
        armor_mod = 0
        # Raven seeker missle
        if raven:
            armor_mod = armor_mod - 2
        # Snetry Guardian Shield
        if guardian_shield:
            armor_mod = armor_mod + 2
        # Ultra's carapace upgrade
        if ultra_armor:
            armor_mod = armor_mod + 2
        return armor_mod

    # Pre mitigation-damage Calculations
    def damage(self, attacker: u.unit, weapon, defender: u.unit, weapon_upgrade: int, splash: float = 1, prismatic = False):
        base_dam = attacker.weapon[weapon]
        ["dmg"[1]]
        # TODO: Fix bonus bamage calc
        if attacker.weapon[weapon]['bonus'[3]] == defender.attributes:
            bonus = attacker.weapon[weapon]['bonus'[1]]
            bonus_scaling = attacker.weapon[weapon]['bonus'[2]]
        else:
            bonus = 0
            bonus_scaling = 0
        # Damage Dealt: This is equal to (Base attack + Bonus damage + Attack upgrades)*Corrupted*Splash*Hallucinated*Prismatic.
        # Corrupted is removed
        # TODO: Need to add halucinated and prismatic calculations
        return (base_dam + bonus + (attacker.weapon[weapon]['dmg'][2] + bonus_scaling) * weapon_upgrade) * splash
    # Post armor damage
    def post_armor_damage(self, damage, armor):
        post_armor_damage = damage - armor
        if post_armor_damage < 0.5:
            post_armor_damage = 0.5
        return post_armor_damage
        
    def main():
        x=1
        
# Needs __mp_main__ for ui.run (must be run in multiprocessor)
if __name__ in {"__main__", "__mp_main__"}:
    # functions.main()
    # units_def.units
    functions = functions
    units = functions.units_list()
    functions.gui()
    ui.run(port=8084)

