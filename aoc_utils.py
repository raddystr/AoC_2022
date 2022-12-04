def input_parse(file_name) -> str:
    try:
        input_file = open(f"./inputs/{file_name}")
        data = input_file.read()
        input_file.close()
        return data
    except:
        return "No such file!"
