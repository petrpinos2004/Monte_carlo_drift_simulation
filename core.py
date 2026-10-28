import numpy as np
from tqdm import tqdm

#####################################################################
# Define Simulation class
#####################################################################

class Simulation:

    def __init__(self, container):

        self.name = f"E_d_N_{container['ratio']}"
        self.position = container['position']

        #Parameter values
        self.ratio = container['ratio'] * 1e-21  # E/N in Td
        self.sigma = container['sigma']
        self.m_gas = container['m_gas']
        self.m_e = container['m_e']
        self.e = container['e']
        self.T = container['T']
        self.N = container['N']
        self.density = 1e20
        self.warmup_N = container['warmup_N']
        self.kB = container['kb']

        #Derived values
        self.a = (self.e * self.ratio * self.density) / self.m_e   #electorn acceleration by electric field

        #Bounds
        self.v_max = 1.0e6 + container['ratio'] * 5.0e5
        self.f_max = self.density * self.sigma * self.v_max

        #Initial conditions
        self.r = np.zeros(3)
        self.v = np.zeros(3)
        self.time = 0
        self.z = 0

        print(f'Running simulation {self.name}')

    def free_fly_time(self):

        return -np.log(np.random.rand()) / self.f_max

    def p_real_collision(self):

        return np.linalg.norm(self.v) / self.v_max

    def v_gas(self):

        return np.random.normal(0.0, np.sqrt(self.kB * self.T / self.m_gas), 3)  #Maxwell distribution for gas at temperature self.T

    def move_in_z(self, t):

        self.r[2] += self.v[2] * t + 0.5 * self.a * t**2
        self.v[2] += self.a * t
        self.time += t

    def elastic_collision(self):

        v_gas = self.v_gas()
        relative_v = self.v - v_gas
        relative_v_norm = np.linalg.norm(relative_v)
        costheta = 2.0 * np.random.rand() - 1.0
        sintheta = np.sqrt(1.0 - costheta**2)
        phi = 2.0 * np.pi * np.random.rand()
        g_prime = (relative_v_norm * np.array([sintheta * np.cos(phi), sintheta * np.sin(phi), costheta]))
        self.v = (self.m_e * self.v + self.m_gas * v_gas) / (self.m_e + self.m_gas) + (self.m_gas / (self.m_e + self.m_gas)) * g_prime
        
    def run(self, j=0):

        for i in tqdm(range(int(self.N)), desc=f"Simulating {self.name}", position=self.position):

            t = self.free_fly_time()
            self.move_in_z(t)
            p = self.p_real_collision()

            if np.random.rand() < p:
                self.elastic_collision()    
            else:
                #Null-collision
                pass

            if i == self.warmup_N:
                self.r[2] = 0.0
                self.time = 0.0

        print(f'Simulation {self.name}_{j} finished with drift velocity {self.r[2]/self.time}')

        with open(f'{self.name}_v2.txt', "a") as f:
            f.write(str(self.r[2]/self.time))
            f.write('\n')

    def sum_up(self):
        
        data = np.loadtxt(f'{self.name}_v2.txt')
        n = len(data)

        print('--------------------------------------------------------------------')
        print(f'Final drift velocity for {self.name} is {np.mean(data)}+-{np.std(data)/np.sqrt(n)}') 
        print('--------------------------------------------------------------------')


