from __future__ import division
from matplotlib import pyplot as plt


movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

xs = [i + 0.1 for i, _ in enumerate(movies)]

print xs

plt.bar(xs, num_oscars)

plt.ylabel("# of Academy Awards")
plt.title("My Favorite Movies")

plt.xticks([i + 0.5 for i, _ in enumerate(movies)], movies)

plt.show()







