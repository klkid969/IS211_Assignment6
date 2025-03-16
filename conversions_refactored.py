class ConversionNotPossible(Exception):
    pass

conversion_factors = {
    ("Celsius", "Kelvin"): lambda x: x + 273.15,
    ("Celsius", "Fahrenheit"): lambda x: (x * 9/5) + 32,
    ("Fahrenheit", "Celsius"): lambda x: (x - 32) * 5/9,
    ("Fahrenheit", "Kelvin"): lambda x: (x - 32) * 5/9 + 273.15,
    ("Kelvin", "Celsius"): lambda x: x - 273.15,
    ("Kelvin", "Fahrenheit"): lambda x: (x - 273.15) * 9/5 + 32,
    ("Miles", "Yards"): lambda x: x * 1760,
    ("Miles", "Meters"): lambda x: x * 1609.34,
    ("Yards", "Miles"): lambda x: x / 1760,
    ("Yards", "Meters"): lambda x: x * 0.9144,
    ("Meters", "Miles"): lambda x: x / 1609.34,
    ("Meters", "Yards"): lambda x: x / 0.9144,
}

def convert(from_unit, to_unit, value):
    if from_unit == to_unit:
        return value
    try:
        conversion_func = conversion_factors[(from_unit, to_unit)]
        return conversion_func(value)
    except KeyError:
        raise ConversionNotPossible(f"Conversion from {from_unit} to {to_unit} is not possible.")