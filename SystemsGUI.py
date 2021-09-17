import tkinter
from tkinter import ttk
from tkinter import StringVar
from tkinter import messagebox
from tkinter import Entry
from tkinter import Button
from tkinter import scrolledtext
import numpy as np
from PIL import ImageTk, Image
from System_Simulator import *
from statespace import *


class Sys(tkinter.Frame):

    def getting_parameters(self):
        ch1=self.checking()
        if(ch1==False):
            return False
        ch2=self.error_in_coeff()
        if(ch2==False):
            messagebox.showerror('Error','Missing coefficient')
            return False
        ch3=self.error_in_coeff_vol2()
        if(ch3==False):
            messagebox.showerror('Error','Missing coefficient')
            return False
        else:
            m=int(self.m.get())
            n=int(self.n.get())
            all_coeffs=self.coeff_to_array_vol2()
            Time=int(self.time_meter.get())
            Input_Type=self.input_type.get()
            OP_plotter(m, n, all_coeffs, Time, Input_Type)
    


    def getting_parameters1(self):
        ch1=self.checking()
        if(ch1==False):
            return False
        ch2=self.error_in_coeff()
        if(ch2==False):
            messagebox.showerror('Error','Missing coefficient')
            return False
        ch3=self.error_in_coeff_vol2()
        if(ch3==False):
            messagebox.showerror('Error','Missing coefficient')
            return False
        else:
            m=int(self.m.get())
            n=int(self.n.get())
            all_coeffs=self.coeff_to_array_vol2()
            Time=int(self.time_meter.get())
            Input_Type=self.input_type.get()
            IP_plotter(m, n, all_coeffs, Time, Input_Type)
    


    def getting_parameters2(self):
        ch1=self.checking()
        if(ch1==False):
            return False
        ch2=self.error_in_coeff()
        if(ch2==False):
            messagebox.showerror('Error','Missing coefficient')
            return False
        ch3=self.error_in_coeff_vol2()
        if(ch3==False):
            messagebox.showerror('Error','Missing coefficient')
            return False
        else:
            m=int(self.m.get())
            n=int(self.n.get())
            all_coeffs=self.coeff_to_array_vol2()
            Time=int(self.time_meter.get())
            Input_Type=self.input_type.get()
            ss_visualization(m, n, all_coeffs, Time, Input_Type)



    def test_val(self,inStr,acttyp):
        if(acttyp=='1'):
            try:
                if (isinstance(float(inStr), float)):
                    1
            except:
                return False
        return True

    
    def disable_combobox(self,event):
        if(self.input_type.get()=="Impulse" or self.input_type.get()=="Step"):
            self.m.config(state='disabled')
            self.m.set(0)
        else:
            self.m.config(state='readonly')


    def opening_new_entry(self,event):
        if(self.input_type.get()=="Sine"):
            self.l15.grid(pady=(20,0), columnspan=4, padx=(0,530), column=2, row=9)
            self.input_type.grid(column=2, columnspan=4, padx=(0,530), row=10)
            self.label_sine.grid(pady=(20,0),padx=(65,0), columnspan=4, column=3, row=9)
            self.entry_sine.grid(padx=(65,0), columnspan=4, column=3, row=10)
        elif(self.input_type.get()=="Cosine"):
            self.l15.grid(pady=(20,0), columnspan=4, padx=(0,530), column=2, row=9)
            self.input_type.grid(column=2, columnspan=4, padx=(0,530), row=10)
            self.label_cosine.grid(pady=(20,0),padx=(65,0), columnspan=4, column=3, row=9)
            self.entry_cosine.grid(padx=(65,0), columnspan=4, column=3, row=10)
        elif(self.input_type.get()=="Exponential"):
            self.l15.grid(pady=(20,0), columnspan=4, padx=(0,530), column=2, row=9)
            self.input_type.grid(column=2, columnspan=4, padx=(0,530), row=10)
            self.label_exp.grid(pady=(20,0),padx=(65,0), columnspan=4, column=3, row=9)
            self.entry_exp.grid(padx=(65,0), columnspan=4, column=3, row=10)
        elif(self.input_type.get()=="Polynomial"):
            self.l15.grid(pady=(20,0), columnspan=4, padx=(0,530), column=2, row=9)
            self.input_type.grid(column=2, columnspan=4, padx=(0,530), row=10)
            self.label_poly.grid(pady=(20,0), padx=(65,0), columnspan=4, column=3, row=9)
            self.entry_t3.grid(padx=(0,105), columnspan=4, column=3, row=10)
            self.label_t3.grid(padx=(100,0), columnspan=2, column=3, row=10)
            self.entry_t2.grid(padx=(15,0), columnspan=3, column=3, row=10)
            self.label_t2.grid(padx=(220,0), columnspan=2, column=3, row=10)
            self.entry_t1.grid(padx=(138,0), columnspan=3, column=3, row=10)
            self.label_t1.grid(padx=(335,0), columnspan=2, column=3, row=10)
            self.entry_t0.grid(padx=(243,0), columnspan=3, column=3, row=10)



    def changing_options(self,event):
        if(self.input_type.get()=="Impulse" or self.input_type.get()=="Step"):
            self.label_sine.grid_forget()
            self.entry_sine.grid_forget()
            self.label_cosine.grid_forget()
            self.entry_cosine.grid_forget()
            self.label_exp.grid_forget()
            self.entry_exp.grid_forget()
            self.label_poly.grid_forget()
            self.entry_t3.grid_forget()
            self.label_t3.grid_forget()
            self.entry_t2.grid_forget()
            self.label_t2.grid_forget()
            self.entry_t1.grid_forget()
            self.label_t1.grid_forget()
            self.entry_t0.grid_forget()
            self.l15.grid_forget()
            self.input_type.grid_forget()
            self.l15.grid(pady=(20,0), column=3, row=9)
            self.input_type.grid(column=3, row=10)
        if(self.input_type.get()=="Sine"):
            self.label_cosine.grid_forget()
            self.entry_cosine.grid_forget()
            self.label_exp.grid_forget()
            self.entry_exp.grid_forget()
            self.label_poly.grid_forget()
            self.entry_t3.grid_forget()
            self.label_t3.grid_forget()
            self.entry_t2.grid_forget()
            self.label_t2.grid_forget()
            self.entry_t1.grid_forget()
            self.label_t1.grid_forget()
            self.entry_t0.grid_forget()
            self.l15.grid_forget()
            self.input_type.grid_forget()
            self.in12.set('')
            self.in13.set('')
            self.in14.set('')
            self.in15.set('')
            self.in16.set('')
            self.in17.set('')
            self.l15.grid(pady=(20,0), columnspan=4, padx=(0,530), column=2, row=9)
            self.input_type.grid(column=2, columnspan=4, padx=(0,530), row=10)
            self.label_sine.grid(pady=(20,0),padx=(65,0), columnspan=4, column=3, row=9)
            self.entry_sine.grid(padx=(65,0), columnspan=4, column=3, row=10)
        if(self.input_type.get()=="Cosine"):
            self.label_sine.grid_forget()
            self.entry_sine.grid_forget()
            self.label_exp.grid_forget()
            self.entry_exp.grid_forget()
            self.label_poly.grid_forget()
            self.entry_t3.grid_forget()
            self.label_t3.grid_forget()
            self.entry_t2.grid_forget()
            self.label_t2.grid_forget()
            self.entry_t1.grid_forget()
            self.label_t1.grid_forget()
            self.entry_t0.grid_forget()
            self.l15.grid_forget()
            self.input_type.grid_forget()
            self.in11.set('')
            self.in13.set('')
            self.in14.set('')
            self.in15.set('')
            self.in16.set('')
            self.in17.set('')
            self.l15.grid(pady=(20,0), columnspan=4, padx=(0,530), column=2, row=9)
            self.input_type.grid(column=2, columnspan=4, padx=(0,530), row=10)
            self.label_cosine.grid(pady=(20,0),padx=(65,0), columnspan=4, column=3, row=9)
            self.entry_cosine.grid(padx=(65,0), columnspan=4, column=3, row=10)
        if(self.input_type.get()=="Exponential"):
            self.label_sine.grid_forget()
            self.entry_sine.grid_forget()
            self.label_cosine.grid_forget()
            self.entry_cosine.grid_forget()
            self.label_poly.grid_forget()
            self.entry_t3.grid_forget()
            self.label_t3.grid_forget()
            self.entry_t2.grid_forget()
            self.label_t2.grid_forget()
            self.entry_t1.grid_forget()
            self.label_t1.grid_forget()
            self.entry_t0.grid_forget()
            self.l15.grid_forget()
            self.input_type.grid_forget()
            self.in11.set('')
            self.in12.set('')
            self.in14.set('')
            self.in15.set('')
            self.in16.set('')
            self.in17.set('')
            self.l15.grid(pady=(20,0), columnspan=4, padx=(0,530), column=2, row=9)
            self.input_type.grid(column=2, columnspan=4, padx=(0,530), row=10)
            self.label_exp.grid(pady=(20,0),padx=(65,0), columnspan=4, column=3, row=9)
            self.entry_exp.grid(padx=(65,0), columnspan=4, column=3, row=10)
        if(self.input_type.get()=="Polynomial"):
            self.label_sine.grid_forget()
            self.entry_sine.grid_forget()
            self.label_cosine.grid_forget()
            self.entry_cosine.grid_forget()
            self.label_exp.grid_forget()
            self.entry_exp.grid_forget()
            self.l15.grid_forget()
            self.input_type.grid_forget()
            self.in11.set('')
            self.in12.set('')
            self.in13.set('')
            self.l15.grid(pady=(20,0), columnspan=4, padx=(0,530), column=2, row=9)
            self.input_type.grid(column=2, columnspan=4, padx=(0,530), row=10)
            self.label_poly.grid(pady=(20,0), padx=(65,0), columnspan=4, column=3, row=9)
            self.entry_t3.grid(padx=(0,105), columnspan=4, column=3, row=10)
            self.label_t3.grid(padx=(100,0), columnspan=2, column=3, row=10)
            self.entry_t2.grid(padx=(15,0), columnspan=3, column=3, row=10)
            self.label_t2.grid(padx=(220,0), columnspan=2, column=3, row=10)
            self.entry_t1.grid(padx=(138,0), columnspan=3, column=3, row=10)
            self.label_t1.grid(padx=(335,0), columnspan=2, column=3, row=10)
            self.entry_t0.grid(padx=(243,0), columnspan=3, column=3, row=10)

        

    def checking(self):
        #if(not self.m.get().isdigit()):
            #messagebox.showerror('Error','m must be a number')
            #return False
        #if(not self.n.get().isdigit()):
            #messagebox.showerror('Error','n must be a number')
            #return False
        #if(self.m.get()>'4'):
            #messagebox.showerror('Error','m is out of range')
            #return False
        #if(self.n.get()>'4'):
            #messagebox.showerror('Error','n is out of range')
            #return False
        if(self.m.get()>self.n.get()):
            messagebox.showerror('Error','m must be a number less than or equal n')
            return False
        else:
            return True



    def error_in_coeff(self):
        if(self.m.get()=='0'):
            if(self.in6.get()!=''):
                return True
            else:
                return False
        if(self.m.get()=='1'):
            if(self.in6.get()!='' and self.in7.get()!=''):
                return True
            else:
                return False
        elif(self.m.get()=='2'):
            if(self.in6.get()!='' and self.in7.get()!='' and self.in8.get()!=''):
                return True
            else:
                return False
        elif(self.m.get()=='3'):
            if(self.in6.get()!='' and self.in7.get()!='' and self.in8.get()!='' and self.in9.get()!=''):
                return True
            else:
                return False
        elif(self.m.get()=='4'):
            if(self.in6.get()!='' and self.in7.get()!='' and self.in8.get()!='' and self.in9.get()!='' and self.in10.get()!=''):
                return True
            else:
                return False
        elif(self.n.get()=='0'):
            if(self.in1.get()!=''):
                return True
            else:
                return False
        elif(self.n.get()=='1'):
            if(self.in1.get()!='' and self.in2.get()!=''):
                return True
            else:
                return False
        elif(self.n.get()=='2'):
            if(self.in1.get()!='' and self.in2.get()!='' and self.in3.get()!=''):
                return True
            else:
                return False
        elif(self.n.get()=='3'):
            if(self.in1.get()!='' and self.in2.get()!='' and self.in3.get()!='' and self.in4.get()!=''):
                return True
            else:
                return False
        elif(self.n.get()=='4'):
            if(self.in1.get()!='' and self.in2.get()!='' and self.in3.get()!='' and self.in4.get()!='' and self.in5.get()!=''):
                return True
            else:
                return False
        


    def error_in_coeff_vol2(self):
        if(self.input_type.get()=="Sine"):
            if(self.in11.get()!=''):
                return True
            else:
                return False
        elif(self.input_type.get()=="Cosine"):
            if(self.in12.get()!=''):
                return True
            else:
                return False
        elif(self.input_type.get()=="Exponential"):
            if(self.in13.get()!=''):
                return True
            else:
                return False
        elif(self.input_type.get()=="Polynomial"):
            if(self.in14.get()!='' and self.in15.get()!='' and self.in16.get()!='' and self.in17.get()!=''):
                return True
            else:
                return False



    def createNewWindow3(self):
        ch1=self.checking()
        if(ch1==False):
            return False
        cond=self.error_in_coeff()
        if(cond==False):
            messagebox.showerror('Error','Missing coefficient')
            return False
        ch3=self.error_in_coeff_vol2()
        if(ch3==False):
            messagebox.showerror('Error','Missing coefficient')
            return False
        else:
            newWindow3 = tkinter.Toplevel(self.parent)
            newWindow3.title("State-Space Represtentaion")
            newWindow3.geometry('813x385')
            newWindow3.resizable(0,0)

            cond=self.error_in_coeff()
            if(cond==False):
                newWindow3.destroy()


            label_1 = tkinter.Label(newWindow3, text = "State-Space Represtentaion", font=("Times New Roman Bold", 30))
            label_1.place(relx=0.22,rely=0.01)
            txt1 = tkinter.scrolledtext.ScrolledText(newWindow3, height=7, width=39, undo=True)
            matrices=self.state_space_representaion(int(self.n.get()), int(self.m.get()))
            first = matrices['A']
            second = matrices['B']
            third = matrices['C']
            fourth = matrices['D']
            np.set_printoptions(precision=3, floatmode='fixed')
            txt1.insert('end','A:')
            txt1.insert('end',first)
            txt1.insert('end','\n')
            txt1.insert('end','B:')
            txt1.insert('end',second)
            txt1.insert('end','\n')
            txt1.insert('end','C:')
            txt1.insert('end',third)
            txt1.insert('end','\n')
            txt1.insert('end','D:')
            txt1.insert('end',fourth)
            txt1.config(font=("Times New Roman Bold", 30), state="disabled")
            txt1.place(relx=0.01,rely=0.15)


    def coeff_to_array(self):
        coeffs = []
        if(self.in1.get()!=''):
            float(self.in1.get())
            coeffs.append(float(self.in1.get()))
        if(self.in2.get()!=''):
            float(self.in2.get())
            coeffs.append(float(self.in2.get()))
        if(self.in3.get()!=''):
            float(self.in3.get())
            coeffs.append(float(self.in3.get()))
        if(self.in4.get()!=''):
            float(self.in4.get())
            coeffs.append(float(self.in4.get()))
        if(self.in5.get()!=''):
            float(self.in5.get())
            coeffs.append(float(self.in5.get()))
        if(self.in6.get()!=''):
            float(self.in6.get())
            coeffs.append(float(self.in6.get()))
        if(self.in7.get()!=''):
            float(self.in7.get())
            coeffs.append(float(self.in7.get()))
        if(self.in8.get()!=''):
            float(self.in8.get())
            coeffs.append(float(self.in8.get()))
        if(self.in9.get()!=''):
            float(self.in9.get())
            coeffs.append(float(self.in9.get()))
        if(self.in10.get()!=''):
            float(self.in10.get())
            coeffs.append(float(self.in10.get()))
        return coeffs



    def coeff_to_array_vol2(self):
        coeffs = []
        if(self.in1.get()!=''):
            float(self.in1.get())
            coeffs.append(float(self.in1.get()))
        if(self.in2.get()!=''):
            float(self.in2.get())
            coeffs.append(float(self.in2.get()))
        if(self.in3.get()!=''):
            float(self.in3.get())
            coeffs.append(float(self.in3.get()))
        if(self.in4.get()!=''):
            float(self.in4.get())
            coeffs.append(float(self.in4.get()))
        if(self.in5.get()!=''):
            float(self.in5.get())
            coeffs.append(float(self.in5.get()))
        if(self.in6.get()!=''):
            float(self.in6.get())
            coeffs.append(float(self.in6.get()))
        if(self.in7.get()!=''):
            float(self.in7.get())
            coeffs.append(float(self.in7.get()))
        if(self.in8.get()!=''):
            float(self.in8.get())
            coeffs.append(float(self.in8.get()))
        if(self.in9.get()!=''):
            float(self.in9.get())
            coeffs.append(float(self.in9.get()))
        if(self.in10.get()!=''):
            float(self.in10.get())
            coeffs.append(float(self.in10.get()))
        if(self.in11.get()!='' and self.input_type.get()=="Sine"):
            float(self.in11.get())
            coeffs.append(float(self.in11.get()))
        if(self.in12.get()!='' and self.input_type.get()=="Cosine"):
            float(self.in12.get())
            coeffs.append(float(self.in12.get()))
        if(self.in13.get()!='' and self.input_type.get()=="Exponential"):
            float(self.in13.get())
            coeffs.append(float(self.in13.get()))
        if(self.in14.get()!='' and self.input_type.get()=="Polynomial"):
            float(self.in14.get())
            coeffs.append(float(self.in14.get()))
        if(self.in15.get()!='' and self.input_type.get()=="Polynomial"):
            float(self.in15.get())
            coeffs.append(float(self.in15.get()))
        if(self.in16.get()!='' and self.input_type.get()=="Polynomial"):
            float(self.in16.get())
            coeffs.append(float(self.in16.get()))
        if(self.in17.get()!='' and self.input_type.get()=="Polynomial"):
            float(self.in17.get())
            coeffs.append(float(self.in17.get()))
        return coeffs



    def state_space_representaion (self,n,m):
        """ state derivatives matrix """
        coeffs=self.coeff_to_array()
        coeffs[:] = [x / coeffs[n] for x in coeffs]
        derivatives_state_variables = []
        for i in range(n):

            derivatives_state_variables.append( "X'")
            derivatives_state_variables[i] = derivatives_state_variables[i] + str(i+1)

        """ matrix A """

        coeff_array = np.reshape(np.zeros(n*n),(n,n))
        k = 0

        for i in range(n):
            for j in range (n):
                if j == n-1:
                    coeff_array[i,j] = (-1) * coeffs[k]
                    k -= 1
                    if k == n-1 :
                        break
        for i in range(n):
            for j in range(n):
                if i-j == 1 :
                    coeff_array[i,j] = 1
    
        """ state variables matrix """  
        state_variables = []
        for i in range(n):
            state_variables.append( "X")
            state_variables[i] = state_variables[i] + str(i+1)

        """ C matrix """
        c = []
        c = np.reshape(np.zeros(1*n),(1,n))
        c[(0,n-1)] = 1
     
        """ B matrix """
        k = np.reshape(np.zeros(n*1),(n,1))
        a = coeffs[0:n+1]
        b = coeffs [n+1:]
        x = 0

        for i in range (len(a)-len(b)):
            b.append(0)

        for i in range(n) :
            k[i] = b[x] - a[x]*b[m]
            x+=1

        """ D matrix"""
        d = b[m]

        return  {'A':coeff_array , 'B':k , 'C':c , 'D':d ,
        'Derivatives_of_sates':np.reshape(derivatives_state_variables,(n,1)) ,
        'states':np.reshape(state_variables,(n,1))}
        

