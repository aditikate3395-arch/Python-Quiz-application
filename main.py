
import sqlite3
import tkinter as tk
from tkinter import messagebox
conn=sqlite3.connect("quiz.db")
cursor=conn.cursor()
cursor.execute(""" Create table if not exists scores(username text,category text,score int)""")
conn.commit()
python_questions=[{
    "question":"python is a ?",
    "options":["Programming language","Browser","Game","Operating system"],
    "answer":1
},
{
    "question":"Which keyword is used to declare function in python",
    "options":["fun","define","def","function"],
    "answer":3
},
{
    "question":"which datatype stores multiple values in python",
    "options":["int","list","float","boolean"],
    "answer":2
},
{
    "question":"which loop is used when number of iterations known?",
    "options":["while","do-while","switch","for"],
    "answer":4
},
{
    "question":"Which symbol is used for comments in python?",
    "options":["//","#","/*","*/","--"],
    "answer":2
}
]
SQL_questions=[{
    "question":"what is full-form of DBMS",
    "options":["Database management system","Data backup management system","Digital base management system","Database memory system"],
    "answer":1
},
{
    "question":"Which cammond is used to display data in SQL?",
    "options":["GET","SHOW","SELECT","DISPLAY"],
    "answer":3
},
{
    "question":"Which command is used to remove all records from table?",
    "options":["DELETE","REMOVE","DROP","TRUNCATE"],
    "answer":4
},
{
    "question":"Which SQL clause is used to filter records?",
    "options":["ORDER BY","GROUP BY","WHERE","FILTER"],
    "answer":3
},
{
    "question":"which key uniquely identifies each record in table?",
    "options":["Foreign key","primary key","unique key","main key"],
    "answer":2 
}
]
C_questions=[{
    "question":"Which function is used to print output in C?",
    "options":["scanf()","printf()","print()","cout"],
    "answer":2
},
{
    "question":"Which header file required for input/output in C?",
    "options":["math.h","string.h","stdio.h","conio.h"],
    "answer":3
},
{
    "question":"What is size of char datatype in C?",
    "options":["1 byte","2 bytes","4 bytes","8 bytes"],
    "answer":1
},
{
    "question":"Which symbol is used to end statement in C?",
    "options":[":",".",";","!"],
    "answer":3
},
{
    "question":"Which datatype store a single character in C?",
    "options":["char","string","text","character"],
    "answer":1
}
]

current_questions = []
current_question = 0
score = 0
category_name = ""
 
root=tk.Tk()
root.geometry("600x700")
root.title("Quiz APP")
root.config(bg="#1e1e1e")
# current_question=0
# score=0
selected_option=tk.IntVar()

title_label=tk.Label(
    root,
    text="QUIZ APPLICATION",
    font=("Arial",20,"bold"),
    bg="#1e1e1e",
    fg="cyan"
)
title_label.pack(pady=10)


question_label=tk.Label(
    root,
    text="Select a quiz",
    font=("Arial",16,"bold"),
    bg="#1e1e1e",
    fg="white",
    wraplength=400
)
question_label.pack(pady=20)


option1=tk.Radiobutton(
    root,
    text="",
    variable=selected_option,
    value=1,
    font=("Arial",12),
    bg="#1e1e1e",
    fg="white",
    selectcolor="#333333",
    activebackground="#1e1e1e"
)
option1.pack()

option2=tk.Radiobutton(
    root,
    text="",
    variable=selected_option,
    value=2,
    font=("Arial",12),
    bg="#1e1e1e",
    fg="white",
    selectcolor="#333333",
    activebackground="#1e1e1e"
)
option2.pack()
option3=tk.Radiobutton(
    root,
    text="",
    variable=selected_option,
    value=3,
    font=("Arial",12),
    bg="#1e1e1e",
    fg="white",
    selectcolor="#333333",
    activebackground="#1e1e1e"
)
option3.pack()

option4=tk.Radiobutton(
    root,
    text="",
    variable=selected_option,
    value=4,
    font=("Arial",12),
    bg="#1e1e1e",
    fg="white",
    selectcolor="#333333",
    activebackground="#1e1e1e"
)
option4.pack()
option1.config(state="disabled")
option2.config(state="disabled")
option3.config(state="disabled")
option4.config(state="disabled")


    
def start_quiz(questions, category):
    global current_questions, current_question, score, category_name

    current_questions = questions
    current_question = 0
    score = 0
    category_name = category

    python_button.pack_forget()
    SQL_button.pack_forget()
    C_button.pack_forget()
    
   
    Next_button.config(state="normal")
    option1.config(state="normal")
    option2.config(state="normal")
    option3.config(state="normal")
    option4.config(state="normal")

    show_question()

def show_question():
    selected_option.set(0)
    
    q=current_questions[current_question]

    question_label.config(text=q["question"])
    option1.config(text=q["options"][0])
    option2.config(text=q["options"][1])
    option3.config(text=q["options"][2])
    option4.config(text=q["options"][3])


def next_question():
     
     global current_question,score
     if selected_option.get() == 0:
        messagebox.showwarning("Warning", "Please select an option first")
        return

     q = current_questions[current_question]

     if selected_option.get() == q["answer"]:
        score += 1
        
    
     current_question+= 1

     if current_question < len(current_questions):
        show_question()
     else:
        messagebox.showinfo("Quiz Finished", f"Your Score: {score}/{len(current_questions)}")

        question_label.config(text=f"Quiz Finished! Score: {score}/{len(current_questions)}")

        option1.config(text="")
        option2.config(text="")
        option3.config(text="")
        option4.config(text="")
        selected_option.set(0)

        option1.config(state="disabled")
        option2.config(state="disabled")
        option3.config(state="disabled")
        option4.config(state="disabled")

        cursor.execute(
            "INSERT INTO scores VALUES (?,?,?)",
            ("Guest", category_name, score)
        )
        conn.commit()
        python_button.pack(pady=10)
        SQL_button.pack(pady=10)
        C_button.pack(pady=10)
        
        Next_button.config(state="disabled")




python_button = tk.Button(
    root,
    text="Python Quiz",
    command=lambda: start_quiz(python_questions, "Python"),
    bg="#4CAF50",
    fg="white",
    font=("Arial",12,"bold"),
    width=20
)
python_button.pack(pady=10)

SQL_button = tk.Button(
    root,
    text="SQL Quiz",
    command=lambda: start_quiz(SQL_questions, "SQL"),
    bg="#2196F3",
    fg="white",
    font=("Arial",12,"bold"),
    width=20
)
SQL_button.pack(pady=10)

C_button = tk.Button(
    root,
    text="C Quiz",
    command=lambda: start_quiz(C_questions, "C"),
    bg="#FF9800",
    fg="white",
    font=("Arial",12,"bold"),
    width=20
)
C_button.pack(pady=10)

Next_button = tk.Button(
    root,
    text="Next Question",
    command=next_question,
    state='disabled',
    bg="purple",
    fg="white",
    font=("Arial",12,"bold"),
    width=20
)
Next_button.pack(pady=20)

root.mainloop()     

conn.close()









