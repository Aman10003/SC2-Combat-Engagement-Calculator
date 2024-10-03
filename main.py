import units_def as u
import reference as ref
from nicegui import ui
import math

class functions:
    def __init__(self) -> None:
        self.units_list()
        pass


    #Creates the gui to use
    def gui(self):
        # ui.label('Hello NiceGUI!')
        # ui.markdown("#Main")
        # Asks useer to select attacker, weapon, defender and upgrades
        ui.label('Attacker')
        attacker: u.unit = ui.select(self.units)
        ui.label('Weapon')
        weapon: u.unit.add_weapon = ui.select(attacker.weapon)
        ui.label('Attack Upgrade')
        weapons_upgrades = ui.toggle([0,1,2,3])
        ui.label('Defender')
        defender: u.unit = ui.select(self.units)
        ui.label('Armor Upgrade')
        armor_upgrade = ui.toggle([0,1,2,3])

        # Accounts for protoss shields and guardian shield
        if defender.race == 'protoss':
            ui.label('Shield Upgrade')
            shield_armor = ui.toggle([0,1,2,3])
            # Guardian Shield only works against ranged attacks
            if attacker.weapon[weapon]['ranged']:
                guardian_shield = ui.checkbox('Guardian Shield (+2 Armor)')
        # If the attcker is terran, enable seeker missle selections
        if attacker.race == 'terran':
            raven = ui.checkbox('Seeker Missle (+2 Armor)')
        # Ultralisk Chitinous Plating option
        if defender == 'Ultralisk':
            ultra_armor = ui.checkbox("Chitinous Plating (+2 Armor)")
        # Calculate pre armor damage
        pre_armor_damage = self.damage(attacker, weapon, defender, weapons_upgrades)
        # Calculate the effective armor and shield armor
        armor_mod = self.armor_calc(defender, armor_upgrade, raven, guardian_shield, ultra_armor)
        shield_armor_mod = self.shield_armor_calc(shield_armor, raven, guardian_shield)
        # Calculate damage post armor
        post_shield_armor_damage = self.post_armor_damage(pre_armor_damage, shield_armor_mod)
        post_armor_damage = self.post_armor_damage(pre_armor_damage, armor_mod)

        # TODO: Deal with weapon qty value
        # TODO: Perform weapon target check
        # TODO: Spell damage bypasses armor
        # Calculate shield shots to kill and time to kill
        leftover_damage = 0
        if defender.shield > 0:
            [htbs, leftover_damage] = self.htb(post_shield_armor_damage, defender.shield)
            if leftover_damage > 0:
                leftover_damage = leftover_damage - armor_mod
                if leftover_damage < 0.5:
                    leftover_damage = 0.5
            ui.label('Hits to break shields: %i hits', htbs)
            ttbs = self.ttk(htbs, weapon['cooldown'])
            ui.label('Time to break shields: %fs', ttbs)
        # Hits and time to kill
        htk = self.htk(post_armor_damage, defender.hp, leftover_damage)
        ui.label('Hits to kill: %i hits', htk)
        ttk = self.ttk(htk, weapon['cooldown'])
        ui.label('Time to kill: %fs', ttk)
        
        


    # Imports units stats
    def units_list(self):
        a = ref.ref()
        self.units = a.units_list()


        # self.units_ref = ref.ref()
        # self.units_ref.units_list()
        # self.units = self.units_list.units()

        # ref_instance = ref.ref()  # Create an instance of ref
        # print("Ref instance created:", ref_instance)
        
        # self.units_ref = ref_instance.units_list()  # Call units_list to get the units
        # print("Units ref:", self.units_ref)

        # self.units = self.units_ref  # Store the units in self.units
        # print("Units extracted:", self.units)



    # Hits to break shields
    # The leftover_damage calculation may be wrong. Liquidpedia isn't clear
    def htb(damage: float, shields: int):
        hits_to_break = math.ceil(shields / damage)
        leftover_damage = damage - (shields % damage)
        return [hits_to_break, leftover_damage]
        
        
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
    function_instance = functions()
    function_instance.units_list()
    function_instance.gui()
    ui.run(port=8084)

