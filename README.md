# Data Analyzer and Transformer

A menu-driven Python program for entering and analyzing numeric data
stored in one-dimensional (1D) lists or two-dimensional (2D)
nested lists.

## Project Overview

This project is based on the "Functional Treat" practical brief for
Python and Data Science. The brief asks for a data analysis and
transformation program that demonstrates Python functions, built-in
operations, recursion, lambda functions, sorting, and other concepts.

The submitted source file, `Project4.py`, currently implements data
entry for 1D and 2D lists and basic statistical summaries. Some
additional features requested in the brief are not yet implemented;
these are listed below so the project documentation accurately reflects
the current code.

## Current Features

-   **Menu-driven interface** to input data, display a summary, or exit.
-   **1D list input:** enter integers separated by spaces.
-   **2D list input:** specify the number of rows and enter each row as
    space-separated integers.
-   **2D grid display:** prints the entered rows in a simple grid-like
    format.
-   **Data summary:** displays the number of elements, sum, minimum,
    maximum, and mean.
-   **Handles both list formats:** the summary function flattens a 2D
    list before calculating statistics.
-   **Global summary variable:** `global_summary` is updated with the
    element count and mean when data is entered.

## Requirements and Implementation Status

The practical brief also asks for the following features. They are **not
currently implemented in `Project4.py`**:

  -----------------------------------------------------------------------
  Requirement in the brief            Status
  ----------------------------------- -----------------------------------
  Basic statistics using built-in     Implemented (`len`, `sum`, `min`,
  functions                           `max`)

  Separate user-defined functions for Not implemented
  additional tasks, such as           
  duplicates and unique values        

  `*args` and `**kwargs`              Not implemented
  demonstrations                      

  Function docstrings using `__doc__` Not implemented
  and displaying them in the menu     

  Recursive factorial or Fibonacci    Not implemented
  calculation                         

  Lambda-based filtering, including   Not implemented
  `map()` / `filter()`                

  Sorting 1D data in ascending and    Not implemented
  descending order                    

  Sorting rows in a 2D list with      Not implemented
  `sorted()`                          

  Returning multiple statistics from  Not implemented
  one function                        

  Sample-data option                  Not implemented
  -----------------------------------------------------------------------

The table distinguishes the submitted code from the broader assignment
requirements. Do not treat unimplemented items as available program
features.

## Prerequisites

-   Python 3.8 or later is recommended.
-   No third-party Python packages are required; the current program
    uses only built-in Python functionality.

## How to Run

1.  Make sure Python is installed.

2.  Place `Project4.py` in your project folder.

3.  Open a terminal or command prompt in that folder.

4.  Run:

    ``` bash
    python Project4.py
    ```

    On some Windows installations, use:

    ``` bash
    py Project4.py
    ```

## Using the Program

When the program starts, it displays the main menu:

``` text
MAIN MENU
1. Input Data
2. Display Summary
3. Exit
```

### 1. Input Data

Choose `1`, then select the data format.

**Example: 1D list**

``` text
1. 1D Array
2. 2D Array
Enter your choice: 1
Enter data for a 1D array (separated by spaces): 10 20 30 40
```

The data is stored in a Python list.

**Example: 2D list**

``` text
1. 1D Array
2. 2D Array
Enter your choice: 2
Enter number of rows: 2
Enter row values separated by spaces: 1 2 3
Enter row values separated by spaces: 4 5 6
```

The program prints the entered rows and stores them as a nested list.

### 2. Display Summary

Choose `2` after entering data. The program displays:

-   Total number of elements
-   Sum of elements
-   Minimum value
-   Maximum value
-   Mean (average)

For example, for the values `10 20 30 40`, the summary is:

``` text
Data Summary
Total Elements (len): 4
Sum of Elements (sum): 100
Minimum Value (min): 10
Maximum Value (max): 40
Mean / Average: 25.0
```

The exact formatting may vary slightly depending on the input.

### 3. Exit

Choose `3` to end the program.

## Code Structure

  -----------------------------------------------------------------------
  Function / variable                 Purpose
  ----------------------------------- -----------------------------------
  `global_summary`                    Global string updated with the
                                      total element count and mean during
                                      data entry

  `input_data()`                      Prompts for 1D or 2D data,
                                      calculates an initial count and
                                      mean, and returns the entered list

  `display_summary(data)`             Flattens 2D data when needed and
                                      prints the count, sum, minimum,
                                      maximum, and mean

  `main()`                            Runs the main menu and manages the
                                      current dataset

  `if __name__ == "__main__":`        Starts the program when the file is
                                      run directly
  -----------------------------------------------------------------------

## Current Limitations

-   Inputs are expected to be integers separated by spaces.
-   Invalid numeric input (for example, letters where integers are
    expected) is not handled and may cause an error.
-   The program does not currently validate negative row counts or
    malformed rows.
-   An empty dataset, or a dataset containing no values, cannot produce
    minimum and maximum values. The current summary function does not
    guard against every such case.
-   `global_summary` is assigned during data entry but is not currently
    displayed or used elsewhere.
-   The program stores data in memory only; it does not save data to a
    file or database.
-   Sorting, filtering, recursion, `*args`, `**kwargs`, docstring
    inspection, and returning multiple statistics have not yet been
    added.

## Suggested Repository Layout


## Future Improvements

To meet the full practical brief, the next development steps are to add
the missing features from the implementation-status table, improve input
validation, handle empty datasets safely, and add examples for each menu
option.

## License

No license has been specified for this project. Add a license only if
required by your course or if you intend to publish the project under
particular reuse terms.
