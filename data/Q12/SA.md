# Player

Human

# Answer

First of all, let's see what are on the two dices:
- Dice A: [1, 9, 2, 0, 7, 8]
- Dice B: [1, 5, 2, 6, 3, 4]

Using two dices to show dates in a month means that they should show integers from 01 to 31.
We will need all 10 digits from 0 to 9.
Also, considering that we will need 01 to 29, digits 0, 1, and 2 all need to appear twice in different dices.
This means that we will need 13 digits, which are 0 to 9 plus 0, 1, and 2.
However, two dices only provide a total of 12 digits.
Well, it is digits that are shown on the dices but not dots.
This means that 6 can be used as 9 if placed up side down, so we need only one digit 6 (or just one digit 9 for the similar reason).

So now we have fixed all 12 digits to be placed:
[0, 1, 2, 3, 4, 5, 6 (or 9), 7, 8, 0, 1, 2].
Let's look back at the two dices.
Dice A is perfectly fine: it has digits 0, 1, and 2, and also 3 of the rest digits.
As a result, dice B needs to have [0, 1, 2, 3, 4, 5].
Looking at the current dice B, it is obvious that digit 6 needs to be changed to digit 0.

In conclusion, digit 6 in the right dice needs to be changed to digit 0.