#Function for checking the Comboboxes m and n


    def check(self,event):
        #if(not self.m.get().isdigit()):
            #messagebox.showerror('Error','m must be a number')
            #self.m.set(0)
        #if(not self.n.get().isdigit()):
            #messagebox.showerror('Error','n must be a number')
            #self.n.set(1)
        #if(self.m.get()>'4'):
            #messagebox.showerror('Error','m is out of range')
            #self.m.set(0)
        #if(self.n.get()>'4'):
            #messagebox.showerror('Error','n is out of range')
            #self.n.set(1)
        if(self.m.get()>self.n.get()):
            messagebox.showerror('Error','m must be a number less than or equal n')
            self.m.set(0)

#Function for checking coefficients of a


    def coeff_of_a(self,event):
        if(self.n.get()>='1'):
            self.a1.config(state='normal')
        else:
            self.a1.delete(0,last='end')
            self.a1.config(state='readonly')
        if(self.n.get()>='2'):
            self.a2.config(state='normal')
        else:
            self.a2.delete(0,last='end')
            self.a2.config(state='readonly')
        if(self.n.get()>='3'):
            self.a3.config(state='normal')
        else:
            self.a3.delete(0,last='end')
            self.a3.config(state='readonly')
        if(self.n.get()>='4'):
            self.a4.config(state='normal')
        else:
            self.a4.delete(0,last='end')
            self.a4.config(state='readonly')

