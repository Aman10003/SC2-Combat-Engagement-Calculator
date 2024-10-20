import math
import units_def as u

class damage_calculation():

    # Hits to break shields
    # The leftover_damage calculation may be wrong. Liquidpedia isn't clear
    def htb(self, damage: float, shields: int, shield_armor: int):
        hits_to_break = math.ceil(shields / (damage-shield_armor))
        leftover_damage = (damage-shield_armor) - (shields % (damage-shield_armor))
        return [hits_to_break, leftover_damage]

    # Hits to kill
    # TODO: Zerg regen
    def htk(damage: float, hp: int, leftover_damage: float = 0):
        hp = hp - leftover_damage
        return math.ceil(hp / damage)

    def ttk(self, hits_to_kill: int, cooldown: float):
        # calculates attacks to kill
        # Does not work for shields yet
        return hits_to_kill / cooldown

    # Functions to calculate armor
    # Calculated armor for hp
    def armor_calc(self, defender: u.unit, armor_upgrade: int, raven: bool = False, guardian_shield: bool = False,
                   ultra_armor: bool = False):
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
        # Raven seeker missile
        if raven:
            armor_mod = armor_mod - 2
        # Sentry Guardian Shield
        if guardian_shield:
            armor_mod = armor_mod + 2
        # Ultra's carapace upgrade
        if ultra_armor:
            armor_mod = armor_mod + 2
        return armor_mod

    # Pre mitigation-damage Calculations
    def damage(self, attacker: u.unit, weapon, defender: u.unit, weapon_upgrade: int,
               splash: float = 1, prismatic: bool = False):
        base_dam = attacker.weapon[weapon]["dmg"[1]]
        # TODO: Fix bonus damage calc
        if attacker.weapon[weapon]['bonus'[2]] == defender.attributes:
            bonus = attacker.weapon[weapon]['bonus'[0]]
            bonus_scaling = attacker.weapon[weapon]['bonus'[1]]
        else:
            bonus = 0
            bonus_scaling = 0
        # Damage Dealt: This is equal to:
        #   (Base attack + Bonus damage + Attack upgrades)*Corrupted*Splash*Hallucinated*Prismatic.
        # Corrupted is removed
        # TODO: Need to add hallucinated and prismatic calculations
        return (base_dam + bonus + (attacker.weapon[weapon]['dmg'][1] + bonus_scaling) * weapon_upgrade) * splash

    # Post armor damage
    def post_armor_damage(self, damage: int, armor: int):
        post_armor_damage = damage - armor
        if post_armor_damage < 0.5:
            post_armor_damage = 0.5
        return post_armor_damage


if __name__ == 'main':
    x=1