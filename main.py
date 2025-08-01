from electricity import ElectricityBill

def main():
    try:
        units = int(input("Enter units consumed: "))
        bill = ElectricityBill(units)
    except ValueError as e:
        print(f"Error: {e}")
        return

    print(f"Units consumed: {bill.units}")
    print(f"Bill amount: Rs {bill.bill_amount}")

    input("Press Enter to exit...")


if __name__ == "__main__":
    main()
