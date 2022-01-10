"""
Реализовать любую настольную игру в стиле ООП.
"""


import random

class Dice:
    
    @staticmethod
    def number():
        return random.randint(1, 6)

class Player:

    def __init__(self, name):
        self.name = name
        self.__cash = 1500
        self.current_possition = 0
        self.own = []

    def get_current_possitioin(self):
        return Game.board[self.current_possition].name
    
    def get_cash(self):
        return self.__cash

    def roll_the_dice(self):
        return Dice.number(self) + Dice.number(self)
    
    def move(self):
        self.current_possition += self.roll_the_dice()

    def buy_property(self):
        Game.board[self.current_possition].level += 1
        self.__cash -= Game.board[self.current_possition].price
        self.own.append(Game.board[self.current_possition].name)
        Game.board[self.current_possition].owner = self.name
    
    def buy_upgrade(self):
        Game.board[self.current_possition].level += 1
        self.__cash -= Game.board[self.current_possition].upgrade_cost
    
    def pay_rent(self):
        self.__cash -= Game.board[self.current_possition].current_rent
    
    def get_money(self, money):
        self.__cash += money
    
    def doing_card(self, card):
        return f"Doing {card.name} quest"
    
class Card:

    def __init__(self, name):
        self.name = name

    
class Title:

    def __init__(self, name, possition):
        self.name = name
        self.__possition = possition
    
    def get_possition(self):
        return self.__possition

class LuckyTitle(Title):

    def __init__(self, name, possition):
        super().__init__(name, possition)
    
    def choise_card(self):
        return random.choice(Game.cards)


class Property(Title):

    def __init__(self, name, possition, price, mortage):
        super().__init__(name, possition)
        self.price = price
        self.mortage = mortage
        self.owner = ""
    
    def get_owner(self):
        return self.owner


class RailProperty(Property):

    def __init__(self, name, possition, price, mortage, rent):
        super().__init__(name, possition, price, mortage)
        self.rent = rent


class PropertyWithUpgreat(Property):
    def __init__(self, name, possition, price, mortage, upgrate_cost, r0, r1, r2, r3, r4, level = 0):
        super().__init__(name, possition, price, mortage)
        self.upgrade_cost = upgrate_cost
        self.level = level
        self.set_current_rent(r0, r1, r2, r3, r4)
        
    def set_current_rent(self, r0, r1, r2, r3, r4):
        if self.level == 0:
            self.current_rent = r0
        elif self.level == 1:
            self.current_rent = r1
        elif self.level == 2:
            self.current_rent = r2
        elif self.level == 3:
            self.current_rent = r3
        else:
            self.current_rent = r4

    def get_current_rent(self):
        return self.current_rent
    
    def get_level(self):
        return self.level

