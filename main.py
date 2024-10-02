import units_def as u
import reference as ref
from nicegui import ui

class functions:

    #Creates the gui to use
    def gui():
        # ui.label('Hello NiceGUI!')
        # ui.markdown("#Main")
        ui.label('Attacker')
        attacker: u.unit = ui.select(units)
        ui.label('Attack Upgrade')
        weapons_upgrades = ui.toggle([0,1,2,3])
        ui.label('Defender')
        defender: u.unit = ui.select(units)
        ui.label('Armor Upgrade')
        armor_upgrade = ui.toggle([0,1,2,3])
        if defender.race == 'protoss':
            ui.label('Shield Upgrade')
            shield_armor = ui.toggle([0,1,2,3])
            guardian_shield = ui.checkbox('Guardian Shield')
        if attacker.race == 'terran':
            raven = ui.checkbox('Seeker Missle')
        if defender == 'Ultralisk':
            ultra_armor = ui.checkbox("Ultra Armor")


    def units_list(self):
        self.units_ref = ref.ref.units_list()
        
    def ttk(self, attacker: u.unit, weapon: str, defender: u.unit, weapon_upgrade: int, armor_upgrade: int, shield_armor_upgrade = 0):
        # calculates attacks to kill
        # Does not work for shields yet
        hits_to_kill = defender.hp / self.damage(attacker)



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
    # TODO: Verifty Values
    def armor_mod(self, raven: bool = False, guardian_shield: bool = False, ultra_armor: bool = False):
        armor_mod = 0
        # Raven seeker missle
        if raven:
            armor_mod = armor_mod - 3
        # Snetry Guardian Shield
        if guardian_shield:
            armor_mod = armor_mod + 2
        # Ultra's carapace upgrade
        if ultra_armor:
            armor_mod = armor_mod + 3
        return armor_mod

    #Damage Calculations
    def damage(self, attacker: u.unit, weapon: str, defender: u.unit, weapon_upgrade: int, splash: float = 1, prismatic = False):
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
        
    def main():
        x=1
        
# Needs __mp_main__ for ui.run (must be run in multiprocessor)
if __name__ in {"__main__", "__mp_main__"}:
    # functions.main()
    # units_def.units
    units = functions.units_list()
    functions.gui()
    ui.run(port=8084)

