# https://web.dio.me/course/seguranca-da-informacao-com-python/learning/28e5acce-837b-424c-8d07-2880f4c9c20f
import requests
from bs4 import BeautifulSoup
import operator
from collections import Counter


def start(url):
    wordlist = []
    site = requests.get(url).text
    soup = BeautifulSoup(site, 'html.parser')
    for i in soup.find_all('div', {'class': 'entry-content'}):
        conteudo = i.text
        palavras = conteudo.lower().split()
        for j in palavras:
            wordlist.append(j)

        limpar_wordlist(wordlist)


def limpar_wordlist(wordlist):
    clean_list = []
    for word in wordlist:
        symbols = "!@#$%^&*()_-+=<>?/|\;:{[]}.,"

        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], '')

        if len(word) > 0:
            clean_list.append(word)

    cria_dicionario(clean_list)


def cria_dicionario(clean_list):
    word_count = {}

    for word in clean_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    for key, value in sorted(word_count.items(),
                             key=operator.itemgetter(1)):
        print("% s : % s " % (key, value))

    c = Counter(word_count)

    top = c.most_common(10)
    print(top)


if __name__ == "__main__":
    start('https://www.geeksforgeeks.org/python-programming-language/?ref=leftbar')
