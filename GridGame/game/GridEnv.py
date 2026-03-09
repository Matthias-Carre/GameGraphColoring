"""
class used for rl with step / reset / encode / mask
"""
import torch
import numpy as np
class GridEnv:
    def __init__(self,engine):
        self.engine = engine
        self.grid = engine.grid
        self.max_colors = self.grid.max_colors
        self.width = self.grid.width
        self.height = self.grid.height

    """
    input : action (x,y,color)
    out : void
    result : play the move on the grid and update the interface
    """
    def step(self, action):
        x, y, color = action
    

    """
    input : void
    out : void
    result : reset the grid and update the interface
    """
    def reset(self):
        self.engine.reset()


    """
    input : void
    out : state representation of the grid
    result : return a representation of the grid state
    """
    def encode_state(self):
        return None
    
    """
    input : state representation of the grid
    out : 
    """
    def decode_state(self, state):
        return None
    
    """
    input : void
    out : list of legal actions
    result : return a list of legal actions for the current player
    """
    def legal_actions(self):
        return None