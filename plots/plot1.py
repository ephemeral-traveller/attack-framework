import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap

# define the data
data_dict = {
    'Manager / Browser': ['LastPass', 'Avira', '1Password', 'Bitwarden', 'NordPass',
                          'Dashlane', 'Keeper', 'RoboForm', 'Proton',
                          'Chrome', 'Edge', 'Firefox'],
    'Valid HTTPS': [0, 0, 3, 1, 1, 1, 0, 3, 1, 0, 0, 1],
    'Invalid HTTPS': [0, 0, 3, 1, 1, 1, 0, 3, 1, -1, -1, -1],
    'HTTP (Plaintext)': [1, 1, 3, 1, 1, 1, 1, 3, 1, 0, 0, 1]
}

df = pd.DataFrame(data_dict)
df.set_index('Manager / Browser', inplace=True)

# create the heatmap
plt.figure(figsize=(8, 9))
orig_cmap = plt.cm.Blues
colors = orig_cmap(np.linspace(0, 0.8, 256))
new_cmap = LinearSegmentedColormap.from_list('light_blues', colors)

ax = sns.heatmap(df,
                 annot=False,
                 cmap=new_cmap,
                 vmin=-1.5, vmax=3.5,
                 cbar_kws={'label': 'Autofill Behaviour Level', 'ticks': [-1, 0, 1, 2, 3]},
                 linewidths=1,
                 linecolor='white')

# customise labels and appearance
plt.xlabel('')
ax.set_xticklabels(['HTTPS\n(Secure)', 'HTTPS\n(Bad Certificate)', 'HTTP\n(Plaintext)'],
                   fontsize=10, rotation=0, ha='center')
ax.xaxis.set_label_coords(0.5, 1.05)
ax.set_yticklabels(ax.get_yticklabels(), rotation=30, fontsize=10, ha='right', va='center_baseline',
                   rotation_mode='anchor')
ax.axhline(y=9, color='white', linewidth=7)  # thick separator line

# custom text annotations for each cell
text_map = {
    3: "Req. Action\nAuto Submit",
    2: "Req. Action\nPartial Fill (Username)",
    1: "Req. Action",
    0: "Autofill",
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

plt.tight_layout(pad=1.0)
plt.show()
