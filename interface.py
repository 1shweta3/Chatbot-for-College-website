import tkinter as tk
from tkinter import *
from chat import  get_response, bot_name

BG_GRAY = "#fff"
BG_COLOR = "#000000"
TEXT_COLOR = "#87CEEB"
BLUE = "#088F8F"

FONT = "Perpetua 15 "
FONT_BOLD  ="Perpetua 16 bold"

class BotInterface:
    def __init__(self):
        self.window = Tk()
        self._setup_main_window()

    def run(self):
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title("Vishwakarma Institute of Technology")
        self.window.resizable(width =False ,height = False)
        self.window.configure(width = 470,height = 550,bg = BG_GRAY)
        
        #head_label
        head_label = Label(self.window, bg = BLUE ,fg = BG_GRAY,
                           text = "Welcome" ,font = FONT_BOLD,pady= 10)
        head_label.place(relwidth = 1)

        #tiny divider
        line = Label(self.window, width=450 ,bg =BG_GRAY)
        line.place(relwidth = 1, rely= 0.07, relheight = 0.0012)

        ##text widget
        self.text_widget = Text(self.window, width = 20 , height = 5, bg= BG_GRAY , fg = BG_COLOR,
                                font = FONT, padx=1,pady = 1)
        self.text_widget.place(relheight=0.745, relwidth=1, rely = 0.08)
        self.text_widget.configure(cursor="arrow",state = DISABLED)

        #scroll bar
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx = 0.995)
        scrollbar.configure(command = self.text_widget.yview)

        #bottom label
        bottom_label = Label(self.window , bg = BLUE, height = 77)
        bottom_label.place(relwidth = 1, rely = 0.825)

        # message entry  box
        self.msg_entry = Entry(bottom_label, bg = BG_GRAY , fg = BG_COLOR, font = FONT)
        self.msg_entry.place(relwidth  =0.76, relheight = 0.073, rely = 0.003, relx = 0.001)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        #send button
        send_button = Button(bottom_label, text = "Send", font=FONT_BOLD, width=20, bg = BLUE,fg = BG_GRAY,
                             command = lambda: self._on_enter_pressed(None))
        send_button.place(relx = 0.77, rely = 0.003, relheight = 0.073, relwidth = 0.23)

    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg,"You")

    
    def display_response_letter_by_letter(self,response):
            
            #words = response.split()
            
            current_char_index = 0
            
            def display_char():
                
                nonlocal current_char_index
                
                #self.text_widget.configure(state =NORMAL)
                
                if current_char_index < len(response):
                        
                        self.text_widget.insert(tk.END, response[current_char_index])
                        current_char_index +=1
                        self.text_widget.see(tk.END) 
                        self.window.after(20, display_char)

                else:   
                        
                        self.text_widget.insert(tk.END, "\n\n")        
                        self.text_widget.configure(state=DISABLED)
                #self.text_widget.insert(tk.END, "\n") 
                
            display_char()  
             
    
    def _insert_message(self, msg, sender):
       # if not msg:
        #    return
        
            #get_response(msg) 
        #self.msg_entry.delete(0, END)
        #msg1 = f"{sender}: {msg}\n\n"
        #self.text_widget.configure(state =NORMAL)
        #self.text_widget.insert(END, msg1)
        #self.text_widget.configure(state=DISABLED)
        
        #msg2 = f"{bot_name}:{get_response(msg)}\n\n"
        #self.text_widget.configure(state =NORMAL)
        #self.text_widget.insert(END, msg2)
        #self.text_widget.configure(state=DISABLED)

        #self.text_widget.see(END)
        
        user_input = msg
        if user_input.lower() =='quit':
            self.window.destroy()
        else:
             self.msg_entry.delete(0, END)
             msg1 = f"You: {msg}\n\n"
             self.text_widget.configure(state =NORMAL)
             self.text_widget.insert(END, msg1)
             self.text_widget.configure(state=DISABLED)
            #self.text_widget.insert(tk.END, "You: "+user_input+"\n\n")
             #self.text_widget.insert(tk.END,  f"{bot_name}: ")
             bot_response = get_response(user_input)
             self.text_widget.configure(state =NORMAL)
             self.text_widget.insert(tk.END, f"{bot_name}  ")
             self.display_response_letter_by_letter(bot_response)
             #self.text_widget.insert (END,  f"{bot_name}: {self.display_response_word_by_word(bot_response)}\n\n")
             #self.text_widget.configure(state =NORMAL)
             #self.text_widget.insert(END, msg2)
             #self.text_widget.configure(state=DISABLED)
             #self.text_widget.see(END)
            #bot_response_generator = get_response(msg)
            #self.text_widget.insert(tk.END , "Bot: ")
           
            #for word in bot_response:
               # msg2 = f"{bot_name}: {display_response_word_by_word(bot_response)}\n\n"
                
            
                
                #self.msg_entry.delete(0, tk.END)
            #self.text_widget.insert(tk.END, "\n\n")
            
        #self.msg_entry.delete(0, tk.END)
            
        #self.text_widget.see(END)

        #def display_response_word_by_word(response):
         #   words = response.split()
          #  current_word_index = 0
           # def display_word():
            #    nonlocal current_word_index
             #   if current_word_index < len(words):
              #          self.text_widget.insert(tk.END, words[current_word_index] + " ")
               #         current_word_index +=1
                #        self.window.after(500, display_word)

            #display_word()
    

if __name__ =="__main__":
    interface = BotInterface()
    interface.run()