def f(x):
    return x**3 + 8

if __name__ == "__main__":
    x = 9
    result = f(x)
    print(f"f({x}) = {result}")

    if result > 27:
        print("YAY!")