#Function for checking coefficients of b

    def coeff_of_b(self,event):
        if(self.m.get()>='1'):
            self.b1.config(state='normal')
        else:
            self.b1.delete(0,last='end')
            self.b1.config(state='readonly')
        if(self.m.get()>='2'):
            self.b2.config(state='normal')
        else:
            self.b2.delete(0,last='end')
            self.b2.config(state='readonly')
        if(self.m.get()>='3'):
            self.b3.config(state='normal')
        else:
            self.b3.delete(0,last='end')
            self.b3.config(state='readonly')
        if(self.m.get()>='4'):
            self.b4.config(state='normal')
        else:
            self.b4.delete(0,last='end')
            self.b4.config(state='readonly')

#Combining Function for bind function

    def combine(self,event):
        self.coeff_of_a(event)
        self.coeff_of_b(event)
        self.opening_new_entry(event)
        self.changing_options(event)
        self.disable_combobox(event)


#Function for checking entry input

    def testVal(self,inStr,acttyp):
        if(acttyp=='1'):
            try:
                if (inStr=='-' or isinstance(float(inStr), float)):
                    1
            except:
                return False
        return True
    
    
    
    def __init__(self, parent):
        
        
        tkinter.Frame.__init__(self, parent)
        
        
        
        self.parent = parent

        self.in1=StringVar()
        self.in2=StringVar()
        self.in3=StringVar()
        self.in4=StringVar()
        self.in5=StringVar()
        self.in6=StringVar()
        self.in7=StringVar()
        self.in8=StringVar()
        self.in9=StringVar()
        self.in10=StringVar()
        self.in11=StringVar()
        self.in12=StringVar()
        self.in13=StringVar()
        self.in14=StringVar()
        self.in15=StringVar()
        self.in16=StringVar()
        self.in17=StringVar()

        self.label_sine=tkinter.Label(self.parent, text = "The value of \u03C9 in sin(\u03C9t)", font=("Cambria", 16))
        self.entry_sine=tkinter.Entry(self.parent, textvariable=self.in11, validate="key")
        self.entry_sine['validatecommand'] = (self.entry_sine.register(self.test_val),'%P','%d')
        self.label_cosine=tkinter.Label(self.parent, text = "The value of \u03C9 in cos(\u03C9t)", font=("Cambria", 16))
        self.entry_cosine=tkinter.Entry(self.parent, textvariable=self.in12, validate="key")
        self.entry_cosine['validatecommand'] = (self.entry_cosine.register(self.test_val),'%P','%d')
        self.label_exp=tkinter.Label(self.parent, text = "The value of a in e\u1d43\u1d57", font=("Times", 16))
        self.entry_exp=tkinter.Entry(self.parent, textvariable=self.in13, validate="key")
        self.entry_exp['validatecommand'] = (self.entry_exp.register(self.testVal),'%P','%d')
        self.label_poly=tkinter.Label(self.parent, text = "The polynomial function", font=("Times", 16))
        self.entry_t3=tkinter.Entry(self.parent, textvariable=self.in14, validate="key", width=4)
        self.entry_t3['validatecommand'] = (self.entry_t3.register(self.testVal),'%P','%d')
        self.label_t3=tkinter.Label(self.parent, text = "t\u00B3+", font=("Times", 14))
        self.entry_t2=tkinter.Entry(self.parent, textvariable=self.in15, validate="key", width=4)
        self.entry_t2['validatecommand'] = (self.entry_t2.register(self.testVal),'%P','%d')
        self.label_t2=tkinter.Label(self.parent, text = "t\u00B2+", font=("Times", 14))
        self.entry_t1=tkinter.Entry(self.parent, textvariable=self.in16, validate="key", width=4)
        self.entry_t1['validatecommand'] = (self.entry_t1.register(self.testVal),'%P','%d')
        self.label_t1=tkinter.Label(self.parent, text = "t+", font=("Times", 14))
        self.entry_t0=tkinter.Entry(self.parent, textvariable=self.in17, validate="key", width=4)
        self.entry_t0['validatecommand'] = (self.entry_t0.register(self.testVal),'%P','%d')

