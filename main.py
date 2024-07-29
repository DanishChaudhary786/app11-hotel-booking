import pandas as pd
import self

df = pd.read_csv("hotels.csv", dtype={"id": str})


class Hotel:

    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        """Book a hotel by changing its availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        """Checks if the hotel is available"""
        availablity = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availablity.lower() == "yes":
            return True
        else:
            return False


class ReservationTicket:

    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
            Than you for your reservation!
            Here are your reservation details:
            Name: {self.customer_name}
            Hotel: {self.hotel.name}
            """
        return content


print(df)
hotel_id = input("Enter the id of the hotel: ")
hotel = Hotel(hotel_id=hotel_id)
if hotel.available():
    hotel.book()
    name = input("Enter your name: ")
    reservationTicket = ReservationTicket(customer_name=name, hotel_object=hotel)
    print(reservationTicket.generate())
else:
    print("Hotel is not free.")
