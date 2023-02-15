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
    def update_json_file(cls, path, values):
        try:
            with open(path, 'r+') as file:
                data = cls.load_json_file(path)
                data["stats"] = values
                json.dump(data, file, indent=4)
        except FileNotFoundError:
            return 1

    @classmethod
    def is_scene_available(cls, path):
        try:
            open(path, 'r')
            return True
        except FileNotFoundError:
            return False



