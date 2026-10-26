import core

#####################################################################
# Define Parameters class
#####################################################################

class Parameters(core.Simulation):

    def __init__(self):

        container = {
            'ratio' : 0.1,
            'sigma' : 6e-20,
            'm_gas' : 4*1.66e-27,
            'm_e' : 9.1e-31,
            'e' : 1.602e-19,
            'T' : 300,
            'N' : 1e7,
            'warmup_N' : 1e5,
            'kb' : 1.38e-23,
            'position' : 0
        }

        super().__init__(container)

#####################################################################
# Simulation execution
#####################################################################

for i in range(10):
    Simulation =  Parameters()
    Simulation.run(i)
Simulation.sum_up()
    