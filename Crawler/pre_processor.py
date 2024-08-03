import re

class PreProcessor:
    re_txt = r'(https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]'

    def remove_urls(self, text):
        ret = re.sub(self.re_txt, '', text, flags=re.MULTILINE)
        return ret

    def remove_newline(self, text):
        ret = re.sub(r"\n", " ", text)
        ret = re.sub(r"\s+", " ", ret)
        return ret.strip()
