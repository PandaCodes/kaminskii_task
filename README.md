# Application Task for Insai-Tech

## Task 1
Information in notebook


## Task 2
Let
- **R** be the conflict radius
- **L** - a size of a bundle
- **N** - neurons count

Task can be solved, for example, by sorting neurons by one coordinate ( **O(NlogN)** ) then checking for closest neighbours till the **x + R** coordinate. Which will be in average **O(N\*L/R)** with the uniform distribution of neurons.
Yet, this check might take near the **O(N^2)** in the worst case, when all neurons are close eonugh in given coordinate, but rearly conflict in another.
Indexing by both coordinates might improve the situation, but makes it hard to select neighbours on both dimentions simultaneously and also might affect complexity on a specific cases.

Also we could think about using descrete nature of the coordinates and mark "conflict area". 
This might work if we have **R^2 << N** or/and hardware that performs fast on matrix operations, such as masking. Which is not our case here.

### Solution
**Implemented** soulution uses grid cells with the diagonal of R that considered as a potential conflict area. (cell dimention **d = ⌊R/√2⌋**)
Thus, two neurons in one cell are going to be in conflict by definition. Also we must consider that neuron will affect some of the surrounding cells. Count **C** of such cells is **< 16**, cause **R < √2(d+1) ~ √2d** as **d >> 1** and the max cells count intersected with the conflicting area is when neuron is in the corner of a cell.
Starting to read neurons one by one, we add information about their positions on the grid. 
- If the cell contains at least one another neuron, we mark the current one as conflicting (and the old one too if it was alone). 
- If the cell is empty, we check all neurons in surrounding touching cells while we don't find (may be won't) conflicting with the current.
- In both cases we also check if the current neuron affects non-conflicting neurons in surrounding touching cells (max 1 neuron in a cell, because if there is more - all was marked as conflicting on their step 1). 

With the uniform distribution of neurons, average count per cell is **N/(L/d)^2** which is less than 0.1 in cell, so the average complexity is  **C\*O(N) ~ O(N)**

The worst case is when we have new neuron in an empty cell and many neurons around to check. But we can't have a big amount of such "unlucky" neurons. If one such neuron has k neighbors to check, that means that **k-C** of them are not first in their cell and was processed by **O(1)**. Thus, increase in complexity of checking one neuron to **O(k)**, brings us asymptotycally same number of fast-checked neurons. **(k-C)O(1) + O(k) ~ O(k)**  for **k-C+1** neurons, participating in a such worst case. 

Suchwise worst-case complexity must be also **C\*O(N) ~ O(N)**.

((Posiible microoptimisations: several shifted grids, subgrid, postpone alone-in-a-cell neurons check, write on C.))

##### Scalability
Not sure what do you mean by scalability here. 
If you mean executing in parallel then merge results, this probably won't work for this algorythm. In this case some hybrid approach with the Merge sort might work.
// Maybe use geometry/graphs with custom cells/topology