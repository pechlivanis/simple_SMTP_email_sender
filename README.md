SMTP Email Sender

A lightweight Python desktop application built with Tkinter that allows users to send test emails via various SMTP servers. This tool is ideal for developers and system administrators who need to verify mail server configurations or test email delivery

Features
- GUI Interface: Simple and intuitive graphical user interface using Tkinter.
- Pre-configured Servers: Includes a dropdown list of popular SMTP servers (Gmail, Outlook, Office365, Otenet, etc.).
- HTML Support: Sends emails in HTML format.
- Real-time Feedback: Provides success or error notifications via message boxes.
- Cross-platform: Runs on Windows, macOS, and Linux (anywhere Python is installed).

Prerequisites

To run this application, you need to have Python installed on your system.
- Python 3.x
- Standard libraries used: tkinter, smtplib, email (these are usually included with Python).

Ιnstallation & Usage
1. Clone the repository:

```git clone https://github.com/your-username/your-repo-name.git```

```cd your-repo-name```

2. Run the application:

```python email_sender.py```

3. How to use:
- Enter your email address.
- Enter your password (Note: For Gmail/Outlook, you may need to use an "App Password" if 2FA is enabled).
- Select or type your SMTP Server.
- Enter the Receiver's email.
- Click Send.

Building for Windows (.exe)
If you want to use this application on Windows without installing Python, you can compile it into a standalone executable using PyInstaller or Nuitka.
Option 1: Using PyInstaller (Easiest)
Install PyInstaller: pip install pyinstaller

Build the exe:

```pyinstaller --noconsole --onefile email_sender.py```

Your executable will be in the dist/ folder.

Option 2: Using Nuitka (Better Performance/Size)

```Install Nuitka: pip install nuitka```

Build the exe:

```python -m nuitka --standalone --onefile --plugin-enable=tk-inter --windows-disable-console email_sender.py```


Important Security Note
[!WARNING] Never hardcode your actual passwords in the source code. This app uses an entry field to take the password at runtime. If you are using Gmail, make sure to generate an App Password from your Google Account security settings, as standard passwords are often blocked for security reasons.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Author
Developed by Pechlivanis Dimitrios