#titles and equations

        self.l1 = tkinter.Label(self.parent, text = "Group 48 System Simulator", font=("Times New Roman Bold", 30)).grid(column=3, row=0)
        self.load = Image.open(r"F:\Personal\college\2nd elec\2nd term\System Dynamics\picture.gif")
        self.img = ImageTk.PhotoImage(self.load)
        self.l2 = tkinter.Label(self.parent,image = self.img).grid(pady=10, column=3, row=1)

#n Combobox

        self.l3 = tkinter.Label(self.parent, text = "n=", font=("Times New Roman", 16)).grid(padx=(6,0), column=0, row=3)
        self.n= ttk.Combobox(self.parent, values=[0,1,2,3,4], state='readonly')
        self.n.grid(column=1, row=3)
        self.n.current(0)

#m Combobox

        self.l4 = tkinter.Label(self.parent, text = "m=", font=("Times New Roman", 16)).grid(column=4, row=3)
        self.m= ttk.Combobox(self.parent, values=[0,1,2,3,4], state='readonly')
        self.m.grid(column=5, row=3)
        self.m.current(0)

#bind fuction waiting for those events (check Function which checks m's and n's  comboboxes)

        self.parent.bind('<ButtonRelease-1>', self.check) and self.parent.bind('<Return>', self.check)

