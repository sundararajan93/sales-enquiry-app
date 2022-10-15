from dbconnection import *
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)

        self.cols = 1
        self.add_widget(Label(text="Add an enquiry", size_hint_y=None, height=50, font_size=40))
        # self.title_grid = GridLayout(cols=1)
        
        # Title of App
        # self.title_grid.add_widget(Label(text="Add an enquiry", size_hint_y=None, height=30))

        # self.add_widget(self.title_grid)
    
        # adding top grid layout
        self.values_grid  = GridLayout()
        self.values_grid.cols = 2

        # Agent name row
        self.values_grid.add_widget(Label(text="Agent Name: ", size_hint_y=None, height=30))
        self.agent = TextInput(multiline=False, size_hint_y=None, height=30)
        self.values_grid.add_widget(self.agent)

        # Customer name row
        self.values_grid.add_widget(Label(text="Customer Name: ", size_hint_y=None, height=30))
        self.customer = TextInput(multiline=False, size_hint_y=None, height=30)
        self.values_grid.add_widget(self.customer)

        # Company Name row
        self.values_grid.add_widget(Label(text="Company Name: ", size_hint_y=None, height=30))
        self.company = TextInput(multiline=False, size_hint_y=None, height=30)
        self.values_grid.add_widget(self.company)

        # Address row
        self.values_grid.add_widget(Label(text="Address: "))
        self.address = TextInput(multiline=True)
        self.values_grid.add_widget(self.address)

        # Contact number row
        self.values_grid.add_widget(Label(text="Contact Number: ", size_hint_y=None, height=30))
        self.contact = TextInput(multiline=False, size_hint_y=None, height=30)
        self.values_grid.add_widget(self.contact)

        # Email Id row
        self.values_grid.add_widget(Label(text="Email: ", size_hint_y=None, height=30))
        self.email = TextInput(multiline=False, size_hint_y=None, height=30)
        self.values_grid.add_widget(self.email)

        # Requirement row
        self.values_grid.add_widget(Label(text="Requirement: "))
        self.requirement = TextInput(multiline=True)
        self.values_grid.add_widget(self.requirement)

        # Adding layout widget
        self.add_widget(self.values_grid)

        # submit button
        self.submit = Button(text="Submit", size_hint_y=None, height=40)

        # bind the button with method
        self.submit.bind(on_press=self.save)
        self.add_widget(self.submit)

    def save(self, instance):
        # Grabbing the values from textinput
        agent = self.agent.text
        customer = self.customer.text
        company = self.company.text
        address = self.address.text
        contact = self.contact.text
        email = self.email.text
        requirement = self.requirement.text

        # Saving them to DB or file
        try:        
            db_connect(DBHOST, DBUSER, DBPASS, DBNAME)
            insert_enquiry_data("enquiry", (agent, customer, company, address, contact, email, requirement))
        except:
            print("Saving the details in text file!")
            with open("enquiry.txt", "a") as f:
                f.write("\n------------------------------------------------------------------------")
                f.write(f"\nAgent - {agent}\nCustomer - {customer}\
                    \nCompany - {company}\nAddress - \n{address}\
                    \nContact - {contact}\nEmail - {email}\nRequirement - \n{requirement}")
            
        # Clearing the input box after we saved the detail

        self.agent.text = ""
        self.customer.text = ""
        self.company.text = ""
        self.address.text = ""
        self.contact.text = ""
        self.email.text = ""
        self.requirement.text = ""

class EnquiryApp(App):
    def build(self):
        self.title = "Sales Enquiry Generation"
        self.icon = 'sales.ico'
        Window.clearcolor = (22/255, 33/255, 62/255, 0.3)
        return MyGridLayout()


if __name__ == "__main__":
    my_app = EnquiryApp()
    my_app.run()