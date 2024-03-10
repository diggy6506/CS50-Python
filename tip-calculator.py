def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}\n")


def dollars_to_float(dollars):
    if dollars.startswith("$"):
        dollars = dollars[1:]
    return float(dollars)


def percent_to_float(percent):
    percent = percent.rstrip('%')
    return float(percent) / 100


main()
