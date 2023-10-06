class HSCards:
    attack = 0
    health = 0
    deathrattle = None
    charge = None
    battlecry = None
    buffs_attack_to_all = 4
    is_poison = True


class HSPlayer:
    nickname = ""
    games_played_count = 23141
    rating = 5000
    games_played = []
    is_online = False


class HSGameEvents:
    turn = 0
    players = [HSPlayer(), HSPlayer()]
    card = HSCards()
    card_target = None


deathwing = HSCards()
deathwing.attack = 8
deathwing.health = 8

grommash = HSCards()
grommash.attack = 4
grommash.health = 10
grommash.charge = True

nick = HSPlayer()
nick.nickname = "Nick"

kevin = HSPlayer()
kevin.nickname = "Kevin"

kevin_nick_gh3r2f4hdddj3 = HSGameEvents()
kevin_nick_gh3r2f4hdddj3.card = deathwing
kevin_nick_gh3r2f4hdddj3.turn = 1
kevin_nick_gh3r2f4hdddj3.players = [kevin, nick]
kevin_nick_gh3r2f4hdddj3.card_target = grommash

print(vars(kevin), vars(nick), vars(kevin_nick_gh3r2f4hdddj3), vars(grommash), vars(deathwing))

destructor5000 = nick
destructor5000.nickname = input()

print(nick.nickname)
