import nltk
from nltk import text
#마침표와 구두점 등으로 구분하여 토큰화 하는것 
nltk.download('punkt')
from nltk.tokenize import word_tokenize

text = 'Brad Pitt is a good actor'
word_tokens =word_tokenize(text)
print(word_tokens) 

#알파벳이 아닌 문자를 구분하여 토큰화
from nltk.tokenize import WordPunctTokenizer

text = 'Brad Pitt is a good actor'
wordPuncttoken = WordPunctTokenizer().tokenize(text)
print(wordPuncttoken)

#정규표현식에 기반한 토큰화
from nltk.tokenize import TreebankWordTokenizer

text = 'Brad Pitt is a good actor'
treebankwordtoken = TreebankWordTokenizer().tokenize(text)
print(treebankwordtoken)

#영문품사 부착
from nltk import pos_tag
nltk.download('averaged_perceptron_tagger')
taggedToken = pos_tag(['I','am','a','good','actor'])
print(taggedToken)

#개체명 인식
nltk.download('words')
nltk.download('maxent_ne_chunker')
from nltk import ne_chunk
neToken = ne_chunk(taggedToken)
print(neToken)

#원형 복원
from nltk.stem import PorterStemmer
ps = PorterStemmer()

print(ps.stem('running'))

#표제어 추출
from nltk.stem import WordNetLemmatizer
wl = WordNetLemmatizer()
print(wl.lemmatize('running'))

#불용어 처리
from collections import Counter
Counter(taggedToken).most_common()

#한글 전처리 실습
#conda install konlpy
from konlpy.tag import komoran