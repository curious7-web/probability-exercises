**Method:** complement + multiply probabilities step by step  
**Key idea:** count “no shared birthdays” and subtract from 1  
**Difficulty:** ★★☆☆☆  
**Sanity check:** value should be between 0 and 1 and roughly around 0.5

### Problem

Assume there are 365 equally likely birthdays (ignore leap years), and different people’s birthdays are independent.

If there are 23 people in a room, what is the probability that at least two of them share a birthday?

### Solution

Let A be the event “at least one shared birthday”.

It is easier to first compute the probability of the complementary event “no shared birthdays”, and then subtract from 1.

We imagine adding people one by one.

- Person 1: any birthday is fine → probability 365/365.
- Person 2: must avoid person 1’s birthday → 364/365.
- Person 3: must avoid the first two → 363/365.
- ...
- Person 23: must avoid the previous 22 birthdays → 343/365.

Because birthdays are independent, we multiply these:

P(no shared birthdays)  
= (365/365) * (364/365) * (363/365) * ... * (343/365).

So:
P(no shared) = (365 * 364 * ... * 343) / 365^23.

Then:
P(A) = 1 - P(no shared)  
     = 1 - (365 * 364 * ... * 343) / 365^23.

### Answer

The probability that at least two of 23 people share a birthday is:

1 - (365 * 364 * ... * 343) / 365^23.

This is known to be a bit more than 0.5 in value, which is surprisingly high but consistent with the standard “birthday paradox” calculation.
