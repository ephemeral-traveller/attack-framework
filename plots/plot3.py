import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# for active simulation attacks
data_dict = {
    'Manager / Browser': ['LastPass', 'Avira', '1Password', 'Bitwarden', 'NordPass',
                          'Dashlane', 'Keeper', 'RoboForm', 'Proton',
                          'Chrome', 'Edge', 'Firefox'],
    'CROS': [4, 1, 3, 2, 2, 2, 4, 3, 2, 4, 4, 2],
    'XSS': [4, 4, -1, 2, -1, -1, 2, 1, -1, 4, 4, 2],
    'Clickjacking (Same-Origin)': [4, 4, 3, 2, 2, 2, 4, 2, -1, 2, 2, 2],
    'Clickjacking (Cross-Origin)': [0, 2, -1, 0, -1, 4, -1, 2, -1, 4, 4, 2]
}

df = pd.DataFrame(data_dict)
df.set_index('Manager / Browser', inplace=True)

# create the heatmap
plt.figure(figsize=(9, 9))
orig_cmap = plt.cm.Purples
colors = orig_cmap(np.linspace(0, 0.7, 256))
new_cmap = LinearSegmentedColormap.from_list('light_blues', colors)

ax = sns.heatmap(df,
                 annot=False,
                 cmap=new_cmap,
                 vmin=-1.5, vmax=4.5,
                 cbar_kws={'label': 'Behaviour Level', 'ticks': [-1, 0, 1, 2, 3, 4]},
                 linewidths=1,
                 linecolor='white')

# customise labels and appearance
plt.xlabel('')
ax.set_xticklabels(['CROS', 'XSS', 'Clickjacking\n(Same-Origin)', 'Clickjacking\n(Cross-Origin)'],
                   fontsize=10, rotation=0, ha='center')
ax.xaxis.set_label_coords(0.5, 1.05)
ax.set_yticklabels(ax.get_yticklabels(), rotation=30, fontsize=10, ha='right', va='center_baseline',
                   rotation_mode='anchor')
ax.axhline(y=9, color='white', linewidth=7)  # thick separator line

# add custom text annotations for each cell
text_map = {
    4: "Autofill",
    3: "Req. Action\nAuto Submit",
    2: "Req. Action",
    1: "Req. Action\nFill Username",
    0: "Req. Action\nWarning",
    -1: "Disabled"
}
for i, manager in enumerate(df.index):
    for j, scenario in enumerate(df.columns):
        value = df.iloc[i, j]
        text = text_map.get(value, "")
        ax.text(j + 0.5, i + 0.5, text,
                ha='center', va='center',
                fontsize=9,
                color='black' if value != -1 else 'dimgray',
                fontweight='normal')

plt.tight_layout(pad=2.0)
plt.subplots_adjust(bottom=0.15)
plt.show()
