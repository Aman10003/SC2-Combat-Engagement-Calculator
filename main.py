import math
from nicegui import ui
import units_def as u
import reference as ref
import damage_calculations as dmg


class functions:
    def __init__(self) -> None:
        # Generates list of units
        self.units = None
        self.units_list()
        # Attacker and defender definition
        self.attacker_name = None
        self.defender_name = None
        self.attacker = None
        self.defender = None
        self.weapon_select = None
        self.weapon = None
        # Defines Gui elements
        self.raven = None
        self.shield_label = None
        self.shield_armor = None
        self.guardian_shield = None
        self.ultra_armor = None
        self.stimpack = None
        self.combat_shield = None
        self.stimpack_damage = None
        self.roach_burrow = None
        # Armor and weapons upgrades
        self.weapons_upgrades = None
        self.armor_upgrade = None
        # Results Output
        self.htbs_label = None
        self.ttbs_label = None
        self.htk_label = None
        self.ttk_label = None
        self.damage_calc = dmg.damage_calculation()
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
        self.weapon_select = ui.select([], label='Choose Weapon', on_change=self.weapon_update)
        ui.label('Attack Upgrade')
        self.weapons_upgrades = ui.toggle([0,1,2,3], on_change=self.damage_update, value=0)
        # TODO: Figure out best way to declare stimpack
        self.stimpack = ui.checkbox('Stimpack: Attack Time -50% ', on_change=self.damage_update)
        self.raven = ui.checkbox('Seeker Missile (-3 Armor)', on_change=self.damage_update)
        ui.label('Defender')
        defender_name = ui.select(list(self.units.keys()), on_change=self.defender_update)
        self.shield_label = ui.label('Shield Upgrade')
        self.shield_armor = ui.toggle([0,1,2,3], on_change=self.damage_update, value=0)
        ui.label('Armor Upgrade')
        self.armor_upgrade = ui.toggle([0,1,2,3], on_change=self.damage_update, value=0)
        self.combat_shield = ui.checkbox('Combat Shield (+10 HP)', on_change=self.damage_update)
        self.stimpack_damage = ui.checkbox('Stimpack Damage', on_change=self.damage_update)
        self.guardian_shield = ui.checkbox('Guardian Shield (+2 Armor)', on_change=self.damage_update)
        self.ultra_armor = ui.checkbox('Chitinous Plating (+2 Armor)', on_change=self.damage_update)

        # Map selected defender name back to actual unit objects
        self.defender: u.unit = self.units.get(defender_name)

        self.htbs_label = ui.label()
        self.ttbs_label = ui.label()
        self.htk_label = ui.label()
        self.ttk_label = ui.label()

    def attacker_update(self, event):
        self.attacker_name = event.value
        self.attacker: u.unit = self.units.get(self.attacker_name)
        # Sets flag for stimpack
        if self.attacker_name == 'Marine' or self.attacker_name == 'Marauder':
            self.stimpack.visible = True
            if self.attacker_name == 'Marine':
                self.stimpack.text = 'Stimpack: Attack Time -0.203'
            else:
                self.stimpack.text = 'Stimpack: Attack Time -0.36'
        else:
            self.stimpack.visible = False
            self.stimpack.value = False
        # If the attacker is terran, enable seeker missile selections
        if self.attacker.race == 'terran':
            self.raven.visible = True
        else:
            self.raven.visible = False
            self.raven.value = False
        self.update_weapon_options(self.attacker)
        self.damage_update()

    # Event handler to update weapon selection based on the chosen attacker
    def update_weapon_options(self, attacker):
        if attacker and attacker.weapon:
            # Update weapon select options with the keys from attacker's weapon dictionary
            self.weapon_select.options = list(attacker.weapon.keys())
            print(list(attacker.weapon.keys()))
            # self.weapon_select.value = list(attacker.weapon.keys())[0]
            self.weapon_select.update()  # Refresh the dropdown to reflect the cleared state
        else:
            # If no weapons are available, clear the weapon options
            self.weapon_select.options = []
            print('now weapons')
            self.weapon_select.update()  # Refresh the dropdown to reflect the cleared state

    def weapon_update(self, event):
        self.weapon: u.unit.add_weapon = self.attacker.weapon.get(event.value)
        # self.weapon = event.value
        self.damage_update()

    def defender_update(self, event):
        self.defender_name = event.value
        self.defender: u.unit = self.units.get(self.defender_name)
        # Accounts for protoss shields and guardian shield
        if self.defender.race == 'protoss':
            self.shield_label.visible = True
            self.shield_armor.visible = True
            self.guardian_shield.visible = True
            # TODO: add range attack detection logic
            # # Guardian Shield only works against ranged attacks
            # if self.attacker is not None and self.attacker.weapon is not None:
            #     if self.attacker.weapon[self.weapon_select]['ranged']:
            #         self.guardian_shield.visible = True
            #     else:
            #         self.guardian_shield.visible = False
            #         self.guardian_shield.value = False
        else:
            self.shield_label.visible = False
            self.shield_armor.visible = False
            self.shield_armor.value = 0
            self.guardian_shield.visible = False
            self.guardian_shield.value = False

        # Sets flag to calculated damage if using stimpack
        if self.defender_name == 'Marine' or self.defender_name == 'Marauder':
            self.stimpack_damage.visible = True
            if self.defender_name == 'Marine':
                self.combat_shield.visible = True
                self.stimpack_damage.text = 'Stimpack: Health - 10'
            else:
                self.combat_shield.visible = False
                self.combat_shield.value = False
                self.stimpack_damage.text = 'Stimpack: Health - 20'
        else:
            self.combat_shield.visible = False
            self.combat_shield.value = False
            self.stimpack_damage.visible = False
            self.stimpack_damage.value = False
        # Ultralisk Chitinous Plating option
        if self.defender_name == 'Ultralisk':
            self.ultra_armor.visible = True
        else:
            self.ultra_armor.visible = False
            self.ultra_armor.value = False
        self.damage_update()

    # TODO: Maybe move most self.damage_calc to dmg.damage_calc for static methods
    def damage_update(self):
        if self.attacker is not None and self.defender is not None and self.weapon is not None:
            target = self.weapon['target']
            if target == 'both' or target == 'air' and self.defender.ground is False or target == 'gnd' and self.defender is True:
                # Calculate pre armor damage
                pre_armor_damage = self.damage_calc.damage(self.weapon, self.defender, self.weapons_upgrades.value, splash=self.weapon['splash'])
                # Calculate the effective armor and shield armor
                armor_mod = self.damage_calc.armor_calc(self.defender, self.armor_upgrade.value, self.raven.value,
                                                        self.guardian_shield.value, self.ultra_armor.value)
                shield_armor_mod = self.damage_calc.shield_armor_calc(self.shield_armor.value, self.raven.value,
                                                                      self.guardian_shield.value)
                # Calculate damage post armor(Not needed anymore)
                # post_shield_armor_damage = self.damage_calc.post_armor_damage(pre_armor_damage, shield_armor_mod)
                # post_armor_damage = self.damage_calc.post_armor_damage(pre_armor_damage, armor_mod)

                cooldown = self.weapon['cooldown']
                # Change Cooldown if stimpack is enabled
                if self.stimpack:
                    # Literal interpretation
                    fire_rate = cooldown ** -1
                    fire_rate = fire_rate * 1.5
                    cooldown = fire_rate ** -1

                # TODO: Deal with weapon qty value
                # TODO: Perform weapon target check
                # TODO: Spell damage bypasses armor
                # Calculate shield shots to kill and time to kill
                leftover_damage = 0
                if self.defender.shield > 0:
                    [htbs, leftover_damage] = self.damage_calc.htb(pre_armor_damage, self.defender.shield, armor_mod)
                    if leftover_damage > 0:
                        leftover_damage = leftover_damage - armor_mod
                        if leftover_damage < 0.5:
                            leftover_damage = 0.5
                    ttbs = self.damage_calc.ttk(htbs, cooldown)
                    self.htbs_label.visible = True
                    self.ttbs_label.visible = True
                    self.htbs_label.text = f"Hits to break shields: {htbs} hits"
                    self.ttbs_label.text = f"Time to break shields: {ttbs}s"
                else:
                    self.htbs_label.visible = False
                    self.ttbs_label.visible = False
                # Hits and time to kill
                # Calculates HP while accounting for stimpacks
                hp = self.defender.hp
                if self.combat_shield:
                    hp = hp + 10
                if self.stimpack_damage:
                    if self.defender_name == 'Marine':
                        hp = hp - 10
                    elif self.defender_name == 'Marauder':
                        hp = hp - 20
                    else:
                        print('Stimpack Damage Error')
                if self.defender.race != 'zerg':
                    htk = self.damage_calc.htk(pre_armor_damage, hp, armor_mod, leftover_damage)
                    ttk = self.damage_calc.ttk(htk, cooldown)
                elif self.defender.race == 'zerg':
                    # Zerg regen health at a rate of 0.38 per s
                    # Roaches Burrowed regen at a rate of 7 hp per s
                    # Mutalisks regen at a rate of 1.4 hp per s
                    regen = 0.38
                    if self.defender_name == 'Mutalisk':
                        regen = 1.4
                    elif self.roach_burrow:
                        regen = 7
                    [htk, ttk] = self.damage_calc.zerg_htk_ttk(pre_armor_damage, hp, armor_mod, )
                    pass
                self.htk_label.text = f"Hits to kill: {htk} hits"
                self.ttk_label.text = f"Time to kill: {ttk}s"
            else:
                self.htbs_label.visible = False
                self.ttbs_label.visible = False
                self.htk_label.visible = False
                self.ttk_label.text = f"Attacker '{self.attacker_name}' cannot attack defender '{self.defender_name}'"

        else:
            print(f"Attacker not found in unit list and/or Defender not found in unit list and/or weapon is not found")

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
