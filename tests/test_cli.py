from typer.testing import CliRunner

from poem_fa.main import app

runner = CliRunner()


def test_app():
    result = runner.invoke(app, ["ghazal", "1"])
    assert result.exit_code == 0
    verse = 'الا یا ایها الساقی ادر کأسا و ناولها'
    assert verse in result.stdout