#a0 label

        self.l5 = tkinter.Label(self.parent, text = "a\u2092=", font=("Times New Roman", 16)).grid(padx=(3,0), column=0, row=4)
#a0 entry with calling validation function

        self.a0=Entry(self.parent, textvariable=self.in1, width=23, validate="key")
        self.a0['validatecommand'] = (self.a0.register(self.testVal),'%P','%d')
        self.a0.grid(column=1, row=4)

#a1 label

        self.l6= tkinter.Label(self.parent, text = "a\u2081=", font=("Times New Roman", 16), ).grid(padx=(3,0), column=0, row=5)
#a1 entry with calling validation function

        self.a1=Entry(self.parent, textvariable=self.in2, width=23, validate="key")
        self.a1['validatecommand'] = (self.a1.register(self.testVal),'%P','%d')
        self.a1.grid(column=1, row=5)

#a2 label

        self.l7= tkinter.Label(self.parent, text = "a\u2082=", font=("Times New Roman", 16)).grid(padx=(3,0), column=0, row=6)
#a2 entry with calling validation function

        self.a2=Entry(self.parent, textvariable=self.in3, width=23, validate="key", state="readonly")
        self.a2['validatecommand'] = (self.a2.register(self.testVal),'%P','%d')
        self.a2.grid(column=1, row=6)

