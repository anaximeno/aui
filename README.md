# Action UI

GTK-Based UI Toolkit for [Nemo Actions](https://github.com/linuxmint/cinnamon-spices-actions).

Action UI (aui) is a Python library and command-line tool that provides a set of GTK-based dialog windows for creating user interfaces in Nemo Actions. It supports various dialog types such as informational messages, questions, text entry, radio choices, actionable buttons, and progress bars. The toolkit can be used programmatically by importing its classes or via the command-line interface for quick scripting.

## Installation

1. Ensure you have Python 3 and GTK 3 installed on your system.
2. Clone or download the repository.
3. Place `aui.py` in your project directory or make it executable and available in your PATH.

Dependencies:

- Python 3
- PyGObject (gi)
- GTK 3

Install dependencies via your package manager, e.g., on Ubuntu or Debian: `sudo apt install python3-gi python3-gi-cairo gir1.2-gtk-3.0`

## Usage

### Command-Line Interface

Run the tool using Python:

```bash
./aui.py <dialog_type> [options]
```

Replace `<dialog_type>` with one of the supported types: `info`, `question`, `entry`, `choice`, `action`, or `progress`.

Common options across dialogs:

- `--title`: Window title (required for most dialogs).
- `--text`: Main dialog text or label.
- `--header`: Header text displayed at the top.
- `--width`: Dialog width (default: 360).
- `--height`: Dialog height (default: 120).
- `--icon-path`: Path to a custom icon file.
- `--icon-name`: Name of a system icon (e.g., 'dialog-information').
- `--hide-in-dialog-icon`: Hide the icon in the dialog header.

### Programmatic Usage

Import the classes from `aui.py` in your Python script:

```python
from aui import InfoDialogWindow

dialog = InfoDialogWindow(message="Hello, World!", title="Info")
dialog.run()
dialog.destroy()
```

Refer to the source code in `aui.py` for class constructors and methods.

## Examples

### Info Dialog

Displays an informational message with optional expandable text.

```bash
./aui.py info --title "Information" --text "This is an info message." --header "Header" --expander-label "Details" --expanded-text "Additional information here."
```

### Question Dialog

Asks a yes/no question. Exits with 0 for yes, 1 for no.

```bash
./aui.py question --title "Confirm" --text "Do you want to proceed?" --header "Confirmation"
```

### Entry Dialog

Prompts for text input. Prints the entered text on success.

```bash
./aui.py entry --title "Input" --text "Enter your name:" --entry-text "Default text" --header "User Input"
```

### Choice Dialog

Presents radio button choices. Prints the selected choice ID (the order the choice was added, starting from 1).

```bash
./aui.py choice --title "Select Option" --text "Choose one:" --add-choice "Option 1" --add-choice "Option 2" --default-choice 1 --orientation vertical
```

### Action Dialog

Shows buttons with actions. Prints the button ID (the order the button was added, starting from 1) on click.

```bash
./aui.py action --title "Actions" --text "What do you want to do?" --add-button "Save" --add-button "Cancel" --default-button 1
```

### Progress Dialog

Displays a progress bar that can be updated via stdin.

```bash
for i in $(seq 0 100); do
    sleep 0.05
    echo $i
    if [ $i -eq 25 ]; then
        echo "# Updated Message"
    elif [ $i -eq 60 ]; then
        echo "> New log entry"
    elif [ $i -eq 85 ]; then
        echo "# Closing Message"
    elif [ $i -eq 100 ]; then
        echo "# Completed"
    fi
    sleep 0.
done | ./aui.py progress --title "Progress" \
                         --text "Processing..." \
                         --expander-label "Log" \
                         --expanded-text "Initial log." \
                         --timeout-ms=50
```

For more details on options, run `./aui.py <dialog_type> --help`.

## Contributing

Contributions are welcome. Please refer to the source code for implementation details.

## License

MIT License. See the header in `aui.py` for full text.
