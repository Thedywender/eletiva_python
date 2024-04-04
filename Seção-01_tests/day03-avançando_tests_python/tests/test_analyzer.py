from unittest.mock import Mock, patch
import pytest
from analyzer import analyze_json_file, read_json_file


def test_analyze_json_file():
    mock_read_json_file = Mock(
        side_effect=[
            {"nome": "Maria", "idade": 31},
            {"nome": "Agenor", "idade": 56},
        ]
    )
    fake_file_path = "invalid.json"

    with patch("analyzer.read_json_file", mock_read_json_file):
        assert (
            analyze_json_file(fake_file_path)
            == "A pessoa de nome Maria tem 31 anos de idade."
        )
        assert (
            analyze_json_file(fake_file_path)
            == "A pessoa de nome Agenor tem 56 anos de idade."
        )
    mock_read_json_file.assert_called_with(fake_file_path)


def test_analize_json_file_propagates_exception():
    mock_read_json_file = Mock(side_effect=FileNotFoundError)
    fake_file_path = "invalid.json"

    with patch("analyzer.read_json_file", mock_read_json_file):
        with pytest.raises(FileNotFoundError):
            analyze_json_file(fake_file_path)


def test_read_json_file(tmp_path):
    fake_file_path = tmp_path / "fake.json"
    fake_file_path.touch()

    mock_json = Mock()
    mock_json.load = Mock(return_value={"nome": "Maria", "idade": 31})

    with patch("analyzer.json", mock_json):
        result = read_json_file(fake_file_path)

    assert result == {"nome": "Maria", "idade": 31}


def test_analyze_json_file_return_error():
    fake_file_path_error = "fake_file.txt"

    with pytest.raises(ValueError, match="O arquivo precisa ser um arquivo JSON."):

        analyze_json_file(fake_file_path_error)


# >>> Modo mais simples, usando os arquivos sem mockar!!!
# from analyzer import analyze_json_file


# def test_analyze_json_file():
#     result = analyze_json_file("person_data.json")
#     assert result == "A pessoa de nome João tem 30 anos de idade."
