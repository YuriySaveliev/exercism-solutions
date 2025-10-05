"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    seats = ('A', 'B', 'C', 'D',)
    index = 0
    count = 0
    while count < number:
        yield(seats[index])
        if index == 3:
            index = 0
        else:
            index += 1
        count += 1


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    seats = generate_seat_letters(number)
    count = 1
    row = 1
    while count <= number:
        if count // 4 > 0 and count % 4 == 1:
            row += 1
        if row != 13: 
            yield(f'{row}{next(seats)}')
            count += 1 


def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """
    
    tickets_map = {}
    seats = list(generate_seats(len(passengers)))
    for item in zip(passengers, seats):
        tickets_map[item[0]] = item[1]

    return tickets_map


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """

    i = 0
    while i < len(seat_numbers):
        code_partial = f'{seat_numbers[i]}{flight_id}'
        zeroes = (12 - len(code_partial)) * '0'
        i += 1
        yield(f'{code_partial + zeroes}')
