def square_odd_even(start, end):
    squares = [x**2 for x in range(start, end + 1)]
    odd_squares = [x for x in squares if x % 2 != 0]
    even_squares = [x for x in squares if x % 2 == 0]
    return squares, odd_squares, even_squares

start_range = int(input("Enter the starting number: "))
end_range = int(input("Enter the ending number: "))

squares, odd_squares, even_squares = square_odd_even(start_range, end_range)

print("List of squares:", squares)
print("List of odd squares:", odd_squares)
print("List of even squares:", even_squares)