#!/usr/bin/python3
class Passengers:
    def __init__(self, name, age, phone_number, email, passport_number, passenger_id):
        self.name = name
        self.age = age
        self.phone_number = phone_number
        self.email = email
        self.passport_number = passport_number
        self.passenger_id = passenger_id

class FirstClass(Passengers):
    weight = 80  # in kg
    luggage_limit = 3  # in pieces
    luggage_weight_limit = 35  # in kg
    luggage_size_limit = 158  # in cm
    luggage_fee = 100  # in dollars
    luggage_fee_per_kg = 10  # in dollars
    luggage_fee_per_piece = 50  # in dollars
    luggage_fee_per_size = 200  # in dollars
    luggage_fee_per_size_per_kg = 5  # in dollars
    luggage_fee_per_size_per_piece = 10  # in dollars
    luggage_fee_per_size_per_piece_per_kg = 2  # in dollars

    def __init__(self, name, age, phone_number, email, passport_number, passenger_id):
        super().__init__(name, age, phone_number, email, passport_number, passenger_id)
        self.seat_class = "First Class"
        self.luggage = 0  # in pieces
        self.luggage_weight = 0
        self.luggage_size = 0
        self.luggage_fee_total = 0
        self.luggage_fee_per_kg_total = 0
        self.luggage_fee_per_piece_total = 0
        self.luggage_fee_per_size_total = 0
        self.luggage_fee_per_size_per_kg_total = 0

    def show_limits(self):
        print(f"\n--- First Class Luggage Limits ---")
        print(f"Luggage pieces limit: {self.luggage_limit}")
        print(f"Luggage weight limit: {self.luggage_weight_limit} kg")
        print(f"Luggage size limit: {self.luggage_size_limit} cm")
        print(f"Fee per piece: ${self.luggage_fee_per_piece}")
        print(f"Fee per kg: ${self.luggage_fee_per_kg}")
        print(f"Fee per size: ${self.luggage_fee_per_size}")
        print(f"----------------------------------\n")

    def add_luggage(self, pieces, weight, size):
        if pieces > self.luggage_limit:
            raise ValueError("Exceeds luggage limit for First Class.")
        if weight > self.luggage_weight_limit:
            raise ValueError("Exceeds luggage weight limit for First Class.")
        if size > self.luggage_size_limit:
            raise ValueError("Exceeds luggage size limit for First Class.")

        self.luggage += pieces
        self.luggage_weight += weight
        self.luggage_size += size

        # Calculate fees
        self.luggage_fee_total = (pieces * self.luggage_fee_per_piece) + (weight * self.luggage_fee_per_kg) + (size * self.luggage_fee_per_size)
        self.luggage_fee_per_kg_total = weight * self.luggage_fee_per_kg
        self.luggage_fee_per_piece_total = pieces * self.luggage_fee_per_piece
        self.luggage_fee_per_size_total = size * self.luggage_fee_per_size
        self.luggage_fee_per_size_per_kg_total = size * weight * self.luggage_fee_per_size_per_kg
        return self.luggage_fee_total

class Economy(Passengers):
    weight = 70  # in kg
    luggage_limit = 2  # in pieces
    luggage_weight_limit = 23  # in kg
    luggage_size_limit = 158  # in cm
    luggage_fee = 50  # in dollars
    luggage_fee_per_kg = 5  # in dollars
    luggage_fee_per_piece = 30  # in dollars
    luggage_fee_per_size = 100  # in dollars
    luggage_fee_per_size_per_kg = 3  # in dollars
    luggage_fee_per_size_per_piece = 5  # in dollars
    luggage_fee_per_size_per_piece_per_kg = 1  # in dollars

    def __init__(self, name, age, phone_number, email, passport_number, passenger_id):
        super().__init__(name, age, phone_number, email, passport_number, passenger_id)
        self.seat_class = "Economy"
        self.luggage = 0  # in pieces
        self.luggage_weight = 0
        self.luggage_size = 0
        self.luggage_fee_total = 0
        self.luggage_fee_per_kg_total = 0
        self.luggage_fee_per_piece_total = 0
        self.luggage_fee_per_size_total = 0
        self.luggage_fee_per_size_per_kg_total = 0

    def show_limits(self):
        print(f"\n--- Economy Class Luggage Limits ---")
        print(f"Luggage pieces limit: {self.luggage_limit}")
        print(f"Luggage weight limit: {self.luggage_weight_limit} kg")
        print(f"Luggage size limit: {self.luggage_size_limit} cm")
        print(f"Fee per piece: ${self.luggage_fee_per_piece}")
        print(f"Fee per kg: ${self.luggage_fee_per_kg}")
        print(f"Fee per size: ${self.luggage_fee_per_size}")
        print(f"-------------------------------------\n")

    def add_luggage(self, pieces, weight, size):
        if pieces > self.luggage_limit:
            raise ValueError("Exceeds luggage limit for Economy Class.")
        if weight > self.luggage_weight_limit:
            raise ValueError("Exceeds luggage weight limit for Economy Class.")
        if size > self.luggage_size_limit:
            raise ValueError("Exceeds luggage size limit for Economy Class.")

        self.luggage += pieces
        self.luggage_weight += weight
        self.luggage_size += size

        # Calculate fees
        self.luggage_fee_total = (pieces * self.luggage_fee_per_piece) + (weight * self.luggage_fee_per_kg) + (size * self.luggage_fee_per_size)
        self.luggage_fee_per_kg_total = weight * self.luggage_fee_per_kg
        self.luggage_fee_per_piece_total = pieces * self.luggage_fee_per_piece
        self.luggage_fee_per_size_total = size * self.luggage_fee_per_size
        self.luggage_fee_per_size_per_kg_total = size * weight * self.luggage_fee_per_size_per_kg
        return self.luggage_fee_total

