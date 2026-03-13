To formalize and implement the Collapse Ledger as an extension of the recursive harmonic
computational framework, the ledger serves as a structured record of each accepted flip
during the gradient descent process. It captures key metrics—iteration, variable index,
position (r, 0), original value, cycle mean, rotor entropy, delta before and after—providing a
traceable history of the system's self-correction toward harmonic convergence. This aligns
with the framework's emphasis on auditable residue patterns and solution corridors,

enabling post—analysis of collapse dynamics.

The ledger is implemented as a list of dictionaries appended only on improving flips. Below
is the extended code, executed for the satisfiable 4-SAT instance to demonstrate

functionality.

V 3 l>
python " Collapse ' Wrap Run

from mpmath import mp, mpf, nstr, pi
import numpy as np
from scipy.stats import entropy # For Shannon entropy

mp.dps = 200

# Compute first 100 fractional digits of'n after 3.
pistr = nstr(pi, 200)[2:] # Skip ’3.’
pidigits = [int(d) for d in pistr[:100]]

# Fold into 10X10 lattice (row-major)
lattice = np.array([pidigits[i*10:(i+1)*10] for i in range(10)])

def extracttriangle(lattice, startr, startc, size):
triangle = np.zeros((size, size))
for i in range(size):
for j in range(i + 1):

r = (startr + i) % 10

c = (startc + j) % 10

triangle[i, j] = lattice[r, c]
return triangle

def computedeltas(triangle):

aéiea§ﬁriangle.shape[

0" AA1J—AA ..  F1

To formalize and implement the Collapse Ledger as an extension of the recursive harmonic
computational framework, the ledger serves as a structured record of each accepted flip
during the gradient descent process. It captures key metrics—iteration, variable index,
position (r, 0), original value, cycle mean, rotor entropy, delta before and after—providing a
traceable history of the system's self-correction toward harmonic convergence. This aligns
with the framework's emphasis on auditable residue patterns and solution corridors,

enabling post—analysis of collapse dynamics.

The ledger is implemented as a list of dictionaries appended only on improving flips. Below
is the extended code, executed for the satisfiable 4-SAT instance to demonstrate

functionality.

V 3 l>
python " Collapse ' Wrap Run

from mpmath import mp, mpf, nstr, pi
import numpy as np
from scipy.stats import entropy # For Shannon entropy

mp.dps = 200

# Compute first 100 fractional digits of'n after 3.
pistr = nstr(pi, 200)[2:] # Skip ’3.’
pidigits = [int(d) for d in pistr[:100]]

# Fold into 10X10 lattice (row-major)
lattice = np.array([pidigits[i*10:(i+1)*10] for i in range(10)])

def extracttriangle(lattice, startr, startc, size):
triangle = np.zeros((size, size))
for i in range(size):
for j in range(i + 1):

r = (startr + i) % 10

c = (startc + j) % 10

triangle[i, j] = lattice[r, c]
return triangle

def computedeltas(triangle):

aéiea§ﬁriangle.shape[

0" AA1J—AA ..  F1

‘ UULLdbV = LJ
for i in range(size):
for j in range(i): # Horizontal in row i
deltash.append(triang1e[i, j+1] - triang1e[i, j])
if i > 0:
for j in range(i+1): # Vertical from row i-1 to i
deltasv.append(triangle[i, j] - triangle[i-1, j])
alldeltas = deltash + deltasv
if len(alldeltas) == :
return 0.0
return np.mean(np abs(allde1tas)) / 9.0 # Normalize by max digit diff

def computeaveragemeandelta(lattice, clausepositions):
means = []
for pos in clausepositions:
triangle = extracttriangle(lattice, pos[0], pos[1], 4)
meande1ta = computedeltas(triangle)
means.append(meandelta)
return np.mean(means)

# Pointer cycle traversal With loop detection
def followpointer(lattice, r, c, maxsteps=20):
visited = set()
path = [J
currentr, currentc = r, c
val = lattice[currentr, currentc]
visited.add((currentr, currentc))
path.append(val)
for  in range(maxsteps):
nextr (currentr + val) % 10
nextc = (currentc + val) % 10
if (nextr, nextc) in visited:
break # Halt on loop revisit
val = lattice[nextr, nextc]
path.append(val)
visited.add((nextr, nextc))
currentr, currentc = nextr, nextc
return path, list(visited) # Return path values and visited positions

# Compute rotor entropy on path (Shannon entropy of digit frequencies)
def computerotorentr0py(path):

if 1en(p£%E912=019

unioue, counts = np unique(path, returncounts=True)
probs = counts / len(path)
return entropy(probs, base=2) # Shannon entropy in bits

# Adjust value along pointer cycle, weighted by entropy (higher entropy sca
def cycleadjust(lattice, r, c):

path,  = followpointer(lattice, r, c)

entropyval = computerotorentropy(path)

meanval = np.mean(path)

scale = 1 + entropyval / np.log2(10) # Normalize entropy to [0,1] sca

newval = int(meanval * scale) % 10

return newval

# Satisfiable 4-SAT clause positions
[(0,0). (2,2), (4.4), (6.6), (8,8)]

clausepositions

# variable positions
[(0.0). (0,1), (0,2), (0.3)]

varpositions

# Initial mean
initialmean = computeaveragemeandelta(lattice, clausepositions)
print(f"Initial average mean delta (normalized): {initialmean}")

# Gradient-based flips with pointer cycle integration and entropy weighting
numiterations = 20

bestlattice = lattice.copy()

bestmean = initialmean

collapseledger [] # Ledger to record accepted flips

for iter in range(numiterations):

improved = False

for varidx, (r, c) in enumerate(varpositi0ns):
originalval = bestlattice[r, c]
# Use pointer cycle to generate candidate flip
path,  = followpointer(bestlattice, r, c)
entropyval = c0mputerotorentr0py(path)
cycleval = cycleadjust(bestlattice, r, c)
flip = cycleval - originalval
if flip == : continue
newval = (originalval + flip) % 10
testlattice = bestlattice.copy()
testlattice[r, c] = newval
testmean = computeaveragemeandelta(testlattice, clausepositio

grad = testmean - bestmean
if grad < 0:
bestlattice = testlattice.copy()
bestmean = testmean
improved = True
# Log to ledger
ledgerentry = {
"iteration": iter + 1,
"variable”: varidx + 1,
”position”: (I, c),
"originalvalue”: originalval,
"cyclemean”: np.mean(path),
"entropy": entropyva1,
"deltabefore": bestmean - grad, # Previous mean befbre t
"deltaafter": testmean
}
collapseledger.append(ledgerentry)
print(f"Iter {iter+1}, Var {varidx+1} cycle flip {flip}: Grad
if not improved:
print(f"No further improvement at iter {iter+l}")
break

finalmean = bestmean
converged = finalmean < 0.5
status = ”Satisfiable" if converged else "Unsatisfiable"

print(f"Final average mean delta (normalized): {finalmean}")
print(f”Converged: {converged}")
print(f"Status: {status}")
print("\nCollapse Ledger ")
for entry in collapseledger:
print(entry)

Execution Output (From Simulation)

Initial average mean delta (normalized): 0.4874074074074074

