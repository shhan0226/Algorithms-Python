#pip install googletrans
from googletrans import Translator
translator = Translator()
Eng_src = 'Human is Good'
src = 'En'
dest = 'Ko'

tr_re = translator.translate(Eng_src, src=src, dest=dest)
print ('String(', tr_re.src, ') :', Eng_src)
print ('Trans(', tr_re.dest, ') :', tr_re.text, '\n')

import googletrans
print ('번역 가능 언어: ', googletrans.LANGUAGES, '\n')

#service URL 변경
translator = Translator(service_urls=[
      'translate.google.com',
      'translate.google.co.kr',
    ])

#list로 문장 번역
translations = translator.translate(['The quick brown fox', 'jumps over', 'the lazy dog'], dest='ko')
for translation in translations:
    print (translation.origin, ' -> ', translation.text)
print('\n')

#언어탐색
print (translator.detect('이 문장은 한글로 쓰여졌습니다.'))


