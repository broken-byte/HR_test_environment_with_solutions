Fraudulent Activity
=======================

[Fraudulent Activity HackerRank Link](https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting)

HackerLand National Bank has a simple policy for warning clients about possible fraudulent 
account activity. If the amount spent by a client on a particular day is greater than or 
equal to 2x the client's median spending for a trailing number of days, they send the client 
a notification about potential fraud. The bank doesn't send the client any notifications 
until they have at least that trailing number of prior days' transaction data.

Given the number of trailing days D and a client's total daily expenditures for a period of 
n days, find and print the number of times the client will receive a notification over all n 
days.

Function Description
--------------------

Complete the function activityNotifications in the editor below. It must return an integer 
representing the number of client notifications.

- activityNotifications has the following parameter(s):

- expenditure: an array of integers representing daily expenditures
d: an integer, the look back days for median spending
