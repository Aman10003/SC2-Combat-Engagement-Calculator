import math
import units_def as u

class damage_calculation:

    # Hits to break shields
    # The leftover_damage calculation may be wrong. Liquidpedia isn't clear
    # Change calculations for post armor damage into calculations
    def htb(self, damage: int, shields: int, shield_armor: int):
        post_armor_damage = self.post_armor_damage(damage, shield_armor)
        hits_to_break = math.ceil(shields / post_armor_damage)
        leftover_damage = post_armor_damage - (shields % post_armor_damage)
        if leftover_damage == post_armor_damage:
            leftover_damage = 0
        # leftover_damage = shields % (damage - shield_armor)
        return [hits_to_break, leftover_damage]

    # Hits to kill
    # Post armor damage
    # Add ability to calculation post armor damage
    # TODO: Zerg regen
    def htk(self, damage: int, hp: int, armor: int, leftover_damage: float = 0):
        post_armor_damage = self.post_armor_damage(damage, armor)
        hp = hp - leftover_damage
        return math.ceil(hp / post_armor_damage)

    @staticmethod
    def ttk(hits_to_kill: int, cooldown: float):
        # Calculates time to kill
        # Does not work for shields yet(maybe)
        return hits_to_kill * cooldown

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
    @staticmethod
    def armor_mod(raven: bool = False, guardian_shield: bool = False, ultra_armor: bool = False):
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
    def damage(self, weapon, defender: u.unit, weapon_upgrade: int,
               splash: float = 1, prismatic: bool = False):
        base_dam = weapon['dmg'][0]
        # TODO: Fix bonus damage calc
        if weapon['bonus'][2] == defender.attributes:
            bonus = weapon['bonus'][0]
            bonus_scaling = weapon['bonus'][1]
        else:
            bonus = 0
            bonus_scaling = 0
        # TODO: Damage Scaling double check
        # Damage Dealt: This is equal to:
        #   (Base attack + Bonus damage + Attack upgrades)*Corrupted*Splash*Hallucinated*Prismatic.
        # Corrupted is removed
        # TODO: Need to add hallucinated and prismatic calculations
        return (base_dam + bonus + (weapon['dmg'][1] + bonus_scaling) * weapon_upgrade) * splash

    # Post armor damage
    def post_armor_damage(self, damage: int, armor: int):
        post_armor_damage = damage - armor
        if post_armor_damage < 0.5:
            post_armor_damage = 0.5
        return post_armor_damage


if __name__ == 'main':
    x = 1
