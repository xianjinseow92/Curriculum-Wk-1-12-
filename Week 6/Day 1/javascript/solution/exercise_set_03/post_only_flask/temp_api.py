"""
File responsible for conversion between different temperature units
"""
ABS_ZERO = 273.15

CONVERSION_FUNC = {
    ('C', 'K'): lambda c: c + ABS_ZERO,
    ('C', 'F'): lambda c: (9/5)*c + 32,
    ('C', 'C'): lambda c: c,
    ('F', 'K'): lambda f: (5/9)*(f-32) + ABS_ZERO,
    ('F', 'F'): lambda f: f,
    ('F', 'C'): lambda f: (5/9)*(f-32),
    ('K', 'K'): lambda k: k,
    ('K', 'F'): lambda k: (5/9)*(k-32) + ABS_ZERO,
    ('K', 'C'): lambda k: (5/9)*(k-32)
}

def convert_temp_from_unit(temperature, unit):
    """
    Converts temperature in units of 'unit' to Kelvin, Fahrenheit, and Centigrade.
    'unit' must be one of 'K', 'F', or 'C'.
    Results returned as dictionary
    """
    other_units = {other: CONVERSION_FUNC[(unit, other)](temperature) for other in 'KFC'}
    return other_units

if __name__ == '__main__':
    # Example of usage
    print("What is 100 degrees Centrigrade in other units?")
    print(convert_temp_from_unit(100, 'C'))
