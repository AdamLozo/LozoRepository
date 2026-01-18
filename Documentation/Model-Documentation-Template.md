# Model Documentation Template

Template for documenting Power BI semantic models.

## Model Overview

**Model Name:** [Enter model name]

**Purpose:** [Brief description of the model's purpose]

**Owner:** [Name and contact]

**Last Updated:** [Date]

**Refresh Schedule:** [Frequency and time]

## Data Sources

| Source | Type | Connection | Refresh |
|--------|------|------------|----------|
| [Name] | [SQL/Excel/API] | [Connection string or path] | [Yes/No] |

## Model Structure

### Fact Tables

1. **[Table Name]**
   - Grain: [Describe granularity]
   - Row Count: [Approximate]
   - Key Columns: [List]
   - Relationships: [List related dimensions]

### Dimension Tables

1. **[Table Name]**
   - Type: [SCD Type]
   - Row Count: [Approximate]
   - Key Column: [Name]
   - Attributes: [Key attributes]

## Relationships

| From | To | Cardinality | Cross Filter | Active |
|------|-----|-------------|--------------|--------|
| [Table].[Column] | [Table].[Column] | [1:*, etc.] | [Single/Both] | [Yes/No] |

## Measures

### [Category Name]

**[Measure Name]**
```dax
[DAX Code]
```
- Purpose: [Description]
- Format: [Format string]
- Dependencies: [List]

## Calculated Columns

| Table | Column | Formula | Purpose |
|-------|--------|---------|----------|
| [Name] | [Name] | [DAX] | [Description] |

## Security

**Row-Level Security (RLS):**
- Role: [Role name]
  - Filter: [DAX filter expression]
  - Applied to: [Table names]

## Performance Considerations

- Model size: [Size in MB]
- Largest tables: [List]
- Optimization techniques applied: [List]
- Known bottlenecks: [Describe]

## Known Issues

1. [Issue description]
   - Impact: [Low/Medium/High]
   - Workaround: [If applicable]

## Change Log

| Date | Change | Author |
|------|--------|--------|
| [Date] | [Description] | [Name] |