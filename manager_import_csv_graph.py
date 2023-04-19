import csv
import numpy as np
from collections import Counter
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

with open('score_data.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    language_counter = Counter()
    
    for row in csv_reader:
        language_counter.update(row['score'].split(';'))


score = []
popularity = []     

for item in language_counter:
    score.append(item[0])
    popularity.append(item[1])

plt.bar(score, popularity)

plt.title("Most popular score")
plt.xlabel("Competencies")
plt.ylabel("Backend")

plt.tight_layout()

plt.show()
