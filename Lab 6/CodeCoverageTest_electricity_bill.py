import pytest
from electricity_bill import energy_charge, late_fee, subsidy


# --- Tests for energy_charge ---
def test_unknown_connection():
    with pytest.raises(ValueError, match="unknown connection"):
        energy_charge(50, "industrial")


def test_invalid_units():
    with pytest.raises(ValueError, match="invalid units"):
        energy_charge(-10, "domestic")


def test_energy_charge_slab1_domestic():
    # units <= 100, domestic connection
    assert energy_charge(50, "domestic") == 50 * 3 + 50  # 200


def test_energy_charge_slab2_commercial():
    # 100 < units <= 300, commercial connection
    # charge = (300 + (200 - 100) * 5) * 2 + 150 = 800 * 2 + 150 = 1750
    assert energy_charge(200, "commercial") == 1750


def test_energy_charge_slab3_domestic():
    # units > 300, domestic connection
    # charge = 1300 + (400 - 300) * 8 + 50 = 2150
    assert energy_charge(400, "domestic") == 2150


# --- Tests for late_fee ---
def test_late_fee_on_time():
    # days_late <= 0
    assert late_fee(500, 0) == 0


def test_late_fee_within_15_days():
    # 0 < days_late <= 15
    assert late_fee(500, 10) == 50


def test_late_fee_after_15_days_high_bill():
    # days_late > 15 and bill_amount > 2000
    # fee = 100 + 3000 // 20 = 250
    assert late_fee(3000, 20) == 250


# --- Tests for subsidy ---
def test_subsidy_senior_low_units():
    # units <= 100 and is_senior
    assert subsidy(50, True, False) == 50


def test_subsidy_has_solar_high_units():
    # has_solar is True and units > 300
    assert subsidy(350, False, True) == 0
