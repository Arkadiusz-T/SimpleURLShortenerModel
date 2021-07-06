# SimpleURLShortenerModel
takes an URL and then process it to return shortened version

## Demo included

## Algorithm
Take an url and checks if it was processed before,
if yes return previously shortened URL
if no take next number from its internals and process it
for numbers in base 62 and then to string.

Return shortened string combining domain name + processed number.
