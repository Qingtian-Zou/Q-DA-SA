# Player

Human

# Answer

So we need to cut the sequence into 3 subsequences that have the same sum.
Let's first calculate this sum: (900+1200+100+500+800+1100+200+400+300+600+1000+700)/3=2600.

Next, as for how to find such 3 subsequences, because we have a target sum (2600) to reach, the quickest way is to start with large numbers.
The largest number in the sequence is 1200.
Let's try grow it in the direction where large numbers are.
The largest number that surrounds 1200 is 900, so this subsequence is now grown to [900, 1200], whose sum is 2100.
Because the target sum is 2600, the 700 left of 900 cannot be used.
Therefore, let's grow this subsequence in the opposite direction with 100.
This results to a subsequence of [900, 1200, 100], but this is a dead end.
We need 400 to grow this subsequence's sum to 2600, but the available numbers are 700 and 500.
Let's look back at how we have produced this subsequence.
We start with 1200, and then assume that 900 is in the same subsequence.
After that, every step we took was deterministic.
If this results to a dead end, our assumption that 1200 and 900 belong to the same subsequence is false.
Therefore, the first cut is between stones worthy of 900 and 1200.

The rest is easy.
We just need to grow subsequences starting from this very first cut we have deduced.
Let's see:
> 1200+100+500+800=2600

> 900+700+1000=2600

> 1100+200+400+300+600=2600

Thus we have the 3 subsequences, and the 3 cuts are:
- Between 1200 and 900.
- Between 800 and 1100.
- Between 600 and 1000.