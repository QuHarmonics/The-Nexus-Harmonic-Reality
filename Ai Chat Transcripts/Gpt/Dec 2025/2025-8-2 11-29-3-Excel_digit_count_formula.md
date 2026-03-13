# Excel digit count formula

https://chat.openai.com/c/688e2ebe-aa74-8324-ab79-907d8c11db60

## USER
is there a formula for excel to total the number of a given digit in a col of cells?

## ASSISTANT
Yes, you can count the total occurrences of a specific digit (e.g., '5') across a column of cells in Excel using a formula that combines `SUMPRODUCT` and `LEN` functions. Assuming your data is in column A (from A1 to A100) and you are searching for digit `5`, use the following formula:

```excel
=SUMPRODUCT(LEN(A1:A100)-LEN(SUBSTITUTE(A1:A100,"5","")))
```

**Explanation:**
- `LEN(A1:A100)`: Returns the length of each cell’s content.
- `SUBSTITUTE(A1:A100,"5","")`: Removes the digit `5` from each cell.
- `LEN(...)-LEN(...)`: Calculates the difference, which is the count of digit `5` in each cell.
- `SUMPRODUCT(...)`: Sums the results across the entire range.

Replace `"5"` with any other digit as needed. This formula works for numbers, text, or a mix in the cells.

## USER
the col is A2:A9

## ASSISTANT
To count the total number of occurrences of a specific digit (for example, `5`) in the range **A2:A9**, use the following Excel formula:

```excel
=SUMPRODUCT(LEN(A2:A9) - LEN(SUBSTITUTE(A2:A9, "5", "")))
```

This formula will sum the total number of times the digit `5` appears within all cells in **A2:A9**. Replace `"5"` with any other digit as required.

