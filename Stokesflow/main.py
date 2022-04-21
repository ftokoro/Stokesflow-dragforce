import numpy as np
import pandas as pd
import stokes 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from tqdm import tqdm

resolusion = 8
force_point = np.array([0, 0, 0])
force_power = 5
force_vector = np.array([1, 0, 0])

x_range = [-10, 10]
y_range = [-10, 10]
z_range = [-10, 10]
 
Stokeslet = stokes.Stokes(resolusion = resolusion,
                          force_point = force_point,
                          force_power = force_power,
                          force_vector = force_vector,
                          x_range = x_range, 
                          y_range = y_range, 
                          z_range = z_range
                          )




if __name__ == '__main__':
    velocity = []
    for num_id in tqdm(range(len(Stokeslet.position))):
        v = Stokeslet.calc_v(num_id)
        velocity.append(v)

    df_position = pd.DataFrame(Stokeslet.position, columns = ["x", "y", "z"])
    df_velocity = pd.DataFrame(velocity, columns = ["vx", "vy", "vz"])
    print(df_position)
    print(df_velocity)
    
    fig = plt.figure()
    ax = Axes3D(fig)
    
    ax.scatter(force_point[0], force_point[1], force_point[2], s=100, c='r')
    ax.quiver(force_point[0], force_point[1], force_point[2],
              force_vector[0], force_vector[1], force_vector[2], color='red',length = force_power)

    #ax.scatter(df_position["x"], df_position["y"], df_position["z"],s=1, c='b')
    ax.quiver(df_position["x"], df_position["y"], df_position["z"],
              df_velocity["vx"], df_velocity["vy"], df_velocity["vz"],
              color="blue", length=10, arrow_length_ratio=0.5)

    fig.savefig('flow.pdf')





