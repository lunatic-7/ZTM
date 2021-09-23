# Translate  (Exercise)

from translate import Translator

translator = Translator(to_lang='hin')
translation = translator.translate('This is a pen')
print(translation)

try:
    with open('./test.txt', mode='r') as my_file:
        translator = Translator(to_lang='ja')
        text = my_file.read()
        translation = translator.translate(text)
        with open('./test_ja.txt', mode='w', encoding='utf-8') as my_file2:  # To create a new translated file.
            my_file2.write(translation)
except FileNotFoundError as err:
    print('there is no such file')
