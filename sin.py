import math

def generate_table():
    print(f"{'x':<10} {'sin(x)':<10}") # print x and sin(x) table headers aligned with 10 characters of width
    print("="*20) # print 20 = characters for table divider

    for i in range(1000):
        x = i / 500 * math.pi # divide values by 500 to ensure maximum value of pi coefficient is 2
        sin_x = math.sin(x) # perform sin from math library on x value
        # print x and sin(x) output to 4 decimal places to table aligned with 10 characters of width
        print(f"{x:<10.4f} {sin_x:<10.4f}")

if __name__ == "__main__":
    generate_table()