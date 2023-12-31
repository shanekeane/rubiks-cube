import numpy as np
import matplotlib.pyplot as plt
import random
from copy import deepcopy
import pandas as pd

class Cube:
    """
    Defines a standard 3x3 Rubik's cube.
    
    Attributes
    ----------
    cube : defines a cube by listing the colours on each of six
           faces, in the order (centre cube colour):
           W, O, G, R, B, Y

    Methods
    -------
    set_solved                         : resets the cube to a solved state
    randomize                          : randomizes the current cube
    U, D, F, B, L, R, U_prime, D_prime,
    B_prime, L_prime, R_prime, U_prime : Functions to turn corresponding
                                         cube face (standard notation)
    plot                               : outputs the cube

    """
    
    def __init__(self, solved = True):
        self.cube = np.zeros((6, 3, 3), dtype='str')
        self.set_solved()
        if solved == False:
            self.randomize()
        
    def set_solved(self):
        colours = ('W', 'O', 'G', 'R', 'B', 'Y')
        for face in range(6):
            self.cube[face] = colours[face]
        return self
            
    def randomize(self):
        possible_moves = (self.U, self.U_prime, self.D, self.D_prime,
                          self.L, self.L_prime, self.R, self.R_prime,
                          self.F, self.F_prime, self.B, self.B_prime)
        number_of_moves = np.random.choice(51)+50 #choose 50-100 moves
        moves = random.choices(possible_moves, k=number_of_moves)

        for move in moves:
            move()

        return self
            
    def _turn_face_clockwise(self, face):
        #To be called when using face-turning functions
        i = [[2,1,0],[2,1,0],[2,1,0]]
        j = [[0,0,0],[1,1,1],[2,2,2]]
        return face[i,j]

    def _turn_face_anticlockwise(self, face):
        #To be called when using face-turning functions
        i = [[0,1,2],[0,1,2],[0,1,2]]
        j = [[2,2,2],[1,1,1],[0,0,0]]
        return face[i,j] 
    
    def F(self):
        cube_orig = deepcopy(self.cube)
        self.cube[0,2,:], self.cube[1,:,2], self.cube[5,0,:], self.cube[3,:,0] \
        = np.flip(cube_orig[1,:,2],0),cube_orig[5,0,:], np.flip(cube_orig[3,:,0], 0), cube_orig[0,2,:]
        self.cube[2] = self._turn_face_clockwise(cube_orig[2])
        return self

    def F_prime(self):
        cube_orig = deepcopy(self.cube)
        self.cube[0,2,:], self.cube[3,:,0], self.cube[5,0,:], self.cube[1,:,2] \
        = cube_orig[3,:,0], np.flip(cube_orig[5,0,:], 0), cube_orig[1,:,2], np.flip(cube_orig[0,2,:],0)
        self.cube[2] = self._turn_face_anticlockwise(cube_orig[2])
        return self

    def B(self):
        cube_orig = deepcopy(self.cube)
        self.cube[0,0,:], self.cube[3,:,2], self.cube[5,2,:], self.cube[1,:,0] \
        = cube_orig[3,:,2], np.flip(cube_orig[5,2,:], 0), cube_orig[1,:,0], np.flip(cube_orig[0,0,:], 0)
        self.cube[4] = self._turn_face_clockwise(cube_orig[4])
        return self

    def B_prime(self):
        cube_orig = deepcopy(self.cube)
        self.cube[0,0,:], self.cube[3,:,2], self.cube[5,2,:], self.cube[1,:,0] \
        = np.flip(cube_orig[1,:,0], 0), cube_orig[0,0,:], np.flip(cube_orig[3,:,2],0), cube_orig[5,2,:]
        self.cube[4] = self._turn_face_anticlockwise(cube_orig[4])
        return self
        
    def L(self):
        cube_orig = deepcopy(self.cube)
        self.cube[0,:,0], self.cube[2,:,0], self.cube[5,:,0], self.cube[4,:,2] \
        = np.flip(cube_orig[4,:,2], 0), cube_orig[0,:,0], cube_orig[2,:,0], np.flip(cube_orig[5,:,0], 0)
        self.cube[1] = self._turn_face_clockwise(cube_orig[1])
        return self
        
    def L_prime(self):
        cube_orig = deepcopy(self.cube)
        self.cube[0,:,0], self.cube[2,:,0], self.cube[5,:,0], self.cube[4,:,2] \
        = cube_orig[2,:,0], cube_orig[5,:,0], np.flip(cube_orig[4,:,2],0), np.flip(cube_orig[0,:,0], 0)
        self.cube[1] = self._turn_face_anticlockwise(cube_orig[1])
        return self

    def R(self):
        cube_orig = deepcopy(self.cube)
        self.cube[0,:,2], self.cube[2,:,2], self.cube[5,:,2], self.cube[4,:,0] \
        = cube_orig[2,:,2], cube_orig[5,:,2], np.flip(cube_orig[4,:,0], 0), np.flip(cube_orig[0,:,2], 0)
        self.cube[3] = self._turn_face_clockwise(cube_orig[3])
        return self

    def R_prime(self):
        cube_orig = deepcopy(self.cube)
        self.cube[0,:,2], self.cube[2,:,2], self.cube[5,:,2], self.cube[4,:,0] \
        = np.flip(cube_orig[4,:,0], 0), cube_orig[0,:,2], cube_orig[2,:,2], np.flip(cube_orig[5,:,2], 0)
        self.cube[3] = self._turn_face_anticlockwise(cube_orig[3])
        return self

    def U(self):
        cube_orig = deepcopy(self.cube)
        self.cube[1,0,:], self.cube[2,0,:], self.cube[3,0,:], self.cube[4,0,:] \
        = cube_orig[2,0,:], cube_orig[3,0,:], cube_orig[4,0,:], cube_orig[1,0,:]
        self.cube[0] = self._turn_face_clockwise(cube_orig[0])
        return self

    def U_prime(self):
        cube_orig = deepcopy(self.cube)
        self.cube[1,0,:], self.cube[2,0,:], self.cube[3,0,:], self.cube[4,0,:] \
        = cube_orig[4,0,:], cube_orig[1,0,:], cube_orig[2,0,:], cube_orig[3,0,:]
        self.cube[0] = self._turn_face_anticlockwise(cube_orig[0])
        return self

    def D(self):
        cube_orig = deepcopy(self.cube)
        self.cube[1,2,:], self.cube[2,2,:], self.cube[3,2,:], self.cube[4,2,:] \
        = cube_orig[4,2,:], cube_orig[1,2,:], cube_orig[2,2,:], cube_orig[3,2,:]
        self.cube[5] = self._turn_face_clockwise(cube_orig[5])
        return self

    def D_prime(self):
        cube_orig = deepcopy(self.cube)
        self.cube[1,2,:], self.cube[2,2,:], self.cube[3,2,:], self.cube[4,2,:] \
        = cube_orig[2,2,:], cube_orig[3,2,:], cube_orig[4,2,:], cube_orig[1,2,:]
        self.cube[5] = self._turn_face_anticlockwise(cube_orig[5]) 
        return self
        
    def _convert_colour_to_numerical(self, colour_array):
        #Converts a face of colours to RGB format for plotting
        COLOUR_SERIES = pd.Series(data = [np.array([255,255,255], dtype=np.uint8), 
                                          np.array([183, 18, 52], dtype=np.uint8),
                                          np.array([0, 70, 173], dtype=np.uint8), 
                                          np.array([255,88, 0], dtype=np.uint8),
                                          np.array([0, 155, 72], dtype=np.uint8), 
                                          np.array([255, 213, 0], dtype=np.uint8)],
                              index = ['W', 'R', 'B', 'O', 'G', 'Y'])

        out_shape = colour_array.shape + (3,)
        return np.stack(COLOUR_SERIES[colour_array.flatten()].to_numpy(), axis=0, dtype=np.uint8).reshape(out_shape)

    def plot(self):
        fig, ax = plt.subplots(3,4)

        for a in ax.ravel():
            a.tick_params(left=False)
            a.tick_params(bottom=False)
            a.set_xticks([])
            a.set_yticks([])

        plt.subplots_adjust(wspace=0, hspace=0)
        ax[0,0].remove()
        ax[0,2].remove()
        ax[0,3].remove()
        ax[2,0].remove()
        ax[2,2].remove()
        ax[2,3].remove()
        ax[0,1].pcolormesh(self._convert_colour_to_numerical(self.cube[0]), edgecolors='k', linewidth=0.5)
        ax[0,1].invert_yaxis()
        ax[1,0].pcolormesh(self._convert_colour_to_numerical(self.cube[1]), edgecolors='k', linewidth=0.5)
        ax[1,0].invert_yaxis()
        ax[1,1].pcolormesh(self._convert_colour_to_numerical(self.cube[2]), edgecolors='k', linewidth=0.5)
        ax[1,1].invert_yaxis()
        ax[1,2].pcolormesh(self._convert_colour_to_numerical(self.cube[3]), edgecolors='k', linewidth=0.5)
        ax[1,2].invert_yaxis()
        ax[1,3].pcolormesh(self._convert_colour_to_numerical(self.cube[4]), edgecolors='k', linewidth=0.5)
        ax[1,3].invert_yaxis()
        ax[2,1].pcolormesh(self._convert_colour_to_numerical(self.cube[5]), edgecolors='k', linewidth=0.5)
        ax[2,1].invert_yaxis()
