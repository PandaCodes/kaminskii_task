# Application Task for Insai-Tech

Work is still in progres and might be complemented over the time till the deadline during moments of inspiration...

## Task 1
Information in comments


## Task 2
let R be the conflict radius. 
L - a size of a bundle.
N - neurons count

Task can be solved, for example, by sorting neurons by one coordinate ( O(NlogN) ) then checking for closest neighbours till the x + R coordinate. Which will be average O(N* L/R) with the uniform distribution of neurons.
Yet, this check might take near the O(N^2) in the worst case, when all neurons are close eonugh in given coordinate, but rearly conflict in another.
Indexing by both coordinates might improve the situation, but makes it hard to select neighbours on both dimentions simultaneously and also might affect complexity on a specific cases.

Also we could think about using descrete nature of the coordinates and mark "conflict area". 
This might work if we have R^2 << N or/and hardware that performs fast on matrix operations, such as masking. Which is not our case here.

Implemented soulution uses grid cells with the diagonal of R that considered as a potential conflict area. (cell dimention d = ⌊R/√2⌋)
Thus, two neurons in one cell are going to be in conflict by definition. Also we must consider that neuron will affect surrounding cells (8 cells).
Starting to read neurons one by one, we add information about their positions on the grid. If the cell contains at least one another neuron, we mark the new one as conflicting (and the old one too if it is alone). Also we should check all the surrounding cells that might be affected (count C of such sells is < 16, cause R < √2*(d+1) ~ √2d as d >> 1 and the max cells count intersected with area is when neuron is in the corner of cell ) for non-conflicting neurons at the moment (they have max 1 in a cell, otherwise - they are already marked as conflicting). The worst case is when we have new neuron in a cell and many neurons around to check. But we can't have big amount of such "unlucky" neurons. If one such neuron has k neighbors to check, that means that k-C of them are not first in their cell and was checked by O(1). Thus, increase in complexity of checking one neuron to O(k), brings us asymptotycally same number of fast-checked neurons. (k-C)*O(1) + O(k) ~ O(k)  for k-C+1 neurons, participating in a such worst case. 

Suchwise worst-case complexity must be O(N) if I don't mess anything. //
With the uniform distribution of neurons, average count per cell is N/(L/d)^2 which is less than 0.1 in cell, so the average complexity is C*O(N) ~ O(N)


(Posiible microoptimisations: several shifted grids, subgrid, postpone alone-in-a-cell neurons check, write on C.)


//Scalability? - Merge sort?
// use complex plane/ geometry/nets/custom cells/topology?