import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import lineStyles

df = pd.read_csv('avgIQpercountry.csv')

filtered_df = df[df["Average IQ"] >= 18]

filtered_df = filtered_df.sort_values(by='Average IQ', ascending=False)

print(filtered_df)

plt.figure(figsize=(14,8))

bars = plt.bar(filtered_df['Country'],filtered_df['Age'],filtered_df['Avarage IQ'], color='skyblue')

plt.title("Average IQ by country (IQ >= 100)", fontsize=16)

plt.xlabel('County',fontsize=14)
plt.ylabel('IQ', fontsize=14)

plt.xticks(rotation=90, fomntsize=10)
plt.yticks(fontsize=10)

plt.grid(axis='y', lineStyle='--', alpha=0.8)
plt.bar_label(bars, fontsize=10, color='black')

plt.tight_layout()
plt.show()