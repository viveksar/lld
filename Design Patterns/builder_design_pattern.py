class Laptop():
    screen=None
    ram=None
    graphic_card=None
    size=None
    battery=None

    def get_specs(self):
        if self.screen:
            print("screen:",self.screen)
        if self.ram:
            print("screen:",self.ram)
        if self.graphic_card:
            print("screen:",self.graphic_card)
        if self.size:
            print("screen:",self.size)
        if self.battery:
            print("screen:",self.battery)

class LaptopBuilder():
    def __init__(self) -> None:
        self.__laptop=Laptop()

    def set_screen(self,screen):
        self.__laptop.screen=screen
        return self
    def set_ram(self,ram):
            self.__laptop.ram=ram
            return self
    def set_graphic_card(self,graphic_card):
            self.__laptop.graphic_card=graphic_card
            return self
    def set_size(self,size):
            self.__laptop.size=size
            return self
    def set_battery(self,battery):
            self.__laptop.battery=battery
            return self
    def display_feture(self):
         self.__laptop.get_specs()

l=LaptopBuilder().set_battery(4000).set_ram(8).set_size(16)
l.display_feture()
l=LaptopBuilder().set_screen("full hd").set_battery(403200).set_ram(18).set_size(161)
l.display_feture()