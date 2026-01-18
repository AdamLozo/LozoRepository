# Annual Recurring Revenue (ARR) Measures

DAX patterns for ARR calculations.

## Total ARR

```dax
Total ARR = 
SUM('Subscriptions'[ARR Amount])
```

**Description:** Simple aggregation of ARR amounts.

**Dependencies:** 
- 'Subscriptions' table with [ARR Amount] column

---

## ARR Growth

```dax
ARR Growth = 
VAR CurrentARR = [Total ARR]
VAR PreviousARR = 
    CALCULATE(
        [Total ARR],
        DATEADD('Date'[Date], -1, YEAR)
    )
VAR Growth = CurrentARR - PreviousARR
RETURN
    Growth
```

**Description:** Year-over-year ARR growth.

---

## ARR Growth %

```dax
ARR Growth % = 
DIVIDE(
    [ARR Growth],
    CALCULATE(
        [Total ARR],
        DATEADD('Date'[Date], -1, YEAR)
    ),
    0
)
```

**Description:** Percentage change in ARR year-over-year.

**Format:** Percentage with 1 decimal place.
