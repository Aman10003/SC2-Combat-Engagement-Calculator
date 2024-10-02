import units_def as u
import reference as ref
import numpy as np
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


    def units_list(self):
        self.units_ref = ref.ref.units_list()
        

    def damage(self, attacker: u.unit, weapon: str, defender: u.unit, weapon_upgrade, splash = 1, prismatic = False):
        base_dam = attacker.weapon[weapon]
        ["dmg"[1]]
        #Fix bonus bamage calc
        if attacker.weapon['bonus'[3]] == defender:
            x=1
            bonus = attacker.weapon['bonus'[1]]
            bonus_scaling = attacker.weapon['bonus'[2]]
        else:
            bonus = 0
            bonus_scaling = 0
        # Damage Dealt: This is equal to (Base attack + Bonus damage + Attack upgrades)*Corrupted*Splash*Hallucinated*Prismatic.
        # Corrupted is removed
        #Need to add halucinated and prismatic calculations
        return (base_dam + bonus + (attacker.weapon['dmg'][2] + bonus_scaling) * weapon_upgrade) * splash
        
    def main():
        x=1
        
# Needs __mp_main__ for ui.run (must be run in multiprocessor)
if __name__ in {"__main__", "__mp_main__"}:
    # functions.main()
    # units_def.units
    units = functions.units_list()
    functions.gui()
    ui.run(port=8084)

