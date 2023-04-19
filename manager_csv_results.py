import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'score_data.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and rainfall amounts from this file.
    score, assessment_id = [], []
    for row in reader:
        
        score.append(score)
        assessment_id = float(row[3])
        assessment_id.append(assessment_id)

# Plot the rainfall amounts.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, precips, c='blue')

# Format plot.
plt.title("Daily Rainfall Amounts - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Rainfall (in)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()