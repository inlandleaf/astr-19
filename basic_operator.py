def perform_ops(float1, float2, int1, int2):
    # Sum of two floats
    sum_float = float1 + float2
    print(f"Sum of two floats: {sum_float}, Type: {type(sum_float)}")

    # Difference of two ints
    diff_int = int1 - int2
    print(f"Difference of two integers: {diff_int}, Type: {type(diff_int)}")

    # Product of a float and int
    prod = float1 * int1
    print(f"Product of a float and integer: {prod}, Type: {type(prod)}")

# Example usage
perform_ops(3.5, 2.5, 5, 2)