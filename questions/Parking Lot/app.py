class Car:
    def __init__(self,reg_no:str,color:str) -> None:
        self.registration_no=reg_no
        self.color=color
    def get_registration(self)->str:
        return self.registration_no
    def get_color(self)->str:
        return self.color

class ParkingLot:
    def __init__(self,size) -> None:
        self.size=size
        self.empty_slots=self.assign_empty_slots(size)
        self.parked_vehicles:list[Car|None]=[None]*size
    def assign_empty_slots(self,size):
        a=[]
        for x in range(size):
            a.append(x)
        return a
    def assign_ticket(self,car:Car):
        if len(self.empty_slots)==0:
            print("no empty slot present at the moment")
        else:
            slot=self.empty_slots[0]
            self.empty_slots=self.empty_slots[1:]
            self.parked_vehicles[slot]=car
            print(f"{car.get_registration()} no car of {car.get_color()} is partked at {slot} number")
    def get_slot_no_of_car_with_reg(self,reg_no):
        for (ind,x) in enumerate(self.parked_vehicles):
            if x and x.get_registration()==reg_no:
                return ind
        return -1
    def update_empty_slots(self,slot_no):
        i=0
        cont=0
        while cont==0 and i<len(self.empty_slots):
            if self.empty_slots[i]>slot_no:
                self.empty_slots=self.empty_slots[:i]+[slot_no]+self.empty_slots[i:]
                cont=1
            i+=1
        if cont==0:
            self.empty_slots=self.empty_slots+[slot_no]
    def leave_car(self,car:Car):
        reg_no=car.get_registration()
        slot_no=self.get_slot_no_of_car_with_reg(reg_no)
        if slot_no==-1:
            print("car is not parked")
        else:
            self.update_empty_slots(slot_no)
            print(f"car with number {car.get_registration()} has left from {slot_no}")
    def get_reg_plate_with_color(self,color):
        res=[]
        for x in self.parked_vehicles:
            if x and x.get_color()==color:
                res.append(x.get_registration())
        print(f"Registration plates of the color {color}: {res}")
    def get_slots_with_color(self,color):
        res=[]
        for (ind,x) in enumerate(self.parked_vehicles):
            if x and x.get_color()==color:
                res.append(ind)
        print(f"SLot of the color {color}: {res}")
car1=Car("KA-01-HH-1234","White")
car2=Car("KA-01-HH-9999","White")
car3=Car("KA-01-BB-0001","Black")
car4=Car("KA-01-HH-7777","Red")
car5=Car("KA-01-HH-2701","Blue")
car6=Car("KA-01-HH-3141","Black")
car7=Car("KA-01-P-333","White")
car8=Car("DL-12-AA-9999","White")

lot=ParkingLot(6)
lot.assign_ticket(car1)
lot.assign_ticket(car2)
lot.assign_ticket(car3)
lot.assign_ticket(car4)
lot.assign_ticket(car5)
lot.assign_ticket(car6)
lot.leave_car(car4)
lot.assign_ticket(car7)
lot.assign_ticket(car8)
lot.get_reg_plate_with_color("White")
lot.get_slots_with_color("White")
lot.get_slot_no_of_car_with_reg("KA-01-HH-3141")
lot.get_slot_no_of_car_with_reg("MH-04-AY-1111")