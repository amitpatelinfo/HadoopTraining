Log Analysis
==============

we are going to write a program that takes web server access log files and counts the number of hits in each minute slot over a week. 

We will analyze months of logs and plot the distribution in order to get a view of how traffic volumes tend to vary over the course of a week.

Our Map function takes a log line, pulls out the timestamp field for when the server finished processing the request, converts it into a minute-in-week slot, then writes out a (<minute-in-week slot>, <1>) key-value pair. We are mapping each line in the access log to its minute-in-week slot.

The Reduce is given <minute-in-week slot> keys and an iterator over all the values for the key that were produced by the maps. So all we have to do is sum the values as we iterate over them, in order to produce a final output which are (<minute-in-week slot>, <total hits>) key-value pairs. 
