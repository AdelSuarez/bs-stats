from typing import List

class Gadget:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

class StarPower:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

class Gear:
    def __init__(self, id: int, name: str, level: int):
        self.id = id
        self.name = name
        self.level = level

class Brawler:
    def __init__(self, id: int, name: str, power: int, rank: int, trophies: int, highestTrophies: int, gears: List[Gear], starPowers: List[StarPower], gadgets: List[Gadget]):
        self.id = id
        self.name = name
        self.power = power
        self.rank = rank
        self.trophies = trophies
        self.highestTrophies = highestTrophies
        self.gears = gears
        self.starPowers = starPowers
        self.gadgets = gadgets

class Club:
    def __init__(self, tag: str, name: str):
        self.tag = tag
        self.name = name

class Player:
    def __init__(self, tag: str, name: str, nameColor: str, iconId: int, trophies: int, highestTrophies: int, expLevel: int, expPoints: int, isQualifiedFromChampionshipChallenge: bool, victories3vs3: int, soloVictories: int, duoVictories: int, bestRoboRumbleTime: int, bestTimeAsBigBrawler: int, club: Club, brawlers: List[Brawler]):
        self.tag = tag
        self.name = name
        self.nameColor = nameColor
        self.iconId = iconId
        self.trophies = trophies
        self.highestTrophies = highestTrophies
        self.expLevel = expLevel
        self.expPoints = expPoints
        self.isQualifiedFromChampionshipChallenge = isQualifiedFromChampionshipChallenge
        self.victories3vs3 = victories3vs3
        self.soloVictories = soloVictories
        self.duoVictories = duoVictories
        self.bestRoboRumbleTime = bestRoboRumbleTime
        self.bestTimeAsBigBrawler = bestTimeAsBigBrawler
        self.club = club
        self.brawlers = brawlers
