import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_parquet("titanic.parquet", engine="pyarrow")
df.to_csv("output.csv", index=False)
survive = df.groupby('Pclass')['Survived'].mean() * 100
bars = plt.bar(survive.index, survive.values)
plt.title('Выживаемость пассажиров Титаника')
plt.xlabel('Класс билета')
plt.ylabel('Процент выживших (%)')
plt.xticks([1, 2, 3], ['Первый класс', 'Второй класс', 'Третий класс'])
plt.show()
