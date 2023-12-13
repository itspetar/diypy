import numpy as np
import os
from matplotlib import pyplot as plt
import matplotlib.colors as mcolors
from cmcrameri import cm

#%%

def make_cmap(rgb_path):
    rgb_values = []
    with open(rgb_path, 'r') as file:
        for line in file:
            if line.startswith('#') or line.startswith('ncolors'):
                continue
            try:
                r, g, b = map(float, line.strip().split())
                rgb_values.append((r, g, b))
            except ValueError:
                print('Skipping invalid line: {}'.format(line.strip()))
    cmap = mcolors.LinearSegmentedColormap.from_list(os.path.splitext(os.path.basename(rgb_path))[0], rgb_values)
    return cmap
# cmap_cividis = make_cmap(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cividis.rgb'))

def imshow_with_cbar(
    fig, ax, data, cmap=cm.batlow, vmin=None, vmax=None, cmap_type='sequential', title_str=None, ticks='off', labels=['x', 'y']
    ):
    if vmin == None:
        vmin = data.min()
    if vmax == None:
        vmax = data.max()
    
    if cmap_type == 'diverging':
        cmap = cm.roma
    elif cmap_type == 'cyclic':
        cmap = cm.romaO
    else:
        cmap = cm.batlow
    
    if ticks != 'on':
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_xticklabels([])
        ax.set_yticklabels([])
    
    cax = ax.imshow(data, cmap=cmap, vmin=vmin, vmax=vmax)
    ax.axis('scaled')

    if title_str is not None:
        ax.set_title(title_str)

    ax.set_xlabel(labels[0])
    ax.set_ylabel(labels[1])

    fig.colorbar(cax, ax=ax)
    fig.tight_layout()

    return (fig, ax)