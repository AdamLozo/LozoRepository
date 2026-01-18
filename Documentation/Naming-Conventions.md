# Naming Conventions

Standards for naming objects in Power BI models.

## Tables

**Fact Tables:**
- Singular nouns
- Descriptive of content
- Examples: `Sales`, `Invoice`, `Transaction`

**Dimension Tables:**
- Singular nouns
- Examples: `Customer`, `Product`, `Date`

**Bridge Tables:**
- Descriptive of relationship
- Example: `Customer Product Bridge`

## Columns

**General Rules:**
- Pascal Case with spaces
- Descriptive and clear
- Avoid abbreviations unless widely understood

**Key Columns:**
- `[Table Name] ID` for primary keys
- Example: `Customer ID`, `Product ID`

**Foreign Keys:**
- Match the name from the related table
- Example: `Customer ID` in Sales table

**Calculated Columns:**
- Descriptive of calculation
- Examples: `Full Name`, `Order Priority Level`

## Measures

**Format:** Descriptive with spaces

**Prefixes (when helpful):**
- `Total` for basic aggregations: `Total Sales`
- `Avg` for averages: `Avg Order Value`
- `Count` for counts: `Count Orders`
- `%` for percentages: `% Growth`

**Time Intelligence:**
- Include period in name
- Examples: `Sales YTD`, `Sales PY`, `Sales vs PY`

**Ratios and Percentages:**
- Clear numerator and denominator
- Examples: `Gross Margin %`, `Customer Retention Rate`

## Measure Groups

Use display folders to organize measures:
- Time Intelligence
- Financial Metrics  
- HR Analytics
- Calculations
- Utilities

## DAX Variables

**Format:** Pascal Case or UPPERCASE
- Examples: `CurrentValue`, `CURRENT_VALUE`
- Use descriptive names
- Avoid single letters except for iterators (x, y)

## Best Practices

1. Be consistent across the model
2. Use full words, not abbreviations
3. Make names self-documenting
4. Consider sort order when naming
5. Use display folders to organize related items