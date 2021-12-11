This one frustrated me pretty good (At low moments I considered manual counting but ultimately chose not to). But full discosure, I did plenty of cheating to arrive at this solution

My initial algorithm tried to find basin size by:
  1. iterating over all points
  2. iterating out in each direction until the boundary was found
  3. Then you find the max for each point and the highest ones are the top basin sizes

The flaw in this logic is not all points can see all other points within the same basin. For example, if it was shaped like the united states then Texas couldn't see Florida.
My first cheating realization was to instead do a "fill" - continually iterate in each direction until no new points were found.
I was still confused since I was trying to iterate over each point still to do a fill.  More cheating made me realize I just need to start at the low points.
The problem itself suggested this, I should have read it more thoroughly.
Along the way of cheating I came into some cool solutions, e.g. [this one using scipy.ndimage](https://gitlab.com/BrytniJ/advent-of-code-2021/-/blob/main/Day_09/Day_09.ipynb) which is an image processing package 

Ultimately, one thing that led to frustration was me assuming I was missing some computer science technique needed to solve this, but I wasn't really.
In hindsight I could have benefited from re-reading the problem carefully and also carefully outlining each step in the algorithm.
