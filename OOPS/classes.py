class Movie:
    def __init__(self,movie_name:str,total_seats:int,ticket_price:int)->None:
        self.movie_name=movie_name
        self.total_seats=total_seats
        self.ticket_price=ticket_price
        self.__booked_seats=0

    def book_seat(self,seats:int)->None:
        if self.total_seats-self.__booked_seats>=seats:
            print("Seats booked confirmed:",seats)
            self.__booked_seats+=seats
        else:
            print("Not enough seats available. Seats available:",self.total_seats-self.__booked_seats)

    def show_status(self)->None:
        print("Movie name:",self.movie_name,"seats available",self.total_seats-self.__booked_seats,"bookeds seats",self.__booked_seats)

animal=Movie("animal",33,290)
animal.book_seat(22)
animal.show_status()
# print(animal.__booked_seats)
animal.__booked_seats=1000
# print(animal.__booked_seats)
# animal.total_seats=99999
animal.book_seat(10)
animal.show_status()
animal.book_seat(3)
animal.show_status()