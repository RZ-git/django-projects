from pprint import pprint


class CodingRule:
    """ コーディング規約 """

    def __init__(self):
        super().__init__()
        self.name = 'PEP8に準拠'

    @classmethod
    def function(cls, arg=None, *kwarg):
        """
        :param arg: 引数 value
        :param kwarg: キーワード引数 {key: value}
        :return: 戻り値
        """

        print(cls.function().__doc__)
        pprint(kwarg)

        # TODO コメント
        odd_number_set = {1, 3, 5}
        even_number_set = {2, 4, 6}
        odd_number_set.add(even_number_set)

        byte_string: bytes = b'newline:\n also newline:\x0a'
        text_string = u"Cyrillic Я is \u042f. Oops: \\u042g"
        return odd_number_set, byte_string, text_string
