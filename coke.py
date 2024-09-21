amount_due = 50
while True:
    insert = int(input('Insert Coin :'))
    if amount_due > 0 and insert !=30:
        amount_due = amount_due - insert
        if amount_due > 0:
            print(f"Amount Due: {amount_due}")
        else:
            print(f"Change Owed: {abs(amount_due)}")
            break
    elif insert == 30:
        print(f"Amount Due: {amount_due}")
