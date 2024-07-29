import pandas as pd
import self

df = pd.read_csv("hotels.csv", dtype={"id": str})
df_cards = pd.read_csv("cards.csv", dtype=str).to_dict(orient="records")
df_cards_security = pd.read_csv("card_security.csv", dtype=str)


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


class SpaHotel(Hotel):

    def book_spa_hotel(self):
        pass



class ReservationTicket:

    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
            Thank you for your reservation!
            Here are your reservation details:
            Name: {self.customer_name}
            Hotel: {self.hotel.name}
            """
        return content

class SpaTicket:

    def __init__(self, customer_name, spa_object):
        self.customer_name = customer_name
        self.spa = spa_object

    def generate(self):
        content = f"""
            Thank you for your reservation!
            Here are your reservation details:
            Name: {self.customer_name}
            Spa: {self.spa.name}
            """
        return content
class CreditCard:
    def __init__(self, card_number):
        self.card_number = card_number
        # self.expiration = expiration
        # self.security_code = security_code
        # self.holder_name = holder_name

    def validate(self, expiration, security_code, holder_name):
        card_data = {"number": self.card_number, "expiration": expiration,
                     "cvc": security_code, "holder": holder_name}
        if card_data in df_cards:
            return True
        else:
            return False


class SecureCreditCard(CreditCard):

    def auhenticate(self, given_password):
        password = df_cards_security.loc[df_cards_security["number"] == self.card_number, "password"].squeeze()
        if password == given_password:
            return True


print(df)
hotel_id = input("Enter the id of the hotel: ")
hotel = SpaHotel(hotel_id=hotel_id)
if hotel.available():
    card_number = input("Enter your card number: ")
    expiration = input("Enter expiration date: ")
    security_code = input("Enter security code: ")
    holder_name = input("Enter holder name: ")
    credit_card = SecureCreditCard(card_number=card_number)
    if credit_card.validate(expiration=expiration, security_code=security_code, holder_name=holder_name):
        password = input("Enter your password: ")
        if credit_card.auhenticate(given_password=password):
            hotel.book()
            name = input("Enter your name: ")
            reservationTicket = ReservationTicket(customer_name=name, hotel_object=hotel)
            print(reservationTicket.generate())
            spa_package = input("Do you want spa package? (yes/no): ")
            if spa_package.lower() == "yes":
                hotel.book_spa_hotel()
                spa_ticket = SpaTicket(
                    customer_name=name,
                    spa_object=hotel
                )
                print(spa_ticket.generate())
        else:
            print("Credit card authentication failed. Please try again.")
    else:
        print("There was an error with your credit card. Please try again.")
else:
    print("Hotel is not free.")
