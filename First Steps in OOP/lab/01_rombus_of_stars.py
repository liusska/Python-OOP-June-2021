def print_row(size, count):
    for row in range(size - count):
        print(" ", end="")
    for row in range(1, star_count):
        print("*", end=" ")
    print("*")


n = int(input())

for star_count in range(1, n):
    print_row(n, star_count)

for star_count in range(n, 0, -1):
    print_row(n, star_count)
