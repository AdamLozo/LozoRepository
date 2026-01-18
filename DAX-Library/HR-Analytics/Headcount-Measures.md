# Headcount Measures

DAX patterns for employee headcount analysis.

## Current Headcount

```dax
Headcount = 
CALCULATE(
    DISTINCTCOUNT('Employees'[Employee ID]),
    'Employees'[Status] = "Active"
)
```

**Description:** Count of active employees.

**Dependencies:**
- 'Employees' table
- [Employee ID] column
- [Status] column

---

## Headcount by Department

```dax
Headcount by Dept = 
CALCULATE(
    [Headcount],
    ALLEXCEPT('Employees', 'Employees'[Department])
)
```

**Description:** Department-specific headcount maintaining filter context.

---

## Average Tenure (Years)

```dax
Average Tenure Years = 
VAR TenureDays = 
    AVERAGEX(
        FILTER(
            'Employees',
            'Employees'[Status] = "Active"
        ),
        DATEDIFF(
            'Employees'[Hire Date],
            TODAY(),
            DAY
        )
    )
RETURN
    DIVIDE(TenureDays, 365.25, 0)
```

**Description:** Average years of service for active employees.

**Format:** Number with 1 decimal place.

**Dependencies:**
- 'Employees' table
- [Hire Date] column
- [Status] column

---

## Turnover Rate

```dax
Turnover Rate = 
VAR TerminationsInPeriod = 
    CALCULATE(
        DISTINCTCOUNT('Employees'[Employee ID]),
        'Employees'[Termination Date] <> BLANK(),
        'Employees'[Termination Date] >= MIN('Date'[Date]),
        'Employees'[Termination Date] <= MAX('Date'[Date])
    )
VAR AverageHeadcount = 
    CALCULATE(
        [Headcount],
        ALL('Date')
    )
RETURN
    DIVIDE(TerminationsInPeriod, AverageHeadcount, 0)
```

**Description:** Percentage of employees who left during the selected period.

**Format:** Percentage with 1 decimal place.
