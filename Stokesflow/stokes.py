import numpy as np
from numpy import linalg as LA
from numpy import pi
import pandas as pd
import pickle

class Stokes():
    
    def __init__(self,
                 resolusion, 
                 force_point,
                 force_power,
                 force_vector,
                 x_range,
                 y_range,
                 z_range
                ):
         
        x = np.linspace(x_range[0], x_range[1], resolusion)
        y = np.linspace(y_range[0], y_range[1], resolusion)
        z = np.linspace(z_range[0], z_range[1], resolusion)

        X, Y, Z = np.meshgrid(x, y, z)
      
        self.x = X.flatten()
        self.y = Y.flatten()
        self.z = Z.flatten()
        
        self.position = np.stack([self.x, self.y, self.z], 1)
         
        self.force = force_vector * force_power
        
        print(self.force)

        self.force_point = force_point

    def ossen(self, num_id):

        vector = self.position[num_id] - self.force_point
        norm = LA.norm(vector)
        
        tensor = np.outer(vector, vector) / (norm**3)
        
        ossen_tensor = ((np.eye(3) / norm) + tensor)/(8 * pi)
        return ossen_tensor

    def calc_v(self, num_id):
        ossen_tensor = self.ossen(num_id)
        v = np.dot(ossen_tensor, self.force)
        return v 
    
if __name__ == "__main__":
    stokes = Stokes(10, [0, 0, 0] ,5 ,np.array([0.3, 0.4, 0.5]) ,[-10,10] ,[-10,10] ,[-10,10])
    
    print(stokes.ossen(0))
    print(f"velocity : {stokes.calc_v(0)}")

    print(len(stokes.position))
    
