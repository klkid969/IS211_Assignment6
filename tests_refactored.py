import conversions_refactored
import pytest

def test_temperature_conversions():
    assert conversions_refactored.convert("Celsius", "Kelvin", 0) == 273.15
    assert conversions_refactored.convert("Celsius", "Kelvin", 100) == 373.15
    assert conversions_refactored.convert("Celsius", "Kelvin", -273.15) == 0.0
    assert conversions_refactored.convert("Fahrenheit", "Celsius", 32) == 0
    assert conversions_refactored.convert("Fahrenheit", "Celsius", 212) == 100
    assert conversions_refactored.convert("Fahrenheit", "Celsius", -40) == -40
    assert conversions_refactored.convert("Kelvin", "Celsius", 273.15) == 0
    assert conversions_refactored.convert("Kelvin", "Fahrenheit", 273.15) == 32

def test_distance_conversions():
    assert conversions_refactored.convert("Miles", "Yards", 1) == 1760
    assert conversions_refactored.convert("Miles", "Meters", 1) == 1609.34
    assert conversions_refactored.convert("Yards", "Miles", 1760) == 1
    assert conversions_refactored.convert("Yards", "Meters", 1) == 0.9144
    assert conversions_refactored.convert("Meters", "Miles", 1609.34) == 1
    assert conversions_refactored.convert("Meters", "Yards", 1) == 1 / 0.9144

def test_same_unit_conversion():
    assert conversions_refactored.convert("Celsius", "Celsius", 10) == 10
    assert conversions_refactored.convert("Miles", "Miles", 5) == 5
    assert conversions_refactored.convert("Kelvin", "Kelvin", 300) == 300
    assert conversions_refactored.convert("Meters", "Meters", 100) == 100

def test_invalid_conversion():
    with pytest.raises(conversions_refactored.ConversionNotPossible):
        conversions_refactored.convert("Celsius", "Miles", 10)
    with pytest.raises(conversions_refactored.ConversionNotPossible):
        conversions_refactored.convert("Miles", "Celsius", 5)
    with pytest.raises(conversions_refactored.ConversionNotPossible):
        conversions_refactored.convert("Fahrenheit", "Yards", 20)
