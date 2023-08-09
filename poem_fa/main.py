import typer
from poem_fa.hafez import Hafez
app = typer.Typer()


@app.command()
def fal():
    Hafez().fal()


@app.command()
def ghazal(number: int):
    poem = Hafez().get_ghazal(number)
    # poem = Hafez().fal()
    
    Hafez().print_poem(poem)


if __name__ == "__main__":
    app()
