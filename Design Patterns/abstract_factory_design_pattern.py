from abc import ABC,abstractmethod

class Starter(ABC):
    @abstractmethod
    def prepare(self):
        pass
    
class Maincourse(ABC):
    @abstractmethod
    def prepare(self):
        pass

class Desert(ABC):
    @abstractmethod
    def prepare(self):
        pass

class PaneerTikka(Starter):
    def prepare(self):
        print("Paneer tikka is ready")

        
class DalMakhni(Maincourse):
    def prepare(self):
        print("Dal Makhni is ready")

        
class Rasgulla(Desert):
    def prepare(self):
        print("Rasgulla is ready")

class SpringRoll(Starter):
    def prepare(self):
        print("Spring roll is ready")

        
class Manchurian(Maincourse):
    def prepare(self):
        print("Manchurian is ready")

        
class Cookie(Desert):
    def prepare(self):
        print("Cookie is ready")


class CusineFactory(ABC):
    @abstractmethod
    def prepare_starter(self)->Starter:
        pass
    @abstractmethod
    def prepare_maincourse(self)->Maincourse:
        pass
    @abstractmethod
    def prepare_desert(self)->Desert:
        pass

class NorthCusine(CusineFactory):
    def prepare_desert(self) -> Desert:
        return Rasgulla()
    def prepare_maincourse(self) -> Maincourse:
        return DalMakhni()
    def prepare_starter(self) -> Starter:
        return PaneerTikka()

class ChineeseCusine(CusineFactory):
    def prepare_desert(self) -> Desert:
            return Cookie()
    def prepare_maincourse(self) -> Maincourse:
        return Manchurian()
    def prepare_starter(self) -> Starter:
        return SpringRoll()


class Resturant():
    def __init__(self,cusine:CusineFactory) -> None:
        self.cusine=cusine
    def prepare_food(self):
        desert=self.cusine.prepare_desert()
        maincourse=self.cusine.prepare_maincourse()
        starter=self.cusine.prepare_starter()
        desert.prepare()
        maincourse.prepare()
        starter.prepare()
    def change_cusine(self,cusine:CusineFactory):
        self.cusine=cusine

north=NorthCusine()
chinese=ChineeseCusine()
restro=Resturant(north)
restro.prepare_food()

restro.change_cusine(chinese)
restro.prepare_food()