import json
import matplotlib.pyplot as plt

# Import dataset
with open('songdata.json') as f:
    data = json.load(f)

# Initialize lists
songsabove8 = []
songsbelow8 = []

# Separate songs into two lists based on loudness
for song in data:
    if song['loudness'] < -8:
        songsbelow8.append(song)
    else:
        songsabove8.append(song)

# Extract tempo values
tempo_above8 = [song['tempo'] for song in songsabove8]
tempo_below8 = [song['tempo'] for song in songsbelow8]

# Create histograms
plt.hist(tempo_below8, bins=50, alpha=0.5, color='g')
plt.xlabel('Tempo')
plt.ylabel('Count')
plt.title('Tempo distribution for songs with loudness below -8')
plt.savefig('hist1.png')
plt.clf()

plt.hist(tempo_above8, bins=50, alpha=0.5, color='b')
plt.xlabel('Tempo')
plt.ylabel('Count')
plt.title('Tempo distribution for songs with loudness above or equal to -8')
plt.savefig('hist2.png')