import sys


def __Emailer(text, subject, recipient, auto=True):
    import win32com.client as win32

    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = recipient
    mail.Subject = subject
    mail.HtmlBody = text
    if auto:
        mail.Display(True)
    else:
        mail.Display(True)
        sys.exit(1)# or whatever the correct code is



__Emailer("Hey", "Hey","")



































