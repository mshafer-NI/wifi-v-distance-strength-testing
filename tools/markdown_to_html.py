import pathlib
import typing

import click
import markdown

@click.command()
@click.argument("input_file", type=click.Path(exists=True, dir_okay=False, path_type=pathlib.Path))
@click.option("--append-file", "-a", "append_files", type=click.Path(path_type=pathlib.Path), multiple=True, default=[])
@click.option("--output-file", "-o", type=click.Path(path_type=pathlib.Path), default="output.html")
def convert(input_file: pathlib.Path, output_file: pathlib.Path, append_files: typing.Tuple[pathlib.Path]):
    text = input_file.read_text(encoding="utf-8")

    html = [markdown.markdown(text)]

    for append_file in append_files:
        text = append_file.read_text(encoding="utf-8")
        html.append(markdown.markdown(text))

    output_file.write_text("\n".join(html), encoding="utf-8")


if __name__ == "__main__":
    convert()
