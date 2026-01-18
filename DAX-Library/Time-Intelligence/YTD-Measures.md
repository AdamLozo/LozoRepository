# Year-to-Date (YTD) Measures

Common YTD calculation patterns.

## Sales YTD

```dax
Sales YTD = 
CALCULATE(
    [Sales],
    DATESYTD('Date'[Date])
)
```

**Description:** Calculates sales from the beginning of the year to the current date.

**Dependencies:** 
- [Sales] measure
- 'Date' table with contiguous dates

**Usage:** Use in visuals with date hierarchy or date columns.

---

## Sales YTD vs PY

```dax
Sales YTD vs PY = 
VAR CurrentYTD = [Sales YTD]
VAR PreviousYTD = 
    CALCULATE(
        [Sales YTD],
        SAMEPERIODLASTYEAR('Date'[Date])
    )
RETURN
    CurrentYTD - PreviousYTD
```

**Description:** Compares current year-to-date sales with prior year.

**Dependencies:**
- [Sales YTD] measure
- 'Date' table marked as date table

**Performance:** Efficient for small to medium datasets.
