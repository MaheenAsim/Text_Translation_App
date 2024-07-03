# Language Translation App

## Overview

This Language Translation App is a simple Python application that translates text from one language to another using the `googletrans` library. The application allows users to input text, choose a destination language, and receive the translated text in real-time. It also displays a list of supported languages and their respective codes.

## Features

- Translate text to any supported language.
- Create a easily navigable webpage with Home and About section.
- Display a list of supported languages and their codes in About section.
- Simple command-line interface for user interaction.

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/language-translation-app.git
   ```

2. Navigate to the project directory:

   ```bash
   cd language-translation-app
   ```

3. Install the required dependencies:

   ```bash
   pip install googletrans==4.0.0-rc1
   ```

## Usage

1. Run the application:

   ```bash
   python translate_app.py
   ```

2. Follow the on-screen instructions:
   - Enter the text you want to translate.
   - Enter the destination language code (e.g., 'es' for Spanish).

3. To quit the application, enter 'q' when prompted to input text.

## Code Explanation

### Initialization

The application begins by importing necessary modules and initializing the `Translator` object from `googletrans`.

```python
from googletrans import Translator, LANGUAGES

translator = Translator()
```

### Functions

- **`translate_text(text, dest_lang)`**: Translates the given text to the specified destination language.
- **`print_supported_languages()`**: Prints a list of all supported languages and their codes.

### Main Function

The `main()` function serves as the entry point of the application. It welcomes the user, displays supported languages, and continuously prompts the user for text to translate until the user chooses to quit.

## Supported Languages

To see the list of supported languages and their codes, run the application and go to About section.


## Contributing

This is just the baseline project and could be improved vastly so Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.
