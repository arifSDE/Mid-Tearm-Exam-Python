class Hall:
    def __init__(self, rows, cols, hall_no):
        self.seats = {}  
        self.show_list = []  
        self.rows = rows  
        self.cols = cols  
        self.hall_no = hall_no  
    def entry_show(self, id, movie_name, time):
     
        show_info = (id, movie_name, time)

        self.show_list.append(show_info)
        
        seats_array = [['0' for _ in range(self.cols)] for _ in range(self.rows)]
        
        
        self.seats[id] = seats_array

    def view_show_list(self):
        return self.show_list
    def view_available_seats(self, show_id):
        if show_id in self.seats:
            available_seats = []
            seats_array = self.seats[show_id]
            for row in range(self.rows):
                for col in range(self.cols):
                    if seats_array[row][col] == '0':
                        available_seats.append((row + 1, col + 1))  
            return available_seats
        else:
            return None

    def book_tickets(self, show_id, seats_to_book):
        if show_id in self.seats:
            seats_array = self.seats[show_id]
            for row, col in seats_to_book:
                if not (0 <= row < self.rows and 0 <= col < self.cols):
                    raise ValueError(f"Invalid seat ({row}, {col}) specified.")
                if seats_array[row][col] != '0':
                    raise ValueError(f"Seat ({row}, {col}) is already booked.")

            for row, col in seats_to_book:
                seats_array[row][col] = '1'
            self.seats[show_id] = seats_array
            return True
        else:
            raise ValueError(f"Show '{show_id}' not found or no seats allocated yet.")


class Counter:
    def __init__(self):
        self.halls = [] 

    def add_hall(self, hall):
        self.halls.append(hall)

    def view_all_shows(self):
        all_shows = []
        for hall in self.halls:
            all_shows.extend(hall.view_show_list())
        return all_shows

    def view_available_seats(self, show_id):
        for hall in self.halls:
            try:
                available_seats = hall.view_available_seats(show_id)
                return available_seats
            except ValueError as e:
                print(f"Error: {e}")
        return None
    def book_tickets(self, show_id, seats_to_book):
        for hall in self.halls:
            try:
                if hall.book_tickets(show_id, seats_to_book):
                    print("Tickets booked successfully!")
                    return True
            except ValueError as e:
                print(f"Error: {e}")
                return False
        return False
def main():
    hall1 = Hall(rows=5, cols=6, hall_no=1)
    hall2 = Hall(rows=8, cols=10, hall_no=2)
    counter = Counter()
    counter.add_hall(hall1)
    counter.add_hall(hall2)
    while True:
        print("\n===== Welcome to Ticket Booking System =====")
        print("1. View all shows")
        print("2. View available seats for a show")
        print("3. Book tickets for a show")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ").strip()
        if choice == '1':
            all_shows = counter.view_all_shows()
            print("\nAll Shows:")
            for show in all_shows:
                print(f"ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")
        elif choice == '2':
            show_id = input("Enter the ID of the show: ").strip()
            available_seats = counter.view_available_seats(show_id)
            if available_seats:
                print(f"\nAvailable Seats for Show '{show_id}':")
                for seat in available_seats:
                    print(f"Row {seat[0]}, Seat {seat[1]}")
            else:
                print(f"Show '{show_id}' not found or no seats allocated yet.")
        elif choice == '3':
            show_id = input("Enter the ID of the show: ").strip()
            available_seats = counter.view_available_seats(show_id)
            if available_seats:
                print(f"\nAvailable Seats for Show '{show_id}':")
                for seat in available_seats:
                    print(f"Row {seat[0]}, Seat {seat[1]}")

                num_seats = int(input("Enter number of seats to book: "))
                seats_to_book = []
                for _ in range(num_seats):
                    try:
                        row = int(input("Enter row number: ")) - 1  
                        col = int(input("Enter seat number: ")) - 1 
                        seats_to_book.append((row, col))
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")

                if seats_to_book:
                    if counter.book_tickets(show_id, seats_to_book):
                        print("Tickets booked successfully!")
                    else:
                        print("Failed to book tickets.")
            else:
                print(f"Show '{show_id}' not found or no seats allocated yet.")

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
if __name__ == "__main__":
    main()
