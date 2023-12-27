
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from subprocess import call
import requests
default_ip = '10.0.0.162'
secret_code = ';&jlU|&mm~yr>`\y"N/u?abYBn-/<eJ@w*Kimo?7u)58py7!31b6WG|3\5\*o!9'

def check(client_ip):
    information = requests.get(f"https://trfhgxx.eu.pythonanywhere.com/check/{client_ip}")

    return information.text

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10)

        # IP Address input
        ip_input = TextInput(multiline=False, text=default_ip)
        layout.add_widget(ip_input)

        # Status text
        status_label = Label(text='Some Status Text', font_size='20sp', color=(0, 0.7, 0.7, 1), markup=True)
        layout.add_widget(status_label)

        # Update Status button
        def update_status(instance):
            # Your logic to update the status text
            client_ip = ip_input.text
            information = check(client_ip)
            # You can access the IP address entered using ip_input.text
            if information == "ON":
                status_label.text = "[color=0d8c55]ON[/color]"
                off_button.disabled = False
            else:
                off_button.disabled = True
                status_label.text = "[color=3d3b3b]Unkown/OFF[/color]"



        update_button = Button(text='Update Status')
        update_button.bind(on_release=update_status)
        layout.add_widget(update_button)

        # Turn Off Laptop button
        def turn_off_laptop(instance):
            if status_label.text.lower() == '[color=0d8c55]on[/color]':
                requests.post('https://trfhgxx.eu.pythonanywhere.com/authenticate',
                                  headers={'Authorization': f'Bearer {secret_code}death'})


                # Your logic to turn off the laptop§

                off_button.disabled = True

        off_button = Button(text='Turn Off Laptop')
        off_button.bind(on_release=turn_off_laptop)
        off_button.disabled = True  # Disabling the button by default

        def on_status_label(instance, value):
            if value.lower() == '[color=008080]off[/color]':
                off_button.disabled = False
            else:
                off_button.disabled = True

        status_label.bind(text=on_status_label)
        layout.add_widget(off_button)

        return layout


if __name__ == '__main__':
    MyApp().run()
