# Power Query Transformations

Reusable M code patterns for data transformation and cleansing.

## Categories

### Data Cleansing
Common data cleaning patterns and techniques.

### Date Tables
Functions for generating and enhancing date tables.

### Data Type Conversions
Safe type conversion patterns.

### Column Operations
Merging, splitting, and transforming columns.

### Table Operations
Appending, merging, and joining tables.

## Best Practices

- Use parameters for reusable queries
- Leverage query folding when possible
- Document complex transformations
- Use meaningful step names
- Avoid volatile functions (e.g., DateTime.LocalNow)

## Performance Tips

- Filter early in the transformation process
- Remove unnecessary columns early
- Use native database queries when possible
- Avoid nested Table functions
- Test with production data volumes

## File Organization

Each file contains:
- Description of the transformation
- M code with comments
- Usage examples
- Performance considerations
