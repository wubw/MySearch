import ntpath

class SearchItem:
    def __init__(self, txt, path) -> None:
        self.txt = txt
        self.ppr_txt = None
        self.tk_txt = None
        self.bf = None
        self.path = path

    def get_basename(self):
        return ntpath.basename(self.path)

    def dump_tokenfile(self):
        output_file_path = self.get_output_tokenfile_path()
        if output_file_path is None:
            return
        with open(output_file_path, 'w', encoding="utf-8") as output_file:
            output_file.write(str(self.tk_txt))
    
    def get_output_tokenfile_path(self):
        fp = self.get_output_file_path()
        if fp is None:
            return None
        return fp + '.tk'

    def dump_pprfile(self):
        output_file_path = self.get_output_pprfile_path()
        if output_file_path is None:
            return
        with open(output_file_path, 'w', encoding="utf-8") as output_file:
            output_file.write(str(self.ppr_txt))

    def get_output_pprfile_path(self):
        fp = self.get_output_file_path() 
        if fp is None:
            return None
        return fp + '.ppr'

    def get_output_file_path(self):
        if self.path is None:
            return None
        filename = ntpath.basename(self.path)
        return 'output/' + filename
    