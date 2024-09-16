import pathlib

import click
import markdown

@click.command()
@click.argument("input_file", type=click.Path(exists=True, dir_okay=False, path_type=pathlib.Path))
@click.option("--output-file", "-o", type=click.Path(path_type=pathlib.Path), default="output.html")
def convert(input_file: pathlib.Path, output_file: pathlib.Path):
    text = input_file.read_text(encoding="utf-8")

    html = markdown.markdown(text)

    output_file.write_text(html, encoding="utf-8")


if __name__ == "__main__":
    convert()
