# Fixed-Income UK Tax Reporting Task List

This branch adds the missing support needed for Schwab fixed-income transactions
like US Treasury bills, Treasury notes/bonds, corporate bonds, and called
redemptions.

## Tasks

- [x] Create a fork and implementation branch.
- [x] Document the fixed-income gaps found in the Schwab transaction export.
- [x] Classify CUSIP fixed-income securities from Schwab descriptions.
- [x] Parse Schwab called-redemption row pairs (`CXL Redemption Adj` +
  `Redemption Adj`).
- [x] Preserve dirty cash amounts for broker cash-balance checks while using
  clean bond consideration for CGT.
- [x] Split accrued interest on bond buys/sells into foreign-interest
  adjustments.
- [x] Treat US Treasury bills as deeply discounted security candidates and
  report disposal/redemption profit as foreign interest instead of CGT.
- [x] Keep coupon-bearing US Treasury and corporate bonds on the CGT path for
  clean principal gains/losses.
- [x] Add regression tests for CUSIP accrued interest, called redemptions, and
  Treasury-bill DDS income.
- [x] Run focused Schwab/fixed-income tests and the full test suite.

## Notes

- This is calculator behavior, not personal tax advice.
- The implementation deliberately prefers explicit, testable classification over
  trying to infer every possible bond term from free-form descriptions.
- US Treasury bills in Schwab exports are handled as deeply discounted security
  candidates because their return is embedded in discount/redemption economics
  rather than explicit coupon rows.
