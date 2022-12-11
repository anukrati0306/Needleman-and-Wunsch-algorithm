# Needleman-and-Wunsch-algorithm
Needleman and Wunsch algo. for Global alignment of nucleotide sequences with Gap penalties and match rewards.

Match = +1 
Mismatch = -1
Gap = -2

Step 1 Initialization 

Creating zeros matrices using Numpy 
with one extra row and column to add the gap penalties. 

Step 2 

With each column keep score from
      - left cell 
      - upper block
      - digonally depending on match or mismatch 
take the maximum value out of three. 

Step 3 

in this code first we have created the match and mismatch matrix without gap penalties. 
later adding penalty as main matrix. 

Trace Back 

coming from the last cell diagonally 
if match go digonal 
if mismatch go to the heighest value 

If the alignment goes from higher to lower value it is a match 
lower to higher value or similer value it is a mismatch 
and the horizontal movement represent the addition of gap as "-"



