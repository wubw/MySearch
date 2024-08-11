import yaml
import os

config = yaml.safe_load(open("config.yml", 'r'))

def is_valid_folder(path):
    basename = os.path.basename(path)
    if basename.startswith('.'):
        return False
    return True

def is_valid_file(path):
    basename = os.path.basename(path)
    if basename.startswith('.'):
        return False
    _, file_extension = os.path.splitext(path)
    if file_extension in config['exclude_file_extensions']:
        return False
    return True

def check_ext(file_path, ext_check):
    _, file_extension = os.path.splitext(file_path)
    if file_extension in ext_check:
        ext_check[file_extension] = ext_check[file_extension] + 1
    else:
        ext_check[file_extension] = 1

def crawl(folder):
    output_file_path = 'output/files.txt'
    ext_check = {}

    files_cnt = 0
    with open(output_file_path, 'w', encoding="utf-8") as output_file:
        # os.walk can have performance issue
        for root, subdirs, files in os.walk(folder):
            if not is_valid_folder(root):
                continue

            for filename in files:
                file_path = os.path.join(root, filename)

                if not is_valid_file(file_path):
                    continue

                check_ext(file_path, ext_check)

                output_file.write('%s' % file_path + '\n')
                files_cnt = files_cnt + 1

    print('Total files:', files_cnt)
    print('File extensions:', ext_check)

for f in config['folders']:
    crawl(f)