#a3 label

        self.l8= tkinter.Label(self.parent, text = "a\u2083=", font=("Times New Roman", 16)).grid(padx=(3,0), column=0, row=7)
#a3 entry with calling validation function

        self.a3=Entry(self.parent, textvariable=self.in4, width=23, validate="key", state="readonly")
        self.a3['validatecommand'] = (self.a3.register(self.testVal),'%P','%d')
        self.a3.grid(column=1, row=7)
#a4 label

        self.l9 = tkinter.Label(self.parent, text = "a\u2084=", font=("Times New Roman", 16)).grid(padx=(3,0), column=0, row=8)
#a4 entry with calling validation function

        self.a4=Entry(self.parent, textvariable=self.in5, width=23, validate="key", state="readonly")
        self.a4['validatecommand'] = (self.a4.register(self.testVal),'%P','%d')
        self.a4.grid(column=1, row=8)
#b0 label

        self.l10 = tkinter.Label(self.parent, text = "b\u2092=", font=("Times New Roman", 16)).grid(column=4, row=4)
#b0 entry with calling validation function

        self.b0=Entry(self.parent, textvariable=self.in6, width=23, validate="key")
        self.b0['validatecommand'] = (self.b0.register(self.testVal),'%P','%d')
        self.b0.grid(column=5, row=4)

