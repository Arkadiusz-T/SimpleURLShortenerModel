class Encoder:

    @staticmethod
    def int2base62char(int_number):
        """
        :param int_number: id of a processed url
        :return: id in a 62 base

        function filrs process int to different base and then assing chars to numbers to create a string
        """
        chars = '0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
        base = 62
        if int_number == 0:
            return 0
        digits = []
        while int_number:
            digits.append(int(int_number % base))
            int_number //= base
        digits = digits[::-1]
        id_in_62_base = str()

        for digit in digits:
            id_in_62_base += str(chars[digit])

        return id_in_62_base
