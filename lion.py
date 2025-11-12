import docx
import matplotlib.pyplot as plt
import pandas as pd

doc = docx.Document('lion.docx')
text = ' '.join([k.text for k in doc.paragraphs])

nenad= '.,!?;:"()[]{}«»—1234567890'
for z in nenad:
    text = text.replace(z, '')

words = text.split()

slova= [ ]

buk= ['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я' ]

for i in words:
    if i not in slova:
        slova.append(i)

word_counts = {}

kolichestvo_slov = len(words)

for word in slova:
    count = words.count(word)
    word_counts[word] = count

spisok_slov = [(slovo, kolichestvo, (kolichestvo / kolichestvo_slov) * 100) for slovo, kolichestvo in word_counts.items()]
pd.DataFrame(spisok_slov, columns=['Слово', 'Количество', 'Частота (%)']).to_excel('slova.xlsx', index=False)  # сохраняем в Excel

buk_counts = {}

for wor in buk:
    coun = text.count(wor)
    buk_counts[wor] = coun

print(buk_counts)

plt.bar(buk_counts.keys(), buk_counts.values())  # создаем столбчатую диаграмму
plt.ylabel('Количество')  # подпись для  оси игрик
plt.xlabel('Буквы')  # подпись для горизонтальной оси икс
plt.show()  # показываем график

for bukva, kolichestvo in buk_counts.items():
    print(f"{bukva}: {kolichestvo}")  # печатаем статистику    
