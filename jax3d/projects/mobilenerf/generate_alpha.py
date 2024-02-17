from matplotlib import pyplot as plt
import os
import numpy as np
import sys
import matplotlib.cm as cm

path = sys.argv[1]
paths = os.listdir(path)

for p in paths:
    if p.startswith("s2_1_") and p.endswith(".png"):
        img = plt.imread(os.path.join(path, p))
        img = img[:, :, 0:3]
        alpha = (img[:, :, 0:3] == 1).sum(-1)
        alpha = alpha == 3                                 
        plt.imsave(os.path.join(path, "alpha_" + p), alpha.astype(bool), cmap=cm.gray)