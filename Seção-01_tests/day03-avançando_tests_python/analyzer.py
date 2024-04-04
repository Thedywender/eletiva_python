import json

file_path = "person_data.json"


def read_json_file(file_path):
    with open(file_path, "r") as file:
        return json.load(file)


def analyze_json_file(file_path) -> str:
    if not file_path.endswith(".json"):
        raise ValueError("O arquivo precisa ser um arquivo JSON.")

    data = read_json_file(file_path)
    result = []
    for dado in data:
        result.append(
            f"A pessoa de nome {dado['nome']} " f"tem {dado['idade']} anos de idade."
        )
    return "\n".join(result)


print(analyze_json_file(file_path))
