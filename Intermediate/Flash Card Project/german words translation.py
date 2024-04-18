from googletrans import Translator
import pandas

translator = Translator()

with open("Intermediate/Flash Card Project/data/de_50k.txt", "r") as german_words:
    list = german_words.readlines()
    new_list = [word.partition(' ')[0] for word in list]
    translated_list = []
    for word in new_list:
        translated_word = translator.translate(word).text
        translated_list.append(translated_word)
        print(new_list.index(word))
    
    df = pandas.DataFrame(new_list, columns=["word"])
    df.insert(1,"translation",translated_list,True)
    df.to_csv("Intermediate/Flash Card Project/data/german_words.csv", index=False)
    
    
    

