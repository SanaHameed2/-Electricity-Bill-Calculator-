# Electricity Bill Calculator (Pakistan Tariff Model)

## About

This is a simple Python project to calculate electricity bills based on Pakistan’s residential rates. It asks the user to enter the number of units used and then shows the total bill.

## Files

- `electricity.py` – Calculates the bill based on unit slabs.
- `main.py` – Runs the program and gets user input.

## How It Works

Electricity is charged in steps (slabs). The more units you use, the higher the rate per unit. This project uses fixed rates for each range:

| Units Used | Rate per Unit (PKR) |
|------------|---------------------|
| 0–100      | 37.38               |
| 101–200    | 45.15               |
| 201–300    | 50.17               |
| 301–400    | 56.73               |
| 401–500    | 59.76               |
| 501–600    | 61.70               |
| 601–700    | 63.24               |
| 701+       | 69.27               |

The final bill adds up the cost from each slab used.

## How to Run

Make sure Python 3 is installed.

Open a terminal and run:

```bash
python main.py
Enter the number of units when asked.

Example
plaintext
Copy
Edit
Enter units consumed: 250
Units consumed: 250
Bill amount: Rs 11185.0



