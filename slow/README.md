# Puzzler 2020: slow.py

The goals of this implementation is to create a Python solution that is as unreasonably slow as possible. 

### Rules:

 - Progressively and continuously work towards a solution
 - No sleeping or waiting
 - No "bogo search" randomness 
 - Must be able to estimate completion time (helpful!)
 
### Usage:

```shell
python3 slow.py /usr/share/dict/words
```

### Output: 

```
Found 0 matches in 5/235886 words -- 0% complete -- 6e+10 hard boiled egg timers remaining
Found 0 matches in 6/235886 words -- 0% complete -- 0.001 aeons remaining
Found 0 matches in 7/235886 words -- 0% complete -- 1e+14 fourths remaining
Found 0 matches in 8/235886 words -- 0% complete -- 7e+56 new york seconds remaining
Found 0 matches in 9/235886 words -- 0% complete -- 1e+11 soft boiled egg timers remaining
Found 0 matches in 10/235886 words -- 0% complete -- 4e+11 moments remaining
Found 0 matches in 11/235886 words -- 0% complete -- 1e+07 friedmans remaining
Found 0 matches in 12/235886 words -- 0% complete -- 8e+04 decades remaining
Found 0 matches in 13/235886 words -- 0% complete -- 2e+11 hectoseconds remaining
Found 0 matches in 14/235886 words -- 0% complete -- 8e+16 fourths remaining
Found 0 matches in 15/235886 words -- 0% complete -- 0.7 megayears remaining
Found 0 matches in 16/235886 words -- 0% complete -- 3e+08 days remaining
Found 0 matches in 17/235886 words -- 0% complete -- 2e+22 nanoseconds remaining
Found 0 matches in 18/235886 words -- 0% complete -- 4e+10 hard boiled egg timers remaining
Found 0 matches in 19/235886 words -- 0% complete -- 7e+04 decades remaining
Found 0 matches in 20/235886 words -- 0% complete -- 1e+15 jiffies remaining
Found 0 matches in 21/235886 words -- 0% complete -- 4e+56 planck time units remaining
Found 0 matches in 22/235886 words -- 0% complete -- 1e+05 dog years remaining
Found 0 matches in 23/235886 words -- 0% complete -- 2e+04 gigaseconds remaining
Found 0 matches in 24/235886 words -- 0% complete -- 1e+11 binghams remaining
Found 0 matches in 25/235886 words -- 0% complete -- 8e+06 dog years remaining
Found 0 matches in 26/235886 words -- 0% complete -- 3e+07 megasecond remaining
Found 0 matches in 27/235886 words -- 0% complete -- 7e+06 dog years remaining
Found 0 matches in 28/235886 words -- 0% complete -- 1e+17 fourths remaining
Found 0 matches in 29/235886 words -- 0% complete -- 3e+11 hectoseconds remaining
Found 0 matches in 30/235886 words -- 0% complete -- 1e+11 soft boiled egg timers remaining
Found 0 matches in 31/235886 words -- 0% complete -- 7e+06 friedmans remaining
Found 0 matches in 32/235886 words -- 0% complete -- 4e+16 milliseconds remaining
Found 0 matches in 33/235886 words -- 0% complete -- 4e+25 picoseconds remaining
Found 0 matches in 34/235886 words -- 0% complete -- 7e+18 light-miles remaining
Found 0 matches in 35/235886 words -- 0% complete -- 4e+31 attoseconds remaining
Found 0 matches in 36/235886 words -- 0% complete -- 0.04 petaseconds remaining
Found 0 matches in 37/235886 words -- 0% complete -- 7e+56 planck time units remaining
Found 0 matches in 38/235886 words -- 0% complete -- 3e+16 milliseconds remaining
Found 0 matches in 39/235886 words -- 0% complete -- 1e+04 centuries remaining
Found 0 matches in 40/235886 words -- 0% complete -- 6e+13 blinks remaining
Found 0 matches in 41/235886 words -- 0% complete -- 2e+15 thirds remaining
...
```

### Method

For each candidate word in the dictionary, the program generates all possible strings in the graph 
with a length equal to or less than the candidate word. If any of the generated string match, 
the candidate word is printed.

To improve the "user experience", the estimated time to completion is calculated. This is achieved by
fitting an exponential curve to the time vs. word length data collected so far, then extrapolating to
the full dictionary. The estimated time remain is displayed in various "helpful" units.

Currently, it takes about 1 million years to complete (or 6e+56 plank time), though I'm still waiting
to confirm this.
