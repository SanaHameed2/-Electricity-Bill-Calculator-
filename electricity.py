class ElectricityBill:
    """Calculate electricity bill based on Pakistani electricity rates."""

    def __init__(self, units: int) -> None:
        if units < 0:
            raise ValueError("Units consumed cannot be negative.")
        self._units = units

    @property
    def units(self) -> int:
        return self._units

    @property
    def bill_amount(self) -> float:
        units = self._units

        if units <= 100:
            amount = units * 37.38
        elif units <= 200:
            amount = 100 * 37.38 + (units - 100) * 45.15
        elif units <= 300:
            amount = 100 * 37.38 + 100 * 45.15 + (units - 200) * 50.17
        elif units <= 400:
            amount = 100 * 37.38 + 100 * 45.15 + 100 * 50.17 + (units - 300) * 56.73
        elif units <= 500:
            amount = (
                100 * 37.38
                + 100 * 45.15
                + 100 * 50.17
                + 100 * 56.73
                + (units - 400) * 59.76
            )
        elif units <= 600:
            amount = (
                100 * 37.38
                + 100 * 45.15
                + 100 * 50.17
                + 100 * 56.73
                + 100 * 59.76
                + (units - 500) * 61.70
            )
        elif units <= 700:
            amount = (
                100 * 37.38
                + 100 * 45.15
                + 100 * 50.17
                + 100 * 56.73
                + 100 * 59.76
                + 100 * 61.70
                + (units - 600) * 63.24
            )
        else:
            amount = (
                100 * 37.38
                + 100 * 45.15
                + 100 * 50.17
                + 100 * 56.73
                + 100 * 59.76
                + 100 * 61.70
                + 100 * 63.24
                + (units - 700) * 69.27
            )

        return round(amount, 2)
