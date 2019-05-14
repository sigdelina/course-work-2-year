import re
import os

# создает таблицу
with open('sentences.csv', 'w', encoding='utf-8') as file:
    row = '%s\t%s\t%s\t%s\n'
    file.write(row % ('Path', 'Segment', 'Id', 'RR'))
path = './corpus_rs3/corpus/' # прописывает путь
# обходит дерево

text_str = ''
for root, dirs, files in os.walk(path):
    for file in files:
        counter = 0 # счетчик
        if ".rs3" in file: # для файлов с нужным расширением
            filename = str(file)
           # print(root, dirs, file)
            text_path = os.path.join(root, file)  # полный путь к файлу
            with open(text_path, encoding="utf-8") as file:
                all_text = file.read()
            #print(all_text)
            lines_text = all_text.splitlines()
            for i in range(len(lines_text)):
               # print(lines_text[i])
                if '<segment id' in lines_text[i]:
                    print(lines_text[i])
                    find_id = re.search(r'<segment id="(\d*)" ', lines_text[i], flags=re.DOTALL)
                    excluding = re.search(r'<.*relname="span".*', lines_text[i], flags=re.DOTALL)
                    if excluding is None:
                        id = find_id.group(1)
                        relation = re.search(r'relname="(\S*)">', lines_text[i], flags=re.DOTALL)
                        ryth_rel = relation.group(1)
                       # print(ryth_rel)
                        sent = re.search(r'<segment.*"(>.*)</segment>', lines_text[i], flags=re.DOTALL)
                        sentence = sent.group(1)
                      #  print(sentence)
                        text_str += str(sentence) + ' '
                        with open('sentences.csv', 'a', encoding='utf-8') as f:
                            row = '%s\t%s\t%s\t%s\n'
                            f.write(row % (text_path, sentence.replace('>', ' '), id, ryth_rel))
#print(text_str)
with open('text.txt', 'w', encoding='utf-8') as file:
    file.write(text_str)

new_string = ''
path = './corpus_txt/raw_corpus_texts' # прописывает путь
for root, dirs, files in os.walk(path):
    for file in files:
        counter = 0 # счетчик
        if ".txt" in file: # для файлов с нужным расширением
            filename = str(file)
            print(root, dirs, file)
            text_path_txt = os.path.join(root, file)  # полный путь к файлу
            with open(text_path_txt, encoding="utf-8") as file_2:
                full_text = file_2.read()
            new_string += full_text + ' '
print(new_string)
with open('news_corpora.txt', 'w', encoding='utf-8') as fi:
    fi.write(new_string)