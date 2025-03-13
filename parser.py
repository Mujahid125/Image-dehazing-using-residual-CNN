def parse_digit_matrix(matrix):
    """Parse a 3x9 matrix into individual 3x3 digit matrices."""
    digits = []
    for i in range(0, 27, 3):  # 3x9 means 27 characters in each row for 9 digits
        digits.append([
            row[i:i + 3] for row in matrix
        ])
    return digits

def toggle_possibilities(digit_matrix, reference_digits):
    """
    Generate all possible digits by toggling one LED.
    Return a list of valid digits or None if invalid.
    """
    possible_digits = []
    for ref_idx, ref_digit in enumerate(reference_digits):
        differences = 0
        for r in range(3):
            for c in range(3):
                if digit_matrix[r][c] != ref_digit[r][c]:
                    differences += 1
        if differences == 1 or differences == 0:
            possible_digits.append(ref_idx)
    return possible_digits

def seven_segment_sum(reference, number_matrix):
    """
    Calculate the sum of all numbers formed by toggling one light per digit.
    If any digit is invalid, return "Invalid".
    """
    # Parse reference and number matrices
    reference_digits = parse_digit_matrix(reference)
    number_digits = parse_digit_matrix(number_matrix)
    
    # Store possible digits for each segment in the number
    possible_digits_list = []
    for digit in number_digits:
        possibilities = toggle_possibilities(digit, reference_digits)
        if not possibilities:
            return "Invalid"
        possible_digits_list.append(possibilities)
    
    # Generate all combinations of numbers
    from itertools import product
    total_sum = 0
    for combination in product(*possible_digits_list):
        total_sum += int(''.join(map(str, combination)))
    
    return total_sum

# Input the 3x9 matrix for digits 0-9
reference = [input().strip() for _ in range(3)]

# Input the 3xN matrix for the number
number_matrix = [input().strip() for _ in range(3)]

# Calculate and print the result
result = seven_segment_sum(reference, number_matrix)
print(result)
