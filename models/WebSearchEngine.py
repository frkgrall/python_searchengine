from pydash import intersection, union, get
import pickle


class WebSearchEngine():
    """docstring for WebSearchEngine"""
    def __init__(self):
        self.count = 0
        self.indexed_urls = []
        self.search_dict = {}

    def __repr__(self):
        return str(self.__dict__)

    def index(self, webpage):
        for word in webpage.desc_words:
            key_value = self.search_dict.get(word)
            if not key_value:
                self.search_dict[word] = {'count': 0, 'urls': []}
            self.search_dict[word]['urls'].append(webpage.url)
        self.indexed_urls.append(webpage.url)
        pickle.dump(self, open("save.p", "wb"))

    def single_search(self, query):
        self.count += 1
        return get(self.search_dict, query + ".urls")

    def multiple_search(self, word_list, is_conjunctive):
        self.count += 1
        first_search = True
        urls = []
        for word in word_list:
            if is_conjunctive:
                if first_search:
                    urls = union(urls, get(self.search_dict, word + ".urls"))
                    first_search = False
                else:
                    urls = intersection(urls, get(self.search_dict, word + ".urls"))
            else:
                urls = union(urls, get(self.search_dict, word + ".urls"))
        return urls

    def all_urls(self):
        return self.indexed_urls

