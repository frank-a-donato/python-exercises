guests = ['Alice', 'Bob', 'Charlie']
amount = 235_01 # $235.01 in cents

base_amount = amount // len(guests)
base_amount / 100
remainder = amount % len(guests)

for i, guest in enumerate(guests):
    if i ==len(guests) - 1:
        pay_amount = base_amount + remainder
        print(f"{guest} pays extra: ${pay_amount / 100:.2f}")
    else:
        print(f"{guest} pays: ${base_amount / 100:.2f}")

