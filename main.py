import math
from nicegui import ui
import units_def as u
import reference as ref
import damage_calculations as dmg
class functions:
    def __init__(self) -> None:
        # Generates list of units
        self.units_list()
        # Attacker and defender definition
        self.attacker = None
        self.defender = None
        self.weapon_select = None
        # Defines Gui elements
        self.shield_label = None
        self.shield_armor = None
        self.guardian_shield = None
        self.ultra_armor = None
        pass

    # Creates the gui to use
    def gui(self):
        # ui.label('Hello NiceGUI!')

        # Asks user to select attacker, weapon, defender and upgrades
        ui.label('Attacker')
        # Use unit names (keys from self.units) for selection, which are serializable
        attacker_name = ui.select(list(self.units.keys()), on_change=self.attacker_update)
        # Map selected attacker name back to actual unit objects
        self.attacker: u.unit = self.units.get(attacker_name)
        ui.label('Weapon')
        # Placeholder for weapon selection, initially empty
        self.weapon_select = ui.select([], label='Choose Weapon')
        ui.label('Attack Upgrade')
        weapons_upgrades = ui.toggle([0,1,2,3])
        ui.label('Defender')
        defender_name = ui.select(list(self.units.keys()))  # Use the same unit list for defender
        self.shield_label = ui.label('Shield Upgrade')
        self.shield_armor = ui.toggle([0,1,2,3])
        ui.label('Armor Upgrade')
        armor_upgrade = ui.toggle([0,1,2,3])
        self.guardian_shield = ui.checkbox('Guardian Shield (+2 Armor)')
        self.ultra_armor = ui.checkbox("Chitinous Plating (+2 Armor)")

        # Map selected defender name back to actual unit objects
        self.defender: u.unit = self.units.get(defender_name)

        # TODO: Move logic to routine
        # Ensure defender is not None before accessing its attributes
        if self.defender is not None:
            pass
        else:
            print(f"Defender '{defender_name}' not found in unit list.")

        # TODO: Move logic to routine
        if self.attacker is not None:
            # If the attacker is terran, enable seeker missile selections
            if self.attacker.race == 'terran':
                raven = ui.checkbox('Seeker Missile (+2 Armor)')
            else:
                raven = False
        else:
            print(f"Defender '{defender_name}' not found in unit list")

        # TODO: Move to damage_calc
        if self.attacker is not None and self.defender is not None:
            # Calculate pre armor damage
            pre_armor_damage = dmg.damage_calculation.damage(self.attacker, self.weapon_select, self.defender, weapons_upgrades)
            # Calculate the effective armor and shield armor
            armor_mod = dmg.damage_calculation.armor_calc(self.defender, armor_upgrade, raven.value, self.guardian_shield.value, self.ultra_armor.value)
            shield_armor_mod = dmg.damage_calculation.shield_armor_calc(self.shield_armor.value, raven.value, self.guardian_shield.value)
            # Calculate damage post armor
            post_shield_armor_damage = dmg.damage_calculation.post_armor_damage(pre_armor_damage, shield_armor_mod)
            post_armor_damage = dmg.damage_calculation.post_armor_damage(pre_armor_damage, armor_mod)

            # TODO: Deal with weapon qty value
            # TODO: Perform weapon target check
            # TODO: Spell damage bypasses armor
            # Calculate shield shots to kill and time to kill
            leftover_damage = 0
            if self.defender.shield > 0:
                [htbs, leftover_damage] = self.htb(post_shield_armor_damage, self.defender.shield)
                if leftover_damage > 0:
                    leftover_damage = leftover_damage - armor_mod
                    if leftover_damage < 0.5:
                        leftover_damage = 0.5
                ui.label(f"Hits to break shields: '{htbs}' hits")
                ttbs = dmg.damage_calculation.ttk(htbs, self.attacker.weapon['cooldown'])
                ui.label(f"Time to break shields: '{ttbs}")
            # Hits and time to kill
            htk = dmg.damage_calculation.htk(post_armor_damage, self.defender.hp, leftover_damage)
            ui.label(f"Hits to kill: '{htk}' hits")
            ttk = dmg.damage_calculation.ttk(htk, self.weapon_select['cooldown'])
            ui.label(f"Time to kill: '{ttk}'")
        else:
            print(f"Attacker '{attacker_name}' not found in unit list and Defender '{defender_name}' not found in unit list")

    def attacker_update(self, event):
        self.update_weapon_options(event)

    # Event handler to update weapon selection based on the chosen attacker
    def update_weapon_options(self, event):
        attacker_name = event.value
        attacker: u.unit = self.units.get(attacker_name)
        if attacker and attacker.weapon:
            # Update weapon select options with the keys from attacker's weapon dictionary
            self.weapon_select.options = list(attacker.weapon.keys())
            self.weapon_select.update()  # Refresh the dropdown to reflect the cleared state           
        else:
            # If no weapons are available, clear the weapon options
            self.weapon_select.options = []
            self.weapon_select.update()  # Refresh the dropdown to reflect the cleared state

    def defender_update(self, event):
        defender_name = event.value
        self.defender: u.unit = self.units.get(defender_name)
        # Accounts for protoss shields and guardian shield
        if self.defender.race == 'protoss':
            self.shield_label.visible = True
            self.shield_armor.visible = True
            # Guardian Shield only works against ranged attacks
            if self.attacker.weapon[self.weapon_select]['ranged']:
                self.guardian_shield.visible = True
            else:
                self.guardian_shield.visible = False
                self.guardian_shield.value = False
        else:
            self.shield_label.visible = False
            self.shield_armor.visible = False
            self.shield_armor.value = 0
            self.guardian_shield.visible = False
            self.guardian_shield.value = False
        # Ultralisk Chitinous Plating option
        if self.defender == 'Ultralisk':
            self.ultra_armor.visible = True
        else:
            self.ultra_armor.visible = False
            self.ultra_armor.value = False

    # Imports units stats
    def units_list(self):
        a = ref.Ref()
        self.units = a.units_list()



    def main(self):
        function_instance = functions()
        function_instance.units_list()
        function_instance.gui()
        ui.run(port=8084)


# Needs __mp_main__ for ui.run (must be run in multiprocessor)
if __name__ in {"__main__", "__mp_main__"}:
    # functions.main()
    # units_def.units
    fun = functions()
    fun.main()
