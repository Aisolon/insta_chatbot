# insta_chatbot

---

A rudimentary chatbot for instagram. Sends messages to specified chats through firefox.

---

## Installation
1. Download the repository as a zip file or clone it.

2. If you have downloaded the repository as a zip file, unzip it and navigate to the folder you saved it in.

3. Open a PowerShell as administrator, to do that, press the Windows Key, search for PowerShell, and click "Open as Administrator".

4. In this PowerShell (and if you have to restart it), execute the following line of code:
    ```powershell
    Set-ExecutionPolicy Bypass -Scope Process -Force
    ```
   This enables execution rights for PowerShell scripts that we are going to run to install all the necessary dependencies for this bot.
5. Now type
    ```powershell
    .\automate_insta_bot.ps1
    ```
    and press Enter.
6. This script downloads and installs [Chocolatey](https://chocolatey.org/), [Firefox](https://www.mozilla.org/en-US/firefox/windows/), [Python](https://www.python.org/) and [gecko-driver](https://github.com/mozilla/geckodriver) for you.
7. Now you have to close the shell once and open it again. Repeat step 4.
8. Type 
    ```powershell
    .\create_venv.ps1
    ```
    This creates a virtual environment in which Python can install the libraries you need for this project without influencing your basic Python installation.
    It also installs the necessary library.
9. Type
    ```powershell
    .\run_insta_bot.ps1
    ```
    and enjoy the outcome!

## TODO
* Rewrite the structure of files so that first, everything is installed, then the venv is created separately, and then the script is run (or pack venvs and python script into one).
* Test message and name input.
