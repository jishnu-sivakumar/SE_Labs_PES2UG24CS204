import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE dues (flat TEXT, month TEXT, amount INTEGER, paid INTEGER)")


def add_due(flat, month, amount, history=None):
    # conn.execute(f"INSERT INTO dues VALUES ('{flat}', '{month}', {amount}, 0)")
    if history is None:
        history = []
    conn.execute("INSERT INTO dues VALUES (?, ?, ?, 0)", (flat, month, amount))
    history.append((flat, month))
    return history


def collect(flat, month):
    query = "SELECT amount FROM dues WHERE flat = ? AND month = ?"
    row = conn.execute(query, (flat, month)).fetchone()
    if row:
        query2 = "UPDATE dues SET paid = 1 WHERE flat = ? AND month = ?"
        conn.execute(query2, (flat, month))
        return row[0]
    return None


def penalty(rule):
    try:
        late_fee = eval(rule)
    # except Exception:
    except (SyntaxError, NameError, TypeError, ZeroDivisionError):
        late_fee = 0
    return late_fee


def pending():
    rows = conn.execute("SELECT flat FROM dues WHERE paid = 0").fetchall()
    # if rows != None:
    if rows is not None:
        return [r[0] for r in rows]
    return []


def main():
    add_due("A-101", "Oct", 2500)
    add_due("A-102", "Oct", 2500)
    print(collect("A-101", "Oct"))
    print(penalty("50 * 2"))
    print(pending())


main()
