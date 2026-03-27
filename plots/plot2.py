import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import numpy as np

# for the merged base techniques and field types
base_techniques = [
    'opacity:0', 'overlay covered', 'transform', 'content-visibility', 'z-index',
    'pointer-events', 'backface-visibility', 'visibility:collapse',
    'off-screen', 'ancestor overflow', 'clip (legacy)',
    'clip-path', 'font-size:0', 'width/height:0', 'tiny (1px)',
    'width/height:0', 'display:none', 'visibility:hidden'
]
field_types = ['Password', 'Credit Card (CVV)', 'Personal Info (Address)']

# the frequency data matrix
frequency_data_merged = [
    [25.0, 40.0, 0.0],
    [25.0, 10.0, 9.1],
    [16.7, 30.0, 9.1],
    [25.0, 10.0, 9.1],
    [25.0, 10.0, 18.2],
    [25.0, 10.0, 0.0],
    [16.7, 0.0, 9.1],
    [8.3, 0.0, 0.0],
    [8.3, 30.0, 0.0],
    [16.7, 40.0, 18.2],
    [8.3, 0.0, 9.1],
    [16.7, 40.0, 9.1],
    [8.3, 0.0, 9.1],
    [8.3, 0.0, 9.1],
    [8.3, 0.0, 9.1],
    [0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0]
]

df_freq_merged = pd.DataFrame(frequency_data_merged, index=base_techniques, columns=field_types)

# create the heatmap
plt.figure(figsize=(8, 11))
orig_cmap = plt.cm.Oranges
colors = orig_cmap(np.linspace(0, 0.8, 256))
new_cmap = LinearSegmentedColormap.from_list('light_blues', colors)

ax = sns.heatmap(df_freq_merged,
                 annot=True,
                 fmt=".1f",
                 cmap=new_cmap,
                 vmin=0, vmax=100,
                 cbar_kws={'label': 'Detection Frequency (%) - HTTPS Only', 'ticks': [0, 25, 50, 75, 100]},
                 linewidths=1,
                 linecolor='white')

# customise labels
plt.xlabel('')
ax.set_xticklabels(['Password', 'Credit Card', 'Personal Info'],
                   fontsize=10, rotation=0, ha='center')
ax.xaxis.set_label_coords(0.5, 1.05)
ax.set_yticklabels(ax.get_yticklabels(), rotation=30, fontsize=10, ha='right', va='center_baseline',
                   rotation_mode='anchor')

# add a y-axis label for the hidden techniques
ax.text(-0.3, 0.5, 'Hidden Techniques',
        ha='center', va='center',
        rotation=90, fontweight='normal', transform=ax.transAxes)

plt.tight_layout()
plt.show()
