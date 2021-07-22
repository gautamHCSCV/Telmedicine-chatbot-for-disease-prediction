from twilio.rest import Client
import random
from tkinter import *
from tkinter import messagebox

class otp_verifier(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('600x550')
        self.resizable(False, False)
        self.n = random.randint(1000,9999)
        # Enter your details from twilio account
        self.client = Client("AC197aca60423945861dcbb99aba1070da", "7a6bd0f6fd2bf8e37d01471e60350bda")
        self.client.messages.create(to = ["+919523730105"], from_ = "+17755714605", body = 'Your OTP is: {}'.format(self.n))

    def Labels(self):
        self.c = Canvas(self, bg="white", width = 400, height = 280)
        self.c.place(x = 100, y=60)
        self.Login_Title = Label(self, text = "OTP Verification", font = "bold,20", bg = "white")
        self.Login_Title.place(x=210,y=90)

    def Entry(self):
        self.User_Name = Text(self, borderwidth=2, highlightthickness=0, width=29, height=2)
        self.User_Name.place(x=190,y = 160)
    def Buttons(self):
        self.submitButtonImage = PhotoImage(file = 'submit.png')
        self.submitButton = Button(self, image=self.submitButtonImage, command=self.checkOTP,
                                   border = 0)
        self.submitButton.place(x=150, y=240)
        self.resendOTPImage = PhotoImage(file = 'resendotp.png')
        self.resendOTP = Button(self, image = self.resendOTPImage, command = self.resendOTP)
        self.resendOTP.place(x=208, y = 400)

    def resendOTP(self):
        self.n = random.randint(1000,9999)
        self.client = Client("AC197aca60423945861dcbb99aba1070da","7a6bd0f6fd2bf8e37d01471e60350bda")
        self.client.messages.create(to=["+919523730105"], from_="+17755714605", body = self.n)
    def checkOTP(self):
        try:
            self.userInput = int(self.User_Name.get(1.0, "end-1c"))
            if self.userInput == self.n:
                messagebox.showinfo("showinfo", "Login Success")
                self.n = "done"
            elif self.n == "done":
                messagebox.showinfo("showinfo", "already entered the OTP")
            else:
                messagebox.showinfo("showinfo", "INVALID OTP")
        except:
            messagebox.showinfo("showinfo", "INVALID OTP")


window = otp_verifier()
window.Labels()
window.Entry()
window.Buttons()
window.mainloop()