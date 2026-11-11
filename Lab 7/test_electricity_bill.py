from hypothesis import given, strategies as st
from electricity_bill import units_consumed, daily_average, tariff_rate

@given(st.text() | st.none())
def test_units_consumed_no_crash(s):
    try:
        units_consumed(s)
    except Exception as e:
        assert False, f"units_consumed crashed with: {e}"

@given(st.text() | st.none())
def test_daily_average_no_crash(s):
    try:
        daily_average(s)
    except Exception as e:
        assert False, f"daily_average crashed with: {e}"

@given(st.text() | st.none())
def test_tariff_rate_no_crash(s):
    try:
        tariff_rate(s)
    except Exception as e:
        assert False, f"tariff_rate crashed with: {e}"
