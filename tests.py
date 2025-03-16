import conversions

def test_convertCelsiusToKelvin():
    print("Testing convertCelsiusToKelvin...")
    assert conversions.convertCelsiusToKelvin(0.0) == 273.15, "Test 1 Failed: 0°C to Kelvin"
    assert conversions.convertCelsiusToKelvin(100.0) == 373.15, "Test 2 Failed: 100°C to Kelvin"
    assert conversions.convertCelsiusToKelvin(-273.15) == 0.0, "Test 3 Failed: -273.15°C to Kelvin"
    assert conversions.convertCelsiusToKelvin(300.0) == 573.15, "Test 4 Failed: 300°C to Kelvin"
    assert conversions.convertCelsiusToKelvin(25.0) == 298.15, "Test 5 Failed: 25°C to Kelvin"

def test_convertCelsiusToFahrenheit():
    print("Testing convertCelsiusToFahrenheit...")
    assert conversions.convertCelsiusToFahrenheit(0.0) == 32.0, "Test 1 Failed: 0°C to Fahrenheit"
    assert conversions.convertCelsiusToFahrenheit(100.0) == 212.0, "Test 2 Failed: 100°C to Fahrenheit"
    assert conversions.convertCelsiusToFahrenheit(-40.0) == -40.0, "Test 3 Failed: -40°C to Fahrenheit"
    assert conversions.convertCelsiusToFahrenheit(300.0) == 572.0, "Test 4 Failed: 300°C to Fahrenheit"
    assert conversions.convertCelsiusToFahrenheit(25.0) == 77.0, "Test 5 Failed: 25°C to Fahrenheit"

def test_convertFahrenheitToCelsius():
    print("Testing convertFahrenheitToCelsius...")
    assert conversions.convertFahrenheitToCelsius(32.0) == 0.0, "Test 1 Failed: 32°F to Celsius"
    assert conversions.convertFahrenheitToCelsius(212.0) == 100.0, "Test 2 Failed: 212°F to Celsius"
    assert conversions.convertFahrenheitToCelsius(-40.0) == -40.0, "Test 3 Failed: -40°F to Celsius"
    assert conversions.convertFahrenheitToCelsius(77.0) == 25.0, "Test 4 Failed: 77°F to Celsius"
    assert conversions.convertFahrenheitToCelsius(500.0) == 260.0, "Test 5 Failed: 500°F to Celsius"

def test_convertFahrenheitToKelvin():
    print("Testing convertFahrenheitToKelvin...")
    assert conversions.convertFahrenheitToKelvin(32.0) == 273.15, "Test 1 Failed: 32°F to Kelvin"
    assert conversions.convertFahrenheitToKelvin(212.0) == 373.15, "Test 2 Failed: 212°F to Kelvin"
    assert conversions.convertFahrenheitToKelvin(-40.0) == 233.15, "Test 3 Failed: -40°F to Kelvin"
    assert conversions.convertFahrenheitToKelvin(77.0) == 298.15, "Test 4 Failed: 77°F to Kelvin"
    assert conversions.convertFahrenheitToKelvin(500.0) == 533.15, "Test 5 Failed: 500°F to Kelvin"

def test_convertKelvinToCelsius():
    print("Testing convertKelvinToCelsius...")
    assert conversions.convertKelvinToCelsius(273.15) == 0.0, "Test 1 Failed: 273.15 K to Celsius"
    assert conversions.convertKelvinToCelsius(373.15) == 100.0, "Test 2 Failed: 373.15 K to Celsius"
    assert conversions.convertKelvinToCelsius(233.15) == -40.0, "Test 3 Failed: 233.15 K to Celsius"
    assert conversions.convertKelvinToCelsius(298.15) == 25.0, "Test 4 Failed: 298.15 K to Celsius"
    assert conversions.convertKelvinToCelsius(533.15) == 260.0, "Test 5 Failed: 533.15 K to Celsius"

def test_convertKelvinToFahrenheit():
    print("Testing convertKelvinToFahrenheit...")
    assert conversions.convertKelvinToFahrenheit(273.15) == 32.0, "Test 1 Failed: 273.15 K to Fahrenheit"
    assert conversions.convertKelvinToFahrenheit(373.15) == 212.0, "Test 2 Failed: 373.15 K to Fahrenheit"
    assert conversions.convertKelvinToFahrenheit(233.15) == -40.0, "Test 3 Failed: 233.15 K to Fahrenheit"
    assert conversions.convertKelvinToFahrenheit(298.15) == 77.0, "Test 4 Failed: 298.15 K to Fahrenheit"
    assert conversions.convertKelvinToFahrenheit(533.15) == 500.0, "Test 5 Failed: 533.15 K to Fahrenheit"

def test_convertFahrenheitToKelvin():
    print("Testing convertFahrenheitToKelvin...")
    # Add 5 test cases here

def test_convertKelvinToCelsius():
    print("Testing convertKelvinToCelsius...")
    # Add 5 test cases here

def test_convertKelvinToFahrenheit():
    print("Testing convertKelvinToFahrenheit...")
    # Add 5 test cases here

# Run the tests
test_convertCelsiusToKelvin()
test_convertCelsiusToFahrenheit()
test_convertFahrenheitToCelsius()
test_convertFahrenheitToKelvin()
test_convertKelvinToCelsius()
test_convertKelvinToFahrenheit()

def test_convertFahrenheitToKelvin():
    print("Testing convertFahrenheitToKelvin...")
    result = conversions.convertFahrenheitToKelvin(-40.0)
    print(f"Fahrenheit: -40.0, Kelvin: {result}")
    assert result == 233.15, "Test 3 Failed: -40°F to Kelvin"
    # ... other tests ...