#b1 label

        self.l11= tkinter.Label(self.parent, text = "b\u2081=", font=("Times New Roman", 16)).grid(column=4, row=5)
#b1 entry with calling validation function

        self.b1=Entry(self.parent, textvariable=self.in7, width=23, validate="key")
        self.b1['validatecommand'] = (self.b1.register(self.testVal),'%P','%d')
        self.b1.grid(column=5, row=5)

#b2 label

        self.l12= tkinter.Label(self.parent, text = "b\u2082=", font=("Times New Roman", 16)).grid(column=4, row=6)
#b2 entry with calling validation function

        self.b2=Entry(self.parent, textvariable=self.in8, width=23, validate="key", state="readonly")
        self.b2['validatecommand'] = (self.b2.register(self.testVal),'%P','%d')
        self.b2.grid(column=5, row=6)

#b3 label

        self.l13= tkinter.Label(self.parent, text = "b\u2083=", font=("Times New Roman", 16)).grid(column=4, row=7)
#b3 entry with calling validation function

        self.b3=Entry(self.parent, textvariable=self.in9, width=23, validate="key", state="readonly")
        self.b3['validatecommand'] = (self.b3.register(self.testVal),'%P','%d')
        self.b3.grid(column=5, row=7)
#b4 label

        self.l14= tkinter.Label(self.parent, text = "b\u2084=", font=("Times New Roman", 16)).grid(column=4, row=8)
