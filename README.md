# Monte_carlo_drift_simulation
This is a school related project on Monte Carlo simulation of electron drifting in homogeneous electric field.

The program should be run from the project root directory using provided 'run_all.sh' shell script. 
This runs all three simulations (E/N = 10, E/N = 1, E/N = 0.1) in parallel. Simulations parameter specification is
handled using container inside Parameters class in respective python files (10.py, 1.py, 0p1.py). Each of these are 
initiated as child process of Simulation class (core.py) where the computional code is located.

Each simulation is by default run ten times with results from each run being saved in corresponding .txt file.
Rerunning the simulation does not clear previous results, new results are simply added after old ones.
To clear ouptputs use 'clean_up.sh' or manually switch export path.

By default this repository contains .txt results from 50 simulation runs with 1e7 collisions from which we got

E/D   \t  v_D
-----------------------
0.1   \t  1540 +- 10
-----------------------
1    \t   5200 +- 20
-----------------------
10   \t   16690 +- 80 
-----------------------

And v2.txt with 10 simulation runs with 1e8 collisions from which we got

E/D   \t  v_D
-----------------------
0.1   \t  1515 +- 7
-----------------------
1    \t   5230 +- 10
-----------------------
10   \t   16610 +- 50 
-----------------------

