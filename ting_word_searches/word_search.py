def exists_word(word, instance):
    search_result = []
    for data in instance.queue:
        file_info = {
            "palavra": word,
            "arquivo": data["nome_do_arquivo"],
            "ocorrencias": []
        }
        for i, line in enumerate(data["linhas_do_arquivo"], start=1):
            if word.lower() in line.lower():
                file_info["ocorrencias"].append({"linha": i})
        if file_info["ocorrencias"]:
            search_result.append(file_info)
    return search_result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
