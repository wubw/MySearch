import yaml
import os

class Crawler:
    config = yaml.safe_load(open("config.yml", 'r'))
    ext_check = {}
    files_cnt = 0

    def is_valid_folder(self, path):
        basename = os.path.basename(path)
        if basename.startswith('.'):
            return False
        return True

    def is_valid_file(self, path):
        basename = os.path.basename(path)
        if basename.startswith('.'):
            return False
        _, file_extension = os.path.splitext(path)
        if file_extension in self.config['exclude_file_extensions']:
            return False
        return True

    def check_ext(self, file_path):
        _, file_extension = os.path.splitext(file_path)
        if file_extension in self.ext_check:
            self.ext_check[file_extension] = self.ext_check[file_extension] + 1
        else:
            self.ext_check[file_extension] = 1

    def crawl(self, folder):
        output_file_path = 'output/files.txt'

        with open(output_file_path, 'w', encoding="utf-8") as output_file:
            # os.walk can have performance issue
            for root, subdirs, files in os.walk(folder):
                if not self.is_valid_folder(root):
                    continue

                for filename in files:
                    file_path = os.path.join(root, filename)

                    if not self.is_valid_file(file_path):
                        continue

                    self.check_ext(file_path)

                    output_file.write('%s' % file_path + '\n')
                    self.files_cnt = self.files_cnt + 1

        #print('Total files:', self.files_cnt)
        #print('File extensions:', self.ext_check)

    def start(self):
        for f in self.config['folders']:
            self.crawl(f)

#c = Crawler()
#c.start()