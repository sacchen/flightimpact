import typer

app = typer.Typer(no_args_is_help=True)


@app.callback()
def main() -> None:
    """A reproducible flight CO₂ estimator with uncertainty quantification."""


@app.command()
def hello() -> None:
    print("flightimpact ready")
