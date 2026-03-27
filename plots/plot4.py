import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import numpy as np

# for usability steps
data_dict = {
    'Manager / Browser': ['LastPass', 'Avira', '1Password', 'Bitwarden', 'NordPass',
                          'Dashlane', 'Keeper', 'RoboForm', 'Proton', 'DualSafe',
                          'Chrome', 'Edge', 'Firefox'],
    'Save New': [1, 1, 3, 1, 1, 2, 1, np.nan, np.nan, np.nan, 1, 1, 1],
    'Manual Save': [9, 10, 11, 9, 9, 10, 11, 10, 9, 8, 11, 12, 11],
    'Auto-Fill': [0, 0, 2, 2, 2, 2, 1, 1, 2, np.nan, 0, 0, 2],
    'Manual Fill': [12, 12, 10, 12, 12, 8, 12, 14, 10, 12, 15, 15, 15],
    'Auto Update': [np.nan, 1, 1, 1, 1, 1, np.nan, np.nan, np.nan, np.nan, 1, 1, 1]
}

df_steps = pd.DataFrame(data_dict)
df_steps.set_index('Manager / Browser', inplace=True)
df_steps.columns = ['Auto Save', 'Manual Save', 'Auto Fill', 'Manual Fill', 'Auto Update']

plt.figure(figsize=(7, 7))
orig_cmap = plt.cm.Oranges
colors = orig_cmap(np.linspace(0, 0.6, 256))
new_cmap = LinearSegmentedColormap.from_list('usability_cmap', colors)

ax = sns.heatmap(df_steps,
                 annot=True,
                 fmt=".0f",
                 cmap=new_cmap,
                 annot_kws={'fontsize': 9},
                 vmin=0, vmax=15,
                 cbar_kws={'label': 'Number of Steps', 'ticks': [0, 3, 6, 9, 12, 15]},
                 linewidths=1,
                 linecolor='white')

# customise labels
plt.xlabel('')
ax.set_xticklabels(['Auto Save', 'Manual Save', 'Auto Fill', 'Manual Fill', 'Auto Update'],
                   fontsize=10, rotation=0, ha='center')
ax.xaxis.set_label_coords(0.5, 1.05)
ax.set_yticklabels(ax.get_yticklabels(), rotation=30, fontsize=10, ha='right', va='center_baseline',
                   rotation_mode='anchor')
ax.axhline(y=9, color='white', linewidth=7)  # thick separator line

plt.tight_layout()
plt.show()
