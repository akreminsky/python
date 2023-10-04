class HSCards:
    attack = 0
    health = 0
    deathrattle = None
    charge = None
    battlecry = None
    buffs_attack_to_all = 4
    is_poison = True


class HSPlayer:
    nickname = "Nick"
    games_played_count = 23141
    rating = 5000
    games_playes = []


class HSGameHand:
    turn = 0
    player = HSPlayer()
    cards_count = 0
    cards = []
    is_cursed = False


class HSGameEvents:
    turn = 0
    players = [HSPlayer(), HSPlayer()]
    card = HSCards()
    card_target = None
