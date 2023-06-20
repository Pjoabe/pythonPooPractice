import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    existing_files = {item["nome_do_arquivo"] for item in instance.queue}
    if path_file not in existing_files:
        lines = txt_importer(path_file)
        if lines:
            data = {
                "nome_do_arquivo": path_file,
                "qtd_linhas": len(lines),
                "linhas_do_arquivo": lines
            }
            instance.enqueue(data)
            sys.stdout.write(str(data))


def remove(instance):
    if instance.queue:
        remove_file = instance.dequeue()
        sys.stdout.write(
            f"Arquivo {remove_file['nome_do_arquivo']} removido com sucesso\n"
        )
    else:
        sys.stdout.write("Não há elementos\n")


def file_metadata(instance, position):
    if position < 0 or position >= len(instance.queue):
        sys.stderr.write("Posição inválida\n")
    else:
        file_info = instance.search(position)
        sys.stdout.write(str(file_info))
