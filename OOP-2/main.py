class HSCards:

    def __init__(self, attack, health, deathrattle, charge, battlecry, buffs_attack_to_all, is_poison, is_immune,
                 is_alive):
        self.attack = attack
        self.health = health
        self.deathrattle = deathrattle
        self.charge = charge
        self.battlecry = battlecry
        self.buffs_attack_to_all = buffs_attack_to_all
        self.is_poison = is_poison
        self.is_immune = is_immune
        self.is_alive = is_alive

    def card_hit(self, opponents_attack):
        if self.is_alive:
            if not self.is_immune:
                self.health -= opponents_attack
            if self.health <= 0:
                self.is_alive = False

    def gain_charge(self):
        self.charge = True

    def ressurect(self):
        if not self.is_alive:
            self.is_alive = True


class HSPlayer:
    def __init__(self, nickname, games_played_count, rating, games_played, is_online, is_active):
        self.nickname = nickname
        self.games_played_count = games_played_count
        self.games_played = games_played
        self.rating = rating
        self.is_online = is_online
        self.is_active = is_active

    def update_online_status(self, online_status):
        self.is_online = online_status

    def update_rating(self, rating_update, is_increase):
        if is_increase:
            self.rating += rating_update
        else:
            self.rating -= rating_update

    def ban(self):
        self.is_active = False
