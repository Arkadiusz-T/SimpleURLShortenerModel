from URLShortener import URLShortener
from Encoder import Encoder
# demo for ulr shortener
shortener = URLShortener()

short_url_1 = shortener.shorten_url('https://www.youtube.com/watch?v=QeWBS0JBNzQ&list=RDQeWBS0JBNzQ&start_radio=1&ab_channel=LadyGagaVEVO')
short_url_2 = shortener.shorten_url('https://www.shutterstock.com/pl/?kw=images%20stock&c3apidt=p43670346507&gclid=CjwKCAjw_o-HBhAsEiwANqYhp1aWQILdshqWmsowDIaSlSYVCZiLy6nmZfykw6onSC5Xid8uthzevRoCJvEQAvD_BwE&gclsrc=aw.ds')
short_url_3 = shortener.shorten_url('https://www.megapixl.com/two-small-jack-russell-terrier-dogs-are-running-across-a-green-meadow-and-have-a-lot-of-fun-stock-photo-153506516')

print('Shortened urls: \n{} \n{} \n{} \n'.format(short_url_1, short_url_2, short_url_3))

#demo for encoder
encoded_number_1 = Encoder.int2base62char(1234567890)
encoded_number_2 = Encoder.int2base62char(987654321)
encoded_number_3 = Encoder.int2base62char(9999999999999999)

print('Shortened urls: \n{} \n{} \n{} \n'.format(encoded_number_1, encoded_number_2, encoded_number_3))
