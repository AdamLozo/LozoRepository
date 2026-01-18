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