class Game:

    #Titles
    go = Title("Go", 0)
    mediterraneanAvenue = PropertyWithUpgreat("Mediterranean Avenue", 1, 60, 30, 50, 2, 10, 30, 90, 160)
    chance1 = LuckyTitle("Chance", 2)
    balticAvenue = PropertyWithUpgreat("Baltic Avenue", 3, 60, 30, 30, 4, 20, 60, 180, 320)
    chance2 = LuckyTitle("Chance", 4)
    readingRailroad = RailProperty("Reading Railroad", 5, 200, 100, 25)
    orientalAvenue = PropertyWithUpgreat("Oriental Avenue", 6, 100, 50, 50, 6, 30, 90, 270, 400)
    chance3 = LuckyTitle("Chance", 7)
    vermontAvenue = PropertyWithUpgreat("Vermont Avenue", 8, 100, 50, 50, 6, 30, 90, 270, 400)
    connecticutAvenue = PropertyWithUpgreat("Connecticut Avenue", 9, 120, 60, 50, 8, 40, 100, 300, 450)
    chance4 = LuckyTitle("Chance", 10)
    stCharlesPlace = PropertyWithUpgreat("St. Charles Place", 11, 140, 70, 100, 10, 50, 150, 450, 625)
    chance5 = LuckyTitle("Chance", 12)
    statesAvenue = PropertyWithUpgreat("States Avenue", 13, 140, 70, 100, 10, 50, 150, 450, 625)
    virginiaAvenue = PropertyWithUpgreat("Virginia Avenue", 14, 160, 80, 100, 12, 60, 180, 500, 700)
    pennsylvaniaRailroad = RailProperty("Pennsylvania Railroad", 15, 200, 100, 25)
    stJamesPlace = PropertyWithUpgreat("St. James Place", 16, 180, 90, 100, 14, 70, 200, 550, 750)
    chance6 = LuckyTitle("Chance", 17)
    tennesseeAvenue = PropertyWithUpgreat("Tennessee Avenue", 18, 180, 90, 100, 14, 70, 200, 550, 750)
    newYorkAvenue = PropertyWithUpgreat("New York Avenue", 19, 200, 100, 100, 16, 80, 220, 600, 800)
    chance7 = LuckyTitle("Chance", 20)
    kentuckyAvenue = PropertyWithUpgreat("Kentucky Avenue", 21, 220, 110, 150, 18, 90, 250, 700, 875)
    chance8 = LuckyTitle("Chance", 22)
    indianaAvenue = PropertyWithUpgreat("Indiana Avenue", 23, 220, 110, 150, 18, 90, 250, 700, 875)
    illinoisAvenue = PropertyWithUpgreat("Illinois Avenue", 24, 240, 120, 150, 20, 100, 300, 750, 925)
    bORailroad = RailProperty("B. & O. Railroad", 25, 200, 100, 25)
    atlanticAvenue = PropertyWithUpgreat("Atlantic Avenue", 26, 260, 130, 150, 22, 110, 330, 800, 975)
    ventnorAvenue = PropertyWithUpgreat("Ventnor Avenue", 27, 260, 130, 150, 22, 110, 330, 800, 975)
    chance9 = LuckyTitle("Chance", 28)
    marvinGardens = PropertyWithUpgreat("Marvin Gardens", 29, 280, 140, 150, 24, 120, 360, 850, 1025)
    chance10 = LuckyTitle("Chance", 30)
    pacificAvenue = PropertyWithUpgreat("Pacific Avenue", 31, 300, 150, 200, 26, 130, 390, 900, 1100)
    northCarolinaAvenue = PropertyWithUpgreat("North Carolina Avenue", 32, 300, 150, 200, 26, 130, 390, 900, 1100)
    chance11 = LuckyTitle("Chance", 33)
    pennsylvaniaAvenue = PropertyWithUpgreat("Pennsylvania Avenue", 34, 320, 160, 200, 28, 150, 450, 1000, 1200)
    shortLine = RailProperty("Short Line", 35, 200, 100, 25)
    chance12 = LuckyTitle("Chance", 36)
    parkPlace = PropertyWithUpgreat("Park Place", 37, 350, 175, 200, 35, 175, 500, 1100, 1300)
    chance13 = LuckyTitle("Chance", 38)
    boardwalk = PropertyWithUpgreat("Boardwalk", 39, 400, 200, 200, 50, 200, 600, 1400, 1700)

    #Cards
    card_money = Card("Get 200 money")
    card_lose_money = Card ("Pay 100 money")

    #Players
    vasia = Player("Vasia")
    kolia = Player("Kolia")
    petia = Player("Petia")
    myhamed = Player("Myhamed")
    

    board = [go, mediterraneanAvenue, chance1, balticAvenue, chance2, readingRailroad, orientalAvenue, chance3, vermontAvenue, connecticutAvenue, chance4, stCharlesPlace, chance5, statesAvenue, virginiaAvenue, pennsylvaniaRailroad, stJamesPlace, chance6, tennesseeAvenue, newYorkAvenue, chance7, kentuckyAvenue, chance8, indianaAvenue, illinoisAvenue, bORailroad, atlanticAvenue, ventnorAvenue, chance9, marvinGardens, chance10, pacificAvenue, northCarolinaAvenue, chance11, pennsylvaniaAvenue, shortLine, chance12, parkPlace, chance13, boardwalk]
    
    cards = [card_money, card_lose_money]