class Business(Passengers):
    weight = 75  # in kg
    luggage_limit = 2  # in pieces
    luggage_weight_limit = 30  # in kg
    luggage_size_limit = 158  # in cm
    luggage_fee = 80  # in dollars
    luggage_fee_per_kg = 8  # in dollars
    luggage_fee_per_piece = 40  # in dollars
    luggage_fee_per_size = 150  # in dollars
    luggage_fee_per_size_per_kg = 4  # in dollars
    luggage_fee_per_size_per_piece = 7  # in dollars
    luggage_fee_per_size_per_piece_per_kg = 1.5  # in dollars

    def __init__(self, name, age, phone_number, email, passport_number, passenger_id):
        super().__init__(name, age, phone_number, email, passport_number, passenger_id)
        self.seat_class = "Business"
        self.luggage = 0  # in pieces
        self.luggage_weight = 0
        self.luggage_size = 0
        self.luggage_fee_total = 0
        self.luggage_fee_per_kg_total = 0
        self.luggage_fee_per_piece_total = 0
        self.luggage_fee_per_size_total = 0
        self.luggage_fee_per_size_per_kg_total = 0

    def show_limits(self):
        print(f"\n--- Business Class Luggage Limits ---")
        print(f"Luggage pieces limit: {self.luggage_limit}")
        print(f"Luggage weight limit: {self.luggage_weight_limit} kg")
        print(f"Luggage size limit: {self.luggage_size_limit} cm")
        print(f"Fee per piece: ${self.luggage_fee_per_piece}")
        print(f"Fee per kg: ${self.luggage_fee_per_kg}")
        print(f"Fee per size: ${self.luggage_fee_per_size}")
        print(f"-------------------------------------\n")

    def add_luggage(self, pieces, weight, size):
        if pieces > self.luggage_limit:
            raise ValueError("Exceeds luggage limit for Business Class.")
        if weight > self.luggage_weight_limit:
            raise ValueError("Exceeds luggage weight limit for Business Class.")
        if size > self.luggage_size_limit:
            raise ValueError("Exceeds luggage size limit for Business Class.")

        self.luggage += pieces
        self.luggage_weight += weight
        self.luggage_size += size

        # Calculate fees
        self.luggage_fee_total = (pieces * self.luggage_fee_per_piece) + (weight * self.luggage_fee_per_kg) + (size * self.luggage_fee_per_size)
        self.luggage_fee_per_kg_total = weight * self.luggage_fee_per_kg
        self.luggage_fee_per_piece_total = pieces * self.luggage_fee_per_piece
        self.luggage_fee_per_size_total = size * self.luggage_fee_per_size
        self.luggage_fee_per_size_per_kg_total = size * weight * self.luggage_fee_per_size_per_kg
        return self.luggage_fee_total

def main():
    try:
        if choice == 1:
            passenger = FirstClass(
                input("Enter name: "),
                int(input("Enter age: ")),
                input("Enter phone number: "),
                input("Enter email: "),
                input("Enter passport number: "),
                input("Enter passenger ID: ")
            )
            print(f"Passenger {passenger.name} added in First Class.")
            passenger.show_limits()
        elif choice == 2:
            passenger = Economy(
                input("Enter name: "),
                int(input("Enter age: ")),
                input("Enter phone number: "),
                input("Enter email: "),
                input("Enter passport number: "),
                input("Enter passenger ID: ")
            )
            print(f"Passenger {passenger.name} added in Economy Class.")
            passenger.show_limits()
        elif choice == 3:
            passenger = Business(
                input("Enter name: "),
                int(input("Enter age: ")),
                input("Enter phone number: "),
                input("Enter email: "),
                input("Enter passport number: "),
                input("Enter passenger ID: ")
            )
            print(f"Passenger {passenger.name} added in Business Class.")
            passenger.show_limits()
        else:
            print("Invalid choice. Please select a valid class.")
            return
    except ValueError as e:
        print(f"Error: {e}")
        return
    # Add luggage
    try:
        pieces = int(input("Enter number of luggage pieces: "))
        weight = float(input("Enter total luggage weight (kg): "))
        size = float(input("Enter total luggage size (cm): "))
        luggage_fee = passenger.add_luggage(pieces, weight, size)
        print(f"Luggage added. Total fee: ${luggage_fee}")
    except ValueError as e:
        print(f"Error: {e}")
        return
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return

if __name__ == "__main__":
    print("Welcome to the Airline Booking System")
    print("1. First Class")
    print("2. Economy Class")
    print("3. Business Class")

    try:
        choice = int(input("Select a class (1-3): "))
        main()
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 3.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
