import customtkinter
import socket
import threading

# Choosing Nickname
nickname = input("Choose your nickname: ")

# Connecting To Server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', notusedport))

# Listening to Server and Sending Nickname
def receive():
    while True:
        try:
            # Receive Message From Server
            # If 'NICK' Send Nickname
            message = client.recv(1024)
            if message.decode('ascii') == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                customtkinter.CTkLabel(scrolable_frame, text=message).pack(pady=10)
        except:
            # Close Connection When Error
            print("An error occured!")
            client.close()
            break

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()

app.title("Social Media " + nickname)
app.geometry('900x900')

scrolable_frame = customtkinter.CTkScrollableFrame(app)
scrolable_frame.pack(pady=40)

#for x in range(20):
    #customtkinter.CTkButton(scrolable_frame, text="Buttonlol").pack(pady=10)

def Submit_Clicked():
    # Sending Messages To Server
    global TextBoxForMsg
    message = '{}: {}'.format(nickname, TextBoxForMsg.get("1.0",'end-1c'))
    client.send(message.encode('ascii'))

TextBoxForMsg = customtkinter.CTkTextbox(app, height=10)
TextBoxForMsg.pack(pady=40)
TextButtonForMsg = customtkinter.CTkButton(app, height=10, text="Submit", command=Submit_Clicked)
TextButtonForMsg.pack(pady=40)

# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()


app.mainloop()
