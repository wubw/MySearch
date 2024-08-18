import search_item

class FileItem(search_item.SearchItem):
    def __init__(self, path) -> None:
        with open(path, 'r', encoding='utf-8') as file:
            txt = file.read()
        super().__init__(txt, path)
