# L6_L7_17_electricity_bill — Electricity Bill

Lab 6: Code and Branch Coverage Analysis

## About

A Python module that computes electricity bills using tiered unit slabs, late payment penalties, and eligible subsidies.

## Files

| File | Description |
|------|-------------|
| `electricity_bill.py` | The module under test |
| `test_electricity_bill.py` | Complete test suite for the module |
| `CodeCoverageTest_electricity_bill.py` | Test suite achieving 100% Code (Line) Coverage |
| `BranchCoverageTest_electricity_bill.py` | Test suite achieving 100% Branch Coverage |
| `CodeCoverage_report.png` | Screenshot of terminal Code Coverage report |
| `BranchCoverage_report.png` | Screenshot of terminal Branch Coverage report |

## Running Coverage

### 1. Code Coverage (Line Coverage)
Run tests and gather line coverage:
```bash
coverage run -m pytest CodeCoverageTest_electricity_bill.py
coverage report -m
```
Result: **100% Code Coverage** (32/32 statements).

### 2. Branch Coverage
Run tests and gather branch coverage:
```bash
coverage run --branch -m pytest BranchCoverageTest_electricity_bill.py
coverage report -m
```
Result: **100% Branch Coverage** (22/22 branches).
