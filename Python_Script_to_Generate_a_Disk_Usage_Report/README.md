# Python Script to Generate a Disk Usage Report

Python language provides different libraries to perform different operations. This project uses sys, os and pandas library of python to calculate the disk usage in each directory of the specified location and finally stores data into a csv file.
Disk usage reports helps to get a summary of usage of disk space and accordingly one can manage their disk allocation. If disk is getting filled fast, this a good way to know what directory is taking up most of the space and disk can be freed up accordingly.

## Libraries used:
### 1. sys
Standard library of python. No need to install

### 2. os
Standard library of python. No need to install

### 3. pandas
To install pandas
```
$pip install pandas
```

### Follow the following steps to complete the project: 
#### Step 1:
Use the __name__ to identify the main code and use sys.argv to access the command line arguments.

#### Step 2: 
Use a for loop to access each sub-directory.

#### Step 3: 
Define a function to determine the disk space used by each directory.

#### Step 4: 
Use pandas to generate a report in CSV format.

After running this program, a csv file will be automatically created in the specified directory