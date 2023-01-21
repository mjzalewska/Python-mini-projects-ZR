import json


class FileManager:
    @classmethod
    def load_scene_json(cls, path):
        try:
            with open(path, 'r') as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            return 1

    @classmethod
    def load_scene_txt(cls, path):
        try:
            with open(path, 'r', encoding='utf-8') as file:
                data = file.read()
                return data
        except FileNotFoundError:
            return 1

    @classmethod
    def update_char_stats(cls, path, values):
        with open(path, 'r+') as file:
            data = cls.load_scene_json(path)
            data["stats"] = values
            json.dump(data, file, indent=4)
