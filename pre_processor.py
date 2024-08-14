import re
import ntpath

class PreProcessor:
    re_txt = r'(https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]'

    def __init__(self, file_path) -> None:
        self.file_path = file_path
        self.working_txt = None
        with open(file_path, 'r') as file:
            self.working_txt = file.read()

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

        output_file_path = self.get_output_file_path()
        with open(output_file_path, 'w', encoding="utf-8") as output_file:
            output_file.write(self.working_txt)

    def get_output_file_path(self):
        filename = ntpath.basename(self.file_path)
        return 'output/' + filename + '.ppr'
    