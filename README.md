# Readthis

Readthis is a command line tool that reads aloud a given text file using the gTTS (Google Text-to-Speech) interface.

## Usage

```bash
$ readthis [OPTIONS] FILE
```

### Positional Arguments

- `FILE`: The file to read aloud. Use - to read from stdin.

### Options

- `-h, --help`: Show the help message and exit.
- `--lang LANG, -l LANG`: Choose the language to use for reading. Specify the language using the language code (e.g., fr for French). Defaults to English.

## Installation

```bash
$ pip install readthis
```

## Examples

- Read a text file named sample.txt in English:

```bash
$ readthis --lang en sample.txt
```

- Read from stdin in French:
```bash
$ echo "Bonjour, comment ça va ?" | readthis -l fr -
```

## License

This project is licensed under the [MIT License](./LICENCE).

