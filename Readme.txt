CME2208 Assignment 1

Due: 22 April 2018, 23:30
Task: Write a Python Function myTable() that
a) prints out the
a. Forward Difference Table
b. Backward Difference Table
c. Central Difference Table
d. Average Table
and
b) Plots a graph that shows the resulting array values with different markers for each operator.
Requirements:
- Must be writen in Python, using the numpy and matplotlib.pyplot package. You can’t use
any package that automatically creates these tables.
- The function must accept a numpy 1D array as its argument. The input array may have any
length as long as it remains 1D. So n the same folder where your code is I will write:
a = np.array[2,5,9,3,2] and myTable(a)
- The function name MUST be myTable() otherwise marks will be deducted.
- Upload the Python function only. No zip, rar, etc required.
- The index of the input array is the x axis, so a[0]=7 means (x,y) = (0,7).
- The graph must include the original values, forward, backward, central and average operator
values in different colors and markers(will upload an example soon) along with a legend.
- Note that you will need to describe a different axis for central difference and average
operators(i.e. 0,0.5,1,1.5... instead of 0,1,2...).
- Cheating will not be tolerated and will be given a grade of zero. Student uploads will be
checked against each other using special software. Check the introduction presentations for
the late upload policy.
