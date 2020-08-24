from googletrans import Translator

translator = Translator()

src = 'En'
dest = 'Ko'


str_total=[]

def _file_():
    urls = []
    f = open("input", "rt", encoding='UTF8')
    lines = f.readlines()
    for line in lines:
        strs = line.strip("\n")
        str_total.append(strs)
    f.close()
    result_str = " ".join(str_total)
    return result_str




if __name__ == '__main__':
    str_=_file_()
    query = str_.replace(". ", ".\n")

#    res= isinstance(query, list)
#    print(res)

#    res = isinstance(query, str)
#    print(res)

    # list로 문장 번역
    translations = translator.translate(query.split("\n"), dest='ko')
    for translation in translations:
        print(translation.origin, ' \n ', translation.text, '\n')
    print('\n', "end.")
