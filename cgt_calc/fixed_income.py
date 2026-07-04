"""Fixed-income classification helpers."""

from __future__ import annotations

from enum import StrEnum


class FixedIncomeType(StrEnum):
    """Supported fixed-income security classes."""

    US_TREASURY_BILL = "US_TREASURY_BILL"
    US_TREASURY_NOTE = "US_TREASURY_NOTE"
    US_TREASURY_BOND = "US_TREASURY_BOND"
    CORPORATE_BOND = "CORPORATE_BOND"


def classify_fixed_income(
    symbol: str | None, description: str
) -> FixedIncomeType | None:
    """Classify a Schwab fixed-income row from its symbol and description."""
    if not symbol:
        return None

    description_upper = description.upper()

    if (
        "US TREASURY BILL" in description_upper
        or "US TREASURY BIL" in description_upper
        or "U S T BILL" in description_upper
    ):
        return FixedIncomeType.US_TREASURY_BILL

    if (
        "US TREASUR NT" in description_upper
        or "US TREASU NT" in description_upper
        or "UST NOTE" in description_upper
    ):
        return FixedIncomeType.US_TREASURY_NOTE

    if "US TREASURY" in description_upper and "UST BOND" in description_upper:
        return FixedIncomeType.US_TREASURY_BOND

    if " DUE " in description_upper or "**CALLED**" in description_upper:
        return FixedIncomeType.CORPORATE_BOND

    return None


def is_deeply_discounted_security_candidate(
    fixed_income_type: str | None,
) -> bool:
    """Return whether this security should be routed through DDS income logic."""
    return fixed_income_type == FixedIncomeType.US_TREASURY_BILL.value


def is_coupon_bearing_fixed_income(fixed_income_type: str | None) -> bool:
    """Return whether this security can carry coupon/accrued-interest treatment."""
    return fixed_income_type in {
        FixedIncomeType.US_TREASURY_NOTE.value,
        FixedIncomeType.US_TREASURY_BOND.value,
        FixedIncomeType.CORPORATE_BOND.value,
    }
