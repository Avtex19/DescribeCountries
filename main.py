from tkinter import *


class CapitalOfCountries:
    d = {}
    with open("Countries.txt") as file:
        for line in file:
            values = line.strip().split("-")  # The strip() method removes any leading
            # (spaces at the beginning) and trailing (spaces at the end) characters
            # (space is the default leading character to remove)
            if values:
                d[values[0]] = values[1:]


    def __init__(self, window):
        self.window = window
        self.window.title("DescribeCountries")
        self.window.geometry("800x600")
        self.window.config(bg='black')

        self.photoOne = PhotoImage(file="world-map-this-the-most-hard-working-country-the-world-7.png")
        photoReduced = self.photoOne.subsample(3, 4)
        self.photoOne_label = Label(self.window, image=photoReduced, bg="black")
        self.photoOne_label.place(anchor=CENTER, relx=.5, rely=.23)

        self.informationText = Label(self.window, fg='orange', bg='black',
                                     text="Welcome to the our application - DescribeCountries. Please enter the"
                                          " country name.",
                                     font=('arial', 18, 'bold'))
        self.informationText.place(anchor=CENTER, relx=.5, rely=.5)

        self.textEntry = Entry(self.window, width=30, bd=10, bg='orange', fg="black", font=('arial', 16, 'bold'))
        self.textEntry.place(anchor=CENTER, relx=.5, rely=.6)

        self.click_button = Button(self.window, text='SUBMIT', command=self.click, width=14, font=('arial', 20, 'bold'),
                                   bg="white", fg="orange")
        self.click_button.place(anchor=CENTER, relx=.3, rely=.7)

        self.output = Text(self.window, width=75, height=3, wrap=WORD, bg='orange', fg="black",
                           font=('arial', 16, 'bold'))
        self.output.place(anchor=CENTER, relx=.5, rely=.85)

        self.exit_button = Button(self.window, text="EXIT", width=14, command=self.close_window,
                                  font=('arial', 20, 'bold'),
                                  bg="white",
                                  fg="orange")
        self.exit_button.place(anchor=CENTER, relx=.7, rely=.7)

        self.window.mainloop()

    def close_window(self):
        self.window.destroy()
        exit()

    def click(self):
        text_input = self.textEntry.get()  # collects text from text entry
        self.output.delete(0.0, END)
        if text_input in self.d.keys():
            self.output.insert(END, str((' '.join(self.d[text_input]))))
        else:
            self.output.insert(END, "Sorry, can not find such a country, please try another one")


if __name__ == "__main__":
    root = Tk()
    app = CapitalOfCountries(root)
