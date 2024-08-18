import re

class PreProcessor:
    re_txt = r'(https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]'

    def __init__(self, search_item) -> None:
        self.si = search_item
        self.working_txt = self.si.txt

    def remove_urls(self):
        self.working_txt = re.sub(self.re_txt, '', self.working_txt, flags=re.MULTILINE)

    def remove_newline(self):
        self.working_txt = re.sub(r"\n", " ", self.working_txt)
        self.working_txt = re.sub(r"\s+", " ", self.working_txt)
        self.working_txt = self.working_txt.strip()

    def remove_specialchars(self):
        pattern = r'[,\(\)\[\]\:\-\#\/\!"]'
        self.working_txt = re.sub(pattern, ' ', self.working_txt)

    def reduce_space(self):
        self.working_txt = re.sub(r'\s+', ' ', self.working_txt)

    def start(self):
        self.remove_urls()
        self.remove_newline()
        self.remove_specialchars()
        self.reduce_space()

        self.si.ppr_txt = self.working_txt
        self.si.dump_pprfile()
    