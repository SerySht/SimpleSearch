# -*- coding: utf-8 -*-
import operator
from .models import Indexes


def add_document(url, input_text, title):

    parsed_text = input_text.replace('.', '').replace(',', '').replace('"', '').replace("'", ''). \
        replace(':', '').replace('!', '').replace('?', '').lower()

    parsed_text = parsed_text.split()

    bulk_list = []
    new_input_text = "&" * 62 + input_text.lower() + "&" * 62

    for word in parsed_text:
        if len(word) < 4 or ord(word[0]) < 33 or word.find(' ') != -1 or word == '':
            continue

        index = new_input_text.find(str(word))
        context = ""
        if index != -1:
            try:
                context = new_input_text[index - 60: index + 60]
            except:
                context = ""
            context = "..." + context.replace("&", "") + "..."


        bulk_list.append(Indexes(word=word, url=url, context=context, title=title))
    Indexes.objects.bulk_create(bulk_list)

    print(" --- Saved ", url)


def find_word(word):
    l = Indexes.objects.filter(word=word.lower()).values_list('url', 'title', 'context')
    #print(l)
    # d = {}
    # for i in l:
    #     if i not in d:
    #         d[i[0]] = 1
    #     else:
    #         d[i[0]] += 1
    # return sorted(d.items(), key=operator.itemgetter(1), reverse=True)
    return set(l)
