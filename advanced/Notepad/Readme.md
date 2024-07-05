# Notepad Application

This is a Tkinter-based Notepad application. This guide explains how to create a Windows executable file using `cx_Freeze`.

## Prerequisites

1. Python 3.12 installed on your system.
2. `cx_Freeze` installed. If not, install it using:
    ```bash
    pip install cx_Freeze
    ```

## Setup Instructions

### Step 1: Project Structure

Ensure your project structure looks like this:

NotepadApp\
 ├── icons2/ # Directory containing your icons\
 ├── Notepad.py # Your main Notepad application script\
 ├── mainicon.ico # Icon for your application\
 ├── setup.py # Setup script for cx_Freeze\
 └── README.md # This README file

### Step 2: Setup Script (`setup.py`)

Ensure your `setup.py` file is configured correctly.

### Step 3: Build the Executable
Open a terminal in your project directory and run the following command to build the executable:
```bash
python setup.py build
```
This will create a build directory containing your executable and all necessary files.

### Step 4: Create an MSI Installer (Optional)
If you want to create an MSI installer for your application, run:
```bash
python setup.py bdist_msi
```
This will create a dist directory containing the MSI installer.

### Troubleshooting
If you encounter any issues, ensure that:

+ Python 3.12 is correctly installed.
+ cx_Freeze is correctly installed.
+ All file paths in setup.py are correctly specified.
For more information on cx_Freeze, refer to the official documentation.

### License
This project is licensed under the MIT License - see the LICENSE file for details.

Save this content in a file named `README.md` in your project directory. This guide should help users understand how to create a Windows executable for your Notepad application using `cx_Freeze`.