#b4 entry with calling validation function

        self.b4=Entry(self.parent, textvariable=self.in10, width=23, validate="key", state="readonly")
        self.b4['validatecommand'] = (self.b4.register(self.testVal),'%P','%d')
        self.b4.grid(column=5, row=8)
#bind fuction waiting for those events (combine Function which checks a's and b's  coefficients)

        self.parent.bind('<Motion>', self.combine) and self.parent.bind('<FocusOut>', self.combine)

#Type input label

        self.l15 = tkinter.Label(self.parent, text = "Input Type", font=("Times New Roman", 16))
        self.l15.grid(pady=(20,0), column=3, row=9)
#Type input Combobox  

        self.input_type= ttk.Combobox(self.parent, values=["Impulse", "Step","Sine", "Cosine", "Exponential", "Polynomial"], width=11, state='readonly')
        self.input_type.grid(column=3, row=10)
        self.input_type.current(0)
#Simulation time label

        self.l16 = tkinter.Label(self.parent, text = "Simulation time", font=("Times New Roman", 16)).grid(pady=(20,0), column=3, row=11)
#Simulation time Scale

        self.time_meter = tkinter.Scale(self.parent, from_=1, to=30, orient="horizontal")
        self.time_meter.grid(column=3, row=12)
#Plotting input button


        self.bt1=Button(self.parent, text="Plotting Input", font=("Times New Roman", 16), bg="lightblue", command=self.getting_parameters1).grid(pady=20, column=0, columnspan=2, row=13)  #add command attribute with the function after font as: , command=fuction()
#Plotting output button

        self.bt2=Button(self.parent, text="Plotting Output", font=("Times New Roman", 16), bg="lightblue", command=self.getting_parameters).grid(pady=20, column=4, columnspan=2, row=13)  #add command attribute with the function after font as: , command=fuction()
#State-Space Representention button

        self.bt3=Button(self.parent, text="State-Space Represtentaion", font=("Times New Roman", 16), bg="lightblue", command=self.createNewWindow3).grid(column=3, row=14)  #add command attribute with the function after font as: , command=fuction()
#Visualizing System States button

        self.bt4=Button(self.parent, text="Visualizing System States", font=("Times New Roman", 16), bg="lightblue", command=self.getting_parameters2).grid(pady=20, column=3, row=15)  #add command attribute with the function after font as: , command=fuction()


        
def main():
    window = tkinter.Tk()
    window.title("SystemsGUI")
    window.geometry('845x700')
    window.resizable(0,0)
    Sys(window).place(relx=1, rely=1)
    window.mainloop()

if __name__ == "__main__":
    main()