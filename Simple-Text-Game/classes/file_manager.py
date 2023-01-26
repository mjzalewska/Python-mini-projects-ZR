import json


class FileManager:
    @classmethod
    def load_json_file(cls, path):
        try:
            with open(path, 'r') as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            return 1

    @classmethod
    def update_char_stats(cls, path, values):
        with open(path, 'r+') as file:
            data = cls.load_scene_json(path)
            data["stats"] = values
            json.dump(data, file, indent=4)
