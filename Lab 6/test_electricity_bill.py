import pytest
from electricity_bill import energy_charge, late_fee, subsidy


# --- Tests for energy_charge ---
def test_energy_charge_unknown_connection():
    with pytest.raises(ValueError, match="unknown connection"):
        energy_charge(50, "industrial")


def test_energy_charge_negative_units():
    with pytest.raises(ValueError, match="invalid units"):
        energy_charge(-1, "domestic")


def test_energy_charge_slab1_domestic_boundary_zero():
    # units = 0 (boundary)
    assert energy_charge(0, "domestic") == 50


def test_energy_charge_slab1_domestic_boundary_100():
    # units = 100 (boundary)
    assert energy_charge(100, "domestic") == 100 * 3 + 50  # 350


def test_energy_charge_slab1_commercial():
    # units <= 100, commercial
    assert energy_charge(50, "commercial") == (50 * 3) * 2 + 150  # 450


def test_energy_charge_slab2_domestic_boundary_101():
    # units = 101 (boundary)
    assert energy_charge(101, "domestic") == 300 + (101 - 100) * 5 + 50  # 355


def test_energy_charge_slab2_domestic_boundary_300():
    # units = 300 (boundary)
    assert energy_charge(300, "domestic") == 300 + (300 - 100) * 5 + 50  # 1350


def test_energy_charge_slab2_commercial():
    # 100 < units <= 300, commercial
    assert energy_charge(200, "commercial") == (300 + (200 - 100) * 5) * 2 + 150  # 1750


def test_energy_charge_slab3_domestic():
    # units > 300, domestic
    assert energy_charge(400, "domestic") == 1300 + (400 - 300) * 8 + 50  # 2150


def test_energy_charge_slab3_commercial():
    # units > 300, commercial
    assert energy_charge(400, "commercial") == (1300 + (400 - 300) * 8) * 2 + 150  # 4350


# --- Tests for late_fee ---
def test_late_fee_negative_days():
    # days_late < 0
    assert late_fee(500, -5) == 0


def test_late_fee_zero_days():
    # days_late == 0 (boundary)
    assert late_fee(500, 0) == 0


def test_late_fee_within_15_days():
    # days_late = 10
    assert late_fee(500, 10) == 50


def test_late_fee_boundary_15_days():
    # days_late = 15 (boundary)
    assert late_fee(500, 15) == 50


def test_late_fee_after_15_days_low_bill():
    # days_late > 15 and bill_amount <= 2000 (covers false branch for bill_amount > 2000)
    assert late_fee(1500, 20) == 100


def test_late_fee_after_15_days_boundary_2000():
    # days_late > 15 and bill_amount == 2000
    assert late_fee(2000, 16) == 100


def test_late_fee_after_15_days_high_bill():
    # days_late > 15 and bill_amount > 2000 (covers true branch for bill_amount > 2000)
    assert late_fee(3000, 20) == 100 + 3000 // 20  # 250


# --- Tests for subsidy ---
def test_subsidy_senior_low_units_no_solar():
    # units <= 100 and is_senior True, has_solar False
    assert subsidy(50, True, False) == 50


def test_subsidy_non_senior_low_units_no_solar():
    # units <= 100 and is_senior False, has_solar False
    assert subsidy(50, False, False) == 0


def test_subsidy_senior_high_units_no_solar():
    # units > 100 and is_senior True, has_solar False
    assert subsidy(150, True, False) == 0


def test_subsidy_has_solar_low_units():
    # has_solar True and units <= 300 (covers false branch for units > 300)
    assert subsidy(200, False, True) == 100


def test_subsidy_has_solar_boundary_300():
    # has_solar True and units == 300 (boundary)
    assert subsidy(300, False, True) == 100


def test_subsidy_has_solar_high_units():
    # has_solar True and units > 300 (covers true branch for units > 300)
    assert subsidy(350, False, True) == 0


def test_subsidy_senior_with_solar_low_units():
    # both senior and solar eligible
    assert subsidy(50, True, True) == 50 + 100  # 150
