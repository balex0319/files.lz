from collections import Counter 
import matplotlib.pyplot as plt
import pandas as pd 
import docx 
import re
file_path = 'lion.docx'
doc = docx.Document(file_path)
text = []
for paragraph in doc.paragraphs:
 text.append(paragraph.text) 
full_text = ' '.join(text)
words = re.findall(r'\b\w+\b', full_text.lower()) 
word_count = Counter(words)
total_words = sum(word_count.values()) 
df_words = pd.DataFrame(word_count.items(), columns=['Слово', 'Частота'])
df_words['Процент'] = (df_words['Частота'] / total_words) * 100 
print(df_words)
output_file_words = 'word_frequency.csv' 
df_words.to_csv(output_file_words, index=False, encoding='utf-8')
print(f'Результаты частоты слов сохранены в файл: {output_file_words}')
letters = re.findall(r'[а-яА-ЯёЁ]', full_text.lower()) 
letter_count = Counter(letters)
df_letters = pd.DataFrame(letter_count.items(), columns=['Буква', 'Частота']) 
total_letters = sum(letter_count.values()) 
df_letters['Процент'] = (df_letters['Частота'] / total_letters) * 100 
plt.bar(df_letters['Буква'], df_letters['Частота'])                               
plt.title('Частота встречаемости букв') 
plt.xlabel('Буквы')                         
plt.ylabel('Частота')                         
plt.grid(axis='y') 
plt.tight_layout() 
plt.show() 


