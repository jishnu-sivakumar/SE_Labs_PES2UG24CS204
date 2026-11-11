RATES = {"DOM": 3, "COM": 6}
SLAB = {"A": 1, "B": 2}

def units_consumed(reading):
    try:
        if not isinstance(reading, str):
            return None
        parts = reading.split(':')
        if len(parts) != 2:
            return None
        previous = int(parts[0].strip())
        current = int(parts[1].strip())
        if previous < 0 or current < 0 or current < previous:
            return None
        return current - previous
    except Exception:
        return None

def daily_average(units_csv):
    try:
        if not isinstance(units_csv, str):
            return None
        if not units_csv.strip():
            return None
        parts = units_csv.split(',')
        units = []
        for u in parts:
            cleaned = u.strip()
            if not cleaned:
                return None
            val = int(cleaned)
            if val < 0:
                return None
            units.append(val)
        if not units:
            return None
        return round(sum(units) / len(units), 2)
    except Exception:
        return None

def tariff_rate(code):
    try:
        if not isinstance(code, str):
            return None
        parts = code.split('-')
        if len(parts) != 2:
            return None
        category = parts[0].strip().upper()
        slab = parts[1].strip().upper()
        if category not in RATES or slab not in SLAB:
            return None
        return RATES[category] * SLAB[slab]
    except Exception:
        return None

def main():
    print("==== Running units_consumed ====")
    user_input = input("Enter meter readings as previous:current (e.g. 1200:1350): ")
    result = units_consumed(user_input)
    print("Units Consumed:", result)

    print("\n==== Running daily_average ====")
    user_input = input("Enter daily units as CSV (e.g. 5,7,6): ")
    result = daily_average(user_input)
    print("Daily Average:", result)

    print("\n==== Running tariff_rate ====")
    user_input = input("Enter a tariff code (e.g. DOM-A): ")
    result = tariff_rate(user_input)
    print("Rate per Unit:", result)

if __name__ == "__main__":
    main()
