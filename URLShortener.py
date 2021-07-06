from Encoder import Encoder

class URLShortener:
    __id = 1
    __dict_with_processed_urls = dict()

    def shorten_url(self, long_url):
        if long_url in self.__dict_with_processed_urls.keys():
            return self.__dict_with_processed_urls[long_url]
        else:
            id_in_62_base = Encoder.int2base62char(self.__id)
            short_url = 'http://www.shorturl.com/' + id_in_62_base
            self.__dict_with_processed_urls[long_url] = short_url
            self.__id += 1
            return short_url
