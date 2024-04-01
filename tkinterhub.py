import tkinter as tk
x=tk.Tk()
x.geometry("500x500")
x.title("TKINTER HUB")
main_frame=tk.Frame(x)
page_1=tk.Frame(main_frame)
page_1_lb=tk.Label(page_1,text="page1",font=("bold",20))
page_1_lb.pack()
page_1.pack(pady=100)
page_2=tk.Frame(main_frame)
page_2_lb=tk.Label(page_2,text="page2",font=("bold",20))
page_2_lb.pack()
page_3=tk.Frame(main_frame)
page_3_lb=tk.Label(page_3,text="page3",font=("bold",20))
page_3_lb.pack()
page_4=tk.Frame(main_frame)
page_4_lb=tk.Label(page_4,text="page4",font=("bold",20))
page_4_lb.pack()
page_5=tk.Frame(main_frame)
page_5_lb=tk.Label(page_5,text="page5",font=("bold",20))
page_5_lb.pack()
page_6=tk.Frame(main_frame)
page_6_lb=tk.Label(page_6,text="page6",font=("bold",20))
page_6_lb.pack()
page_7=tk.Frame(main_frame)
page_7_lb=tk.Label(page_7,text="page7",font=("bold",20))
page_7_lb.pack()
page_8=tk.Frame(main_frame)
page_8_lb=tk.Label(page_8,text="page8",font=("bold",20))
page_8_lb.pack()

pages=[page_1,page_2,page_3,page_4,page_5,page_6,page_7,page_8]
count=0
def move_next_page():
    global count
    if not count>len(pages)-2:
        for p in pages:
            p.pack_forget()
        count+=1
        page=pages[count]
        page.pack(pady=100)
def move_back_page():
    global count
    if not count==0:
        for p in pages:
            p.pack_forget()
        count-=1
        page=pages[count]
        page.pack(pady=100)
    
        

main_frame.pack(fill=tk.BOTH,expand=True)
bottom_frame=tk.Frame(x)
back_btn=tk.Button(bottom_frame,text="BACK",font=("bold",12),bg='#1877f2',command=move_back_page)
back_btn.pack(side=tk.LEFT,padx=10)
next_btn=tk.Button(bottom_frame,text="NEXT",font=("bold",12),bg='#1877f2',command=move_next_page)
next_btn.pack(side=tk.LEFT,padx=10)
bottom_frame.pack(side=tk.BOTTOM,pady=10)

x.mainloop()
