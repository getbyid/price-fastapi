import pytest
from pathlib import Path


def pytest_configure(config):
    config.addinivalue_line("markers", "sample_html(file_name): get html from file")


@pytest.fixture
def load_html(request):
    """Загрузка определённого HTML из файла"""
    marker = request.node.get_closest_marker("sample_html")
    if marker is None:
        return ""

    file_name = marker.args[0]
    p = Path(__file__).parent.joinpath("sample_html", file_name)
    return p.read_text()
