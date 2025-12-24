import tkinter as tk
from tkinter import messagebox, ttk
import smtplib
from email.mime.text import MIMEText

mail_servers = ("smtp.office365.com",
                "smtp-mail.outlook.com",
                "smtp.gmail.com",
                "smtp.mail.yahoo.com",
                "mailgate.otenet.gr",
                "mailgate.cosmotemail.gr"
                )

def connect_tomailsrv(msg, mail_server, mail_address, mail_pass):
    """Connects to the SMTP server and sends the message.

    Args:
        msg (str): The message to be sent.
        mail_server (str): The SMTP server address.
        mail_address (str): The sender's email address.
        mail_pass (str): The sender's password.
    """

    try:
        #print("Connecting to mail server:", mail_server)
        server = smtplib.SMTP(mail_server, 587)
        server.ehlo()
        server.starttls()
        server.login(mail_address, mail_pass)
        server.sendmail(mail_address, msg['To'], msg.as_string())
        server.quit()
        messagebox.showinfo("Send email", "Email sent successfully")
    except Exception as e:
        messagebox.showerror("Send email", f"There was a problem sending the email.: {e}")
        #print(e)

def send_email():
    """Composes and sends the email."""

    mail_to = mail_to_entry.get()
    mail_address = mail_addr_entry.get()
    mail_pass = mail_pass_entry.get()
    mail_server = mail_server_entry.get()
    print("Mail to: ",mail_to)
    print("from: ",mail_address)
    print("pass: ",mail_pass)
    print("Mail server: ",mail_server)

    if not mail_to or not mail_address or not mail_pass or not mail_server:
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    html = """\
    <html>
    <head></head>
    <body>
    <p style="font-size:16">
        TEST email, SMTP mail test
    </p>
    </body>
    </html>
    """

    msg = MIMEText(html, 'html')
    msg['Subject'] = 'Send a test message'
    msg['From'] = mail_address
    msg['To'] = mail_to

    connect_tomailsrv(msg, mail_server, mail_address, mail_pass)

#Create the main window
root = tk.Tk()
root.title("SMTP email sender")
root.geometry("240x165")

title_label = tk.Label(root, text="SMTP e-mail test",
                       font=("Segoe IU", 12), fg="#0e77d2")
title_label.grid(row=0, column=0, columnspan=2)

mail_addr_label = tk.Label(root, text="Your email:")
mail_addr_label.grid(row=1, column=0)
mail_addr_entry = tk.Entry(root)
mail_addr_entry.grid(row=1, column=1)

mail_pass_label = tk.Label(root, text="Password:")
mail_pass_label.grid(row=2, column=0)
mail_pass_entry = tk.Entry(root)  # to hide password  show="*"
mail_pass_entry.grid(row=2, column=1)

mail_server_label = tk.Label(root, text="SMTP Server:")
mail_server_label.grid(row=3, column=0)
mail_server_entry = ttk.Combobox(root, values=list(mail_servers))
mail_server_entry.grid(row=3, column=1)

mail_to_label = tk.Label(root, text="Receiver email:")
mail_to_label.grid(row=4, column=0)
mail_to_entry = tk.Entry(root)
mail_to_entry.grid(row=4, column=1)

send_btn = tk.Button(root, text="Send", command=send_email)
send_btn.grid(row=5, column=0, padx=5, pady=5, sticky="nsew")

footer_label = tk.Label(root, text="dev in python, Pechlivanis Dimitrios")
footer_label.grid(row=6, column=0, columnspan=2)

root.mainloop()
