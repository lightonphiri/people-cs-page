# Mphephu Faresa
# CSC1011H Tutotial 1

from Person import Person
import datetime
import pickle

docs,docs_id ,pts , pts_id, appts = list() , list() , list() , list() , list()

clinic_data = [docs,docs_id ,pts , pts_id, appts] # This is the list to be picked containing all clinic information 


class Patient(Person) :
    def __init__(self,iden="Unknown",adr = "Unkown adress",vis = "unspecified visits") :
        #Person.__init__(self,name,age)
        self.idno = iden
        self.adress = adr
        self.visits = vis
        
    def fees_owed(self) :
        rate ,trade = 200 , "ZAR"       
        med_fees = rate*self.visits
        return trade +' - '+ str(med_fees) + " | {} Visits".format(self.visits)
    
    def __str__(self) :
        return str(self.pt_id) + "," + str(self.adress) +"," + str(self.visits) + "," # Fees owed missing boss

class Doctor(Person) :
    def __init__(self,iden="Unknown",adr = "Unkown adress" ) :
        self.idno = iden
        self.adress = adr
    def __str__() :  
        return str(self.doc_id) + "," + str(self.adress) 
    

        
def add_appointment(self,pts,docs)   :   
    memo = input("Describe how the appointment was /n > ".format())
    def __str__(self) :
        return str(pt_id) +","+ str(doc_id) +"," + memo 
    
def clinic_menu() :
    print("{0:_^50}\n\n{1:-^50}\n{2:-^50}\n{3:-^50}\n{4:~^50}\n{5:~^50}\n{6:~^50}\n{7:_^50}\n{8:_^50}\n".format(("Welcome To Clinic"),('Press 1 To Add Patient'),('Press 2 To Add Doctor'),("Press 3 To Appointment"),("Press 4 To Display Patients"),("Press 5 To Display Dcotors"),("Press 6 To Display Appontments"),("0 - Quit"),("111-Restart")))
    
def input_human(kind) : # Kind refers to whether Patient or Doctor 
    human_name = input("Input {} Name __> ".format(kind))
    name = human_name[:] #Creates a copy to set the name Person.name
    if kind == "Patient" : 
        human_name = Patient()
        human_name.visits = int(input("Enter the number of Visits    NB : Numbers Only\n__> "))
    
    if kind ==  "Doctor" : human_name = Doctor()
    
    human_name.name = name 
    human_name.age = input("Enter The {} Age __> ".format(kind))
    human_name.idno = input("Enter the {} Identity Number __> ".format(kind))
    human_name.adress = input("Enter The {} Adress : \n ".format(kind))
       
    if kind == "Patient" : 
        clinic_data[2].append(human_name) # Appned the class object to the datastructure
        clinic_data[3].append(human_name.idno)
    elif kind == "Doctor" : 
        clinic_data[0].append(human_name)
        clinic_data[1].append(human_name.idno)
        
def display_option(list_name):
    
    for name in list_name :
        print(name.name)
    
def display_appointments(app_list) :
    for n in app_list :
        print(n)

def main() : 
    
    while True :   
        try : 
            while True :
                clinic_menu()
                option = int(input("Enter Option __> "))
                if option == 0 :
                    pickle_file = open("Pickle.txt","wb")
                    pickle.dump(clinic_data,pickle_file)
                    pickle_file.close()
                    break
                elif option == 1 : input_human("Patient")
                elif option == 2 : input_human("Doctor")
                elif option == 3 :
                    
                    pt_input = input("Enter The Patient ID To add An Appointment \n__> ")
                    if pt_input in clinic_data[3] :
                        pt_id = pt_input           
                    else :
                        print("No patient of that ID was found")
                            
                    doc_input = input("Enter the Doctor ID you want to add \n__>")
                    if doc_input in  clinic_data[1] :
                        doc_id = doc_input
                    else :
                        print("Doc id not found")
                             
                    date = input("Enter the date and time of appointment \n  [YEAR/MONTH/DATE ] : ")
                    time = input("Enter the Time of appointment (24hours) \n[HH:MM] : ")
                        
                    time_stamp = date+" "+time   
                    
                    clinic_data[4].append("\n{:_^50}\n\nPatient {} and Doctor {} \n{}\n{}\n".format(("Appointment Reciept between"),(pt_id),(doc_id),("@"),(time_stamp)))
                                 
                   
                    
                elif option == 4 :
                    saved_data = list()
                    inFile = open("Pickle.txt","rb")
                    saved_data = pickle.load(inFile)   
                    # inFile.close()    
                    display_option(saved_data[2])
                elif option == 5 :
                    saved_data = list()
                    inFile = open("Pickle.txt","rb")
                    saved_data = pickle.load(inFile)   
                    # inFile.close()                                        
                    display_option(saved_data[0])
                elif option == 6 : 
                    saved_data = list()
                    inFile = open("Pickle.txt","rb")
                    saved_data = pickle.load(inFile)                                          
                    display_appointments(saved_data[4])
                    
                elif option == 7 : pass
                
        except : 
            print("Something Went Wrong , Please Try Again")
            continue 
                  
        else : break 
main()