from datetime import datetime
from tkinter import *
from tkinter import PhotoImage
from time import sleep
from time import strftime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import connectingdb



df=pd.DataFrame(connectingdb.rows,columns = connectingdb.columns)
    


class Main_Screen:
    obj=None
    def __init__(self):
        
        self.window=Tk()
        
        self.window.state('zoomed')
        
        self.frame = Frame(self.window,bg="#2C3E50",width=300,height=750)
        self.frame.place(x=0,y=0)

        self.frame2 = Frame(self.window,bg="White",width=1500,height=2000)
        self.frame2.place(x=300,y=0)
        
        
        
        self.image=PhotoImage(file="clockw.png")
        self.image2=PhotoImage(file="profileicon.png")
        
        self.now = datetime.now()

        self.crrentdate=self.now.date()

        self.time=Label(self.window,font=("Times New Roman",24),fg="white",bg="#2C3E50")
        self.time.place(x=100,y=10)

        self.date=Label(self.frame,text=self.crrentdate,font=("Times New Roman",24),fg="white",bg='#2C3E50').place(x=60,y=60)

        self.mainscreen_label=Label(self.frame2,text="Main Screen",bg="white",font=("Times New Roman",24))
        self.mainscreen_label.place(x=450,y=0)
        
        Label(self.frame,text="Ammar Asif",font=("bahnschrift",24),fg="white",bg='#2C3E50').place(x=53,y=250)
        
        self.image_label=Label(self.frame,image=self.image,bg='#2C3E50',fg="white")
        self.image_label.place(x=50,y=10)
        
        self.image2_label=Label(self.frame,image=self.image2,bg='#2C3E50')
        self.image2_label.place(x=93,y=140)
        
        self.k=df[df["Condition"]=="Heart Attack"]
        self.heartattackrate=round((self.k["Condition"].count()/df["Condition"].count())*100,2)
        
        
        self.inforcard1=Frame(self.frame2,bg="#5dade2",width=340,height=110, bd=2, relief="ridge" )
        self.inforcard1.place(x=60,y=400)

        self.inforcard2=Frame(self.frame2,bg="#e74c3c",width=340,height=110, bd=2, relief="ridge")
        self.inforcard2.place(x=60,y=550)
        
        
        
        Label(self.inforcard1,text="👥 Total Patients:",font=("bahnschrift",24),fg="white",bg="#5dade2").place(x=50,y=0)

        Label(self.inforcard1,text=df["Patient_ID"].count(),font=("bahnschrift",44),fg="white",bg="#5dade2").place(x=120,y=40)
        
        Label(self.inforcard2,text="⚠️ Heart Attack Rate:",font=("bahnschrift",24),fg="white",bg="#e74c3c").place(x=6,y=0)

        Label(self.inforcard2,text=f"{self.heartattackrate}%",font=("bahnschrift",44),fg="white",bg="#e74c3c").place(x=100,y=40)
        
        
        self.age_sect=Button(self.frame,text="📈 Age type Analysis",font=("bahnschrift",19),fg="white",padx=23,pady=35,bg="#2C3E50",borderwidth=0,activebackground="#2C3E50",activeforeground="white",command=lambda:self.goto_age_sect()).place(x=0,y=300)
        self.finance_sect=Button(self.frame,text="💰 Financial Analysis",font=("bahnschrift",19),fg="white",padx=26,pady=35,bg="#2C3E50",borderwidth=0,activebackground="#2C3E50",activeforeground="white",command=lambda:self.goto_finance_sect()).place(x=0,y=400)
        self.patient_sect=Button(self.frame,text="🛌 Patient type Analysis",font=("bahnschrift",19),fg="white",padx=5,pady=35,bg="#2C3E50",borderwidth=0,activebackground="#2C3E50",activeforeground="white",command=lambda:self.goto_patient_sect()).place(x=0,y=500)
        self.mainscreen=Button(self.frame,text="*goto main screen",font=("bahnschrift",19),fg="white",padx=23,pady=35,bg="#2C3E50",borderwidth=0,activebackground="#2C3E50",activeforeground="white",command=lambda:self.goto_Main_Screen()).place(x=10,y=604)

        
        
        
        
        
        Main_Screen.obj=self
    

        self.update_time()
        self.create_gender_graph()
        self.create_rtvsft_graph()
        self.create_disease_chart()
        
        Age_Section()
        Finance_Section()
        Patient_Section()
        
        
        self.window.after(70,self.show_gender_graph)
        self.window.after(70,self.show_rtvsft_graph)
        self.window.after(70,self.show_disease_graph)
        
        
        self.window.mainloop()
        
        
    
    def update_time(self):
        self.current_time = strftime("%H:%M:%S")
        self.time.config(text=self.current_time)
        self.time.after(1000,self.update_time)
    
    def goto_age_sect(self):
        self.frame2.place_forget()  
        Finance_Section.financesect_obj.financesect_frame.place_forget()
        Patient_Section.patientsect_obj.patientsect_frame.place_forget()
        Age_Section.agesect_obj.agesect_frame.place(x=300, y=0)
    
    
    def goto_finance_sect(self):
        self.frame2.place_forget()  
        Age_Section.agesect_obj.agesect_frame.place_forget()
        Patient_Section.patientsect_obj.patientsect_frame.place_forget()
        Finance_Section.financesect_obj.financesect_frame.place(x=300, y=0)

    
    def goto_patient_sect(self):
        self.frame2.place_forget()  
        Finance_Section.financesect_obj.financesect_frame.place_forget()
        Age_Section.agesect_obj.agesect_frame.place_forget()
        Patient_Section.patientsect_obj.patientsect_frame.place(x=300, y=0)

    
    
    def goto_Main_Screen(self):
        Finance_Section.financesect_obj.financesect_frame.place_forget()
        Age_Section.agesect_obj.agesect_frame.place_forget()
        Patient_Section.patientsect_obj.patientsect_frame.place_forget()
        self.frame2.place(x=300,y=0)

    def show_gender_graph(self):
        
        
        self.canvas = FigureCanvasTkAgg(self.gender_graph, master=self.frame2)
        self.canvas.draw()
        self.canvas.get_tk_widget().place(x=60,y=60)

    def create_gender_graph(self):
        
        self.genders=df["Gender"].value_counts().index.tolist()
        self.num=df["Gender"].value_counts().values.tolist()
        self.gender_graph,ax=plt.subplots(figsize=(3,3))

        self.barplot=ax.bar(self.genders,self.num,color=["pink","lightblue"],ec="black")
        ax.bar_label(self.barplot,labels=self.num,label_type="center")
        ax.set_title("Number of Male/Female Patients")
    
    def show_rtvsft_graph(self):
        
        self.canvas = FigureCanvasTkAgg(self.ft_vs_rt, master=self.frame2)
        self.canvas.draw()
        self.canvas.get_tk_widget().place(x=600,y=60)
    

    def create_rtvsft_graph(self):
       
        self.k=df["Readmission"].value_counts().index.tolist()
        self.l=df["Readmission"].value_counts().values.tolist()
        
        
        
        self.ft_vs_rt,ax=plt.subplots(figsize=(4,3))
        self.myexplode=[0.0,0.1]
        
        ax.pie(self.l,labels=["First time","Returning"],explode=self.myexplode,autopct='%1.1f%%')
        ax.set_title("Proportion of First-Time and Returning Patients")
    
    def show_disease_graph(self):
        
        
        self.canvas = FigureCanvasTkAgg(self.agegrp_disease_chart, master=self.frame2)
        self.canvas.draw()
        self.canvas.get_tk_widget().place(x=680,y=400)
        
    def create_disease_chart(self):
        
       self.num_of_patients=df["Condition"].value_counts().values.tolist()
       self.total_cases=0
       for i in self.num_of_patients:
        self.total_cases+=i
       
       
       self.df_3=df[df["Age"].isin(range(25,30))]
       self.t=self.df_3[["Age","Condition"]].value_counts().tolist()

       self.cases_25to30=0
       for i in self.t:
        self.cases_25to30+=i
       
       self.percentage_25_to_30=round((self.cases_25to30/self.total_cases)*100,2)

       
       
       self.df_4=df[df["Age"].isin(range(30,40))]
       self.k=self.df_4[["Age","Condition"]].value_counts().tolist()

       self.cases_30to40=0
       for i in self.k:
        self.cases_30to40+=i

       self.percentage_30_to_40=round((self.cases_30to40/self.total_cases)*100,2)

       
       
       self.df_4=df[df["Age"].isin(range(40,50))]
       self.o=self.df_4[["Age","Condition"]].value_counts().tolist()

       self.cases_40to50=0
       for i in self.o:
        self.cases_40to50+=i

       self.percentage_40_to_50=round((self.cases_40to50/self.total_cases)*100,2)
       
       
       
       self.df_5=df[df["Age"].isin(range(50,60))]
       self.p=self.df_5[["Age","Condition"]].value_counts().tolist()

       self.cases_50to60=0
       for i in self.p:
        self.cases_50to60+=i

       self.percentage_50_to_60=round((self.cases_50to60/self.total_cases)*100,2)

       
       
       self.df_6=df[df["Age"].isin(range(60,70))]
       self.y=self.df_6[["Age","Condition"]].value_counts().tolist()
       
       self.cases_60to70=0
       for i in self.y:
        self.cases_60to70+=i

       self.percentage_60_to_70=round((self.cases_60to70/self.total_cases)*100,2)

       
       
       self.df_7=df[df["Age"].isin(range(70,80))]
       self.y=self.df_7[["Age","Condition"]].value_counts().tolist()

       self.cases_70to80=0
       for i in self.y:
        self.cases_70to80+=i
       
       self.percentage_70_to_80=round((self.cases_70to80/self.total_cases)*100,2) 

       
       
       self.agegrp_disease_chart,ax=plt.subplots(figsize=(3,3))
       self.myexplode = [0,0,0,0.1,0,0]
       print(self.percentage_25_to_30,"\n",self.percentage_30_to_40)
       ax.pie([int(self.percentage_25_to_30),int(self.percentage_30_to_40),int(self.percentage_40_to_50),int(self.percentage_50_to_60),int(self.percentage_60_to_70),int(self.percentage_70_to_80)],labels=["20s","30s","40s","50s","60s","70s"],explode=self.myexplode,colors=['#1abc9c', '#f39c12', '#9b59b6', '#e74c3c', '#5dade2', '#34495e'])
       ax.set_title("Age Group Disease Analysis")

