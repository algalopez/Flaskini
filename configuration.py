import yaml


def read_file(filename):
    with open(filename) as file:
        # The FullLoader parameter handles the conversion from YAML scalar values to Python the dictionary format
        return yaml.load(file, Loader=yaml.FullLoader)
