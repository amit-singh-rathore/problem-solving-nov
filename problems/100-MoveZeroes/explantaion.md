# Explanation

If we see a nozero elemnt we update that to the nozero idx and increase both cur idx and nonzero idx. If we see any zero we just update the cur idx. 
This we always keep track of the zon_zero-idx postion. 

Once we have moved all nonzero to rightm, we update everyting after nonzero idx to zero.


