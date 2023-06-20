import sys


def txt_importer(path_file):
    if path_file.find(".txt") <= 0:
        sys.stderr.write("Formato inválido\n")
        return []

    try:
        with open(path_file, "r") as archive:
            data = archive.read().split("\n")
        return data
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
        return []
