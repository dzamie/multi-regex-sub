# Multiple Regex Replacement
This tool allows you to execute multiple sequential regex replaces on a file in one go.

Each line of `find.txt` is a regex string to search for in the input document, corresponding to the same numbered line in `repl.txt`. Both files should end in a blank newline to prevent unexpected behavior.

To use, copy the input text into `input.txt`, set up `find.txt` and `repl.txt`, and run `main.py`. The resulting text will be in `output.txt`.

Replaces are run sequentially from top to bottom.