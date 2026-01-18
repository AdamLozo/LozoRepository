# Generate Date Table

M code to create a comprehensive date table.

## Basic Date Table

```powerquery
let
    StartDate = #date(2020, 1, 1),
    EndDate = #date(2030, 12, 31),
    NumberOfDays = Duration.Days(EndDate - StartDate) + 1,
    DateList = List.Dates(StartDate, NumberOfDays, #duration(1, 0, 0, 0)),
    #"Converted to Table" = Table.FromList(DateList, Splitter.SplitByNothing(), {"Date"}, null, ExtraValues.Error),
    #"Changed Type" = Table.TransformColumnTypes(#"Converted to Table",{{"Date", type date}}),
    #"Added Year" = Table.AddColumn(#"Changed Type", "Year", each Date.Year([Date]), Int64.Type),
    #"Added Quarter" = Table.AddColumn(#"Added Year", "Quarter", each Date.QuarterOfYear([Date]), Int64.Type),
    #"Added Month" = Table.AddColumn(#"Added Quarter", "Month", each Date.Month([Date]), Int64.Type),
    #"Added Month Name" = Table.AddColumn(#"Added Month", "Month Name", each Date.MonthName([Date]), type text),
    #"Added Day of Week" = Table.AddColumn(#"Added Month Name", "Day of Week", each Date.DayOfWeek([Date], Day.Monday) + 1, Int64.Type),
    #"Added Day Name" = Table.AddColumn(#"Added Day of Week", "Day Name", each Date.DayOfWeekName([Date]), type text)
in
    #"Added Day Name"
```

## Features

- Year
- Quarter
- Month (number and name)
- Day of Week (number and name)
- Easily extendable for additional columns

## Usage

1. Create a new blank query
2. Open Advanced Editor
3. Paste the code
4. Adjust StartDate and EndDate as needed
5. Mark as date table in Power BI