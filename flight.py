def corpFlightBookings(bookings, n):
        flights = []
        for i in range(n+1):
            flights.append(0)
        for b in bookings:
            i, j, k = b
            flights[i - 1] += k
            flights[j] -= k
        print(flights)
        for i in range(1, n):
            flights[i] += flights[i - 1]
        return flights[:-1]


print(corpFlightBookings([
    [1, 2, 10], [2, 3, 20], [2, 5, 25]
], 5))