class Age_Section:
    agesect_obj=None
    def __init__(self):
        self.agesect_frame=Frame(Main_Screen.obj.window,bg='white',width=1500,height=2000)
        
        
        self.yng_patients=df[(df["Age"]>18) & (df["Age"]<=45)]
        self.yng_patients_prnctg=round((int(self.yng_patients["Age"].count())/df["Age"].count())*100,1)
        
        self.avgpatients=round(df["Age"].mean(),2)
        
        
        self.inforcard1=Frame(self.agesect_frame,bg="#E74C3C",width=220,height=100, bd=2, relief="ridge" )
        self.inforcard1.place(x=720,y=400)
    
        self.inforcard2=Frame(self.agesect_frame,bg="#27ae60",width=122,height=100, bd=2, relief="ridge" )
        self.inforcard2.place(x=930,y=400)
        
        
        self.inforcard3=Frame(self.agesect_frame,bg="#3498db",width=335,height=110, bd=2, relief="ridge" )
        self.inforcard3.place(x=720,y=500)
        
        Label(self.inforcard1,text="Oldest Patient",font=("bahnschrift",20),fg="white",bg="#E74C3C").place(x=10,y=0)

        Label(self.inforcard1,text=df["Age"].max(),font=("bahnschrift",34),fg="white",bg="#E74C3C").place(x=55,y=40)

        Label(self.inforcard2,text="YNG %",font=("bahnschrift",20),fg="white",bg="#27ae60").place(x=20,y=0)

        Label(self.inforcard2,text=self.yng_patients_prnctg,font=("bahnschrift",34),fg="white",bg="#27ae60").place(x=20,y=40)
        
        Label(self.inforcard3,text="Avg Patient Age",font=("bahnschrift",20),fg="white",bg="#3498db").place(x=66,y=0)

        Label(self.inforcard3,text=self.avgpatients,font=("bahnschrift",34),fg="white",bg="#3498db").place(x=96,y=40)
        
        
        
        Age_Section.agesect_obj=self
        self.create_age_distribution_chart()
        self.create_satisfaction_score_graph()
        self.create_avg_revenue_per_age()
        
        
        
        Main_Screen.obj.window.after(70,self.show_age_distribution_chart)
        Main_Screen.obj.window.after(70,self.show_satisfaction_score_chart)
        Main_Screen.obj.window.after(70,self.show_avg_revenue_per_age)
        
    
        
    def show_age_distribution_chart(self):
        self.age_distribution_graph.tight_layout()
        self.canvas = FigureCanvasTkAgg(self.age_distribution_graph, master=self.agesect_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().place(x=30,y=0)
    
    def create_age_distribution_chart(self):
        
        self.df_4=df[df["Age"].isin(range(25,30))]
        self.total_25to30_patients=self.df_4["Age"].count()

        self.df_5=df[df["Age"].isin(range(30,40))]
        self.total_30to40_patients=self.df_4["Age"].count()
        
        self.df_4=df[df["Age"].isin(range(40,50))]
        self.total_40to50_patients=self.df_4["Age"].count()

        self.df_4=df[df["Age"].isin(range(50,60))]
        self.total_50to60_patients=self.df_4["Age"].count()
        
        self.df_4=df[df["Age"].isin(range(60,70))]
        self.total_60to70_patients=self.df_4["Age"].count()

        self.df_4=df[df["Age"].isin(range(70,80))]
        self.total_70to80_patients=self.df_4["Age"].count()

        self.age_distribution_graph,ax=plt.subplots(figsize=(3,3))
        self.bar_plot=ax.barh(["25 to 30","30 to 40","40 to 50","50 to 60","60 to 70","70 to 80"],[self.total_25to30_patients,self.total_30to40_patients,self.total_40to50_patients,self.total_50to60_patients,self.total_60to70_patients,self.total_70to80_patients],color="#1E88E5",ec="black")
        lables=ax.bar_label(self.bar_plot,labels=[self.total_25to30_patients,self.total_30to40_patients,self.total_40to50_patients,self.total_50to60_patients,self.total_60to70_patients,self.total_70to80_patients],label_type="center",padding=3)
        
        for label in lables:
            label.set_color("white") 
            label.set_fontsize(13)
        self.x=ax.set_xlabel("Number Of Patients")
        ax.set_title("Age Distribution graph")


    
    def show_satisfaction_score_chart(self):
        self.satisfaction_score.tight_layout()
        self.canvas = FigureCanvasTkAgg(self.satisfaction_score, master=self.agesect_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().place(x=30,y=400)
    
    
    def create_satisfaction_score_graph(self):
        self.lables=["25 to 30","30 to 40","40 to 50","50 to 60","60 to 70","70 to 80"]

        self.df_5=df[df["Age"].isin(range(25,30))]
        self.ratings25=round(self.df_5["Satisfaction"].mean(),1)
        
        self.df_6=df[df["Age"].isin(range(30,40))]
        self.ratings30=round(self.df_6["Satisfaction"].mean(),1)

        self.df_7=df[df["Age"].isin(range(40,50))]
        self.ratings40=round(self.df_7["Satisfaction"].mean(),1)

        self.df_8=df[df["Age"].isin(range(50,60))]
        self.ratings50=round(self.df_8["Satisfaction"].mean(),1)

        self.df_9=df[df["Age"].isin(range(60,70))]
        self.ratings60=round(self.df_9["Satisfaction"].mean(),1)

        self.df_10=df[df["Age"].isin(range(70,80))]
        self.ratings70=round(self.df_10["Satisfaction"].mean(),1)

        self.satisfaction_score,ax=plt.subplots(figsize=(3,3))

        self.bar_plot=ax.barh(self.lables,[self.ratings25,self.ratings30,self.ratings40,self.ratings50,self.ratings60,self.ratings70],color="#1E88E5",ec="Black")

        lables=ax.bar_label(self.bar_plot,labels=[self.ratings25,self.ratings30,self.ratings40,self.ratings50,self.ratings60,self.ratings70],label_type="center",padding=3)

        for label in lables:
            label.set_color("white")
            label.set_fontsize(13)
        
        ax.set_title("Avg Ratings per Age")
        
        ax.set_xlabel("Satisfaction Score")

    def show_avg_revenue_per_age(self):
        self.avg_cost_per_age.tight_layout()
        self.canvas = FigureCanvasTkAgg(self.avg_cost_per_age, master=self.agesect_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().place(x=700,y=0)
    
    
    
    def create_avg_revenue_per_age(self):
        
        self.lables=["25 to 30","30 to 40","40 to 50","50 to 60","60 to 70","70 to 80"]
        
        self.df_5=df[df["Age"].isin(range(25,30))]
        self.avgcost25=round(self.df_5["Cost"].mean(),2)

        self.df_6=df[df["Age"].isin(range(30,40))]
        self.avgcost30=round(self.df_6["Cost"].mean(),2)
        
        self.df_7=df[df["Age"].isin(range(40,50))]
        self.avgcost40=round(self.df_7["Cost"].mean(),2)

        self.df_8=df[df["Age"].isin(range(50,60))]
        self.avgcost50=round(self.df_8["Cost"].mean(),2)

        self.df_9=df[df["Age"].isin(range(60,70))]
        self.avgcost60=round(self.df_9["Cost"].mean(),2)
        
        self.df_10=df[df["Age"].isin(range(70,80))]
        self.avgcost70=round(self.df_10["Cost"].mean(),2)

        self.avg_cost_per_age,ax=plt.subplots(figsize=(3,3))

        ax.barh(self.lables,[self.avgcost25,self.avgcost30,self.avgcost40,self.avgcost50,self.avgcost60,self.avgcost70],color="#1E88E5",ec="black")
        lables=ax.bar_label(self.bar_plot,labels=[self.avgcost25,self.avgcost30,self.avgcost40,self.avgcost50,self.avgcost60,self.avgcost70],padding=3)
        
        for label in lables:
            label.set_color("white")
            label.set_fontsize(13)
            label.set_fontsize(13)
        
        ax.set_title("Average Cost by Age")
       
        ax.set_xlabel("Cost")

            
    

class Finance_Section:
    finance_obj=None
    def __init__(self):
        self.financesect_frame=Frame(Main_Screen.obj.window,bg='white',width=1500,height=2000)
        

        
        Finance_Section.financesect_obj=self

        self.creating_revenue_graph()
        
        Main_Screen.obj.window.after(70,self.show_revenue_graph)

    def show_revenue_graph(self):
        self.rev_gen_proced.tight_layout()
        
        self.canvas = FigureCanvasTkAgg(self.rev_gen_proced, master=self.financesect_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().place(x=40,y=60)
    
    
    def creating_revenue_graph(self): 
       
       self.df_2=df[["Procedure","Cost"]]
       self.var=self.df_2.value_counts().index.tolist()
       
       self.procedures=[]
       for i in range(len(self.var)):
         self.procedures.append(self.var[i][0])
       
       self.x=df[["Condition","Cost"]].value_counts().index.tolist()
       self.y=df[["Condition","Cost"]].value_counts().values.tolist()
       
       
       self.list1=[]

       for i in range(len(self.x)):
        self.d=self.x[i][1] * self.y[i]
        self.list1.append(self.d)

       self.r=df[["Condition"]].value_counts().index.tolist()
       
    
       self.rev_gen_proced,ax=plt.subplots(figsize=(7,5))
       self.box_plot=ax.barh(self.procedures,self.list1,color="#1E88E5",ec="black")
       ax.bar_label(self.box_plot,labels=self.list1,padding=3)
       ax.set_xlabel("Values (1.0 = 1 million)")
       
       ax.set_title("Revenue Generated per Procedure")

class Patient_Section:
    patientsect_obj=None
    def __init__(self):
        self.patientsect_frame=Frame(Main_Screen.obj.window,bg='white',width=1500,height=2000)
        

        Label(self.patientsect_frame,bg='white',text="Patient Section",font=("Times New Roman",24)).place(x=600,y=0)

        Patient_Section.patientsect_obj=self


Main_Screen()

