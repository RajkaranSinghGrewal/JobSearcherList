import json
import os

class Jobs:
    company_name = ""
    job_role = ""
    job_description = []
    job_location = ""
    date = ""
    job_link = ""
    status = ""
    json_object = {}
    def __init__(self,company_name = "",job_role = "",job_description = [],job_location = "",date = "",job_link = "",status = ""):
        self.company_name = company_name
        self.job_role = job_role
        self.job_description = job_description
        self.job_location = job_location
        self.date = date
        self.job_link = job_link
        self.status = status
        self.json_object = {}
    def create_json_object(self):
        for key in [attr for attr in dir(Jobs) if not callable(getattr(Jobs,attr)) and not attr.startswith("__")]:
            if key != "json_object":
                self.json_object.update({key:self.get_values(key)})
    def get_values(self,field_name):
        var = vars(self)
        return var[field_name]
    def set_company_name(self,company_name):
        self.company_name = company_name
    def set_job_role(self,job_role):
        self.job_role = job_role
    def set_job_location(self,job_location):
        self.job_location = job_location
    def set_job_description(self,job_description):
        self.job_description = job_description
    def set_date(self,date):
        self.date = date
    def set_job_link(self,job_link):
        self.job_link = job_link
    def set_status(self,status):
        self.status = status
def loadDatabase(filename):
    json_file = {}
    try:
        with open(filename,'r+') as database_file:
            text = database_file.read()
            json_file = json.loads(text)
        print("File has been loaded correctly")
    except Exception as e:
        print("File has not been loaded correctly")
        print("Generating Empty json objects")
        json_file = json.loads('{}')
    return json_file
def saveDatabase(filename,json_file):
    try:
        with open(filename,'w+') as database_file:
            database_file.write(json.dumps(json_file,indent=3,sort_keys=True))
        print("File has been saved")
    except Exception as e:
        print("File has not been saved correctly due to ")
        print(e)
if __name__ == "__main__":
    list_of_jobs = loadDatabase("database.json")
    #actions of the code
    job = {}
    loop_flag = True
    index = str(len(list_of_jobs))
    while(loop_flag):
        try:
            print("""What would you like to do Type:\n
                Create_Empty to empty the current job Object\n
                Read display all the variables in job\n
                Append to the database\n
                List all the object in database\n
                Select the object in database\n
                Save the entire database\n
                Set Value for object\n
                Reset the entire database\n
                Exit\n
                """)
            choice = input()
            if choice == "Create_Empty":
                index = str(len(list_of_jobs))
                job = Jobs()
                print("current_job is empty")
            elif choice == "Reset":
                list_of_jobs = loadDatabase("database.json")
            elif choice == "Read":
                job.create_json_object()
                print(job.json_object)
            elif choice == "Append":
                list_of_jobs[format(index,'09d')] = job.json_object
            elif choice == "List":
                print(json.dumps(list_of_jobs,indent=3,sort_keys=True))
            elif choice == "Select":
                index = input("Please select the index number")
                job_json = list_of_jobs[index]
                job = Jobs(company_name = job_json["company_name"],
                       job_role = job_json["job_role"],
                       job_description = job_json["job_description"],
                       job_location = job_json["job_location"],
                       date = job_json["date"],
                       job_link = job_json["job_link"],
                       status = job_json["status"]
                       )
            elif choice == "Set":
                loop_set_flag = True
                while loop_set_flag:
                    job_variable = input("""
                    Which Value would you like to set: company_name, job_role, job_description, job_location, date, job_link, status or exit:\n""")
                    if job_variable == "company_name":
                        job.set_company_name(input("Please Enter Company Name: "))
                    elif job_variable == "job_role":
                        job.set_job_role(input("Please Enter Job role: "))
                    elif job_variable == "job_description":
                        job_description = input("Please Enter Job Description: (Use triple qoutes for multiline input)\n")
                        job_description = job_description.split('\n')
                        job_description = [line for line in job_description if line]
                        job.set_job_description(job_description)
                    elif job_variable == "job_location":
                        job.set_job_location(input("Please Enter Job Location: "))
                    elif job_variable == "date":
                        job.set_date(input("Please Enter Job date: "))
                    elif job_variable == "job_link":
                        job.set_job_link(input("Please Enter Job Link: "))
                    elif job_variable == "status":
                        job.set_status(input("Please Enter Job status: "))
                    elif job_variable == "exit":
                        job.create_json_object()
                        loop_set_flag = False
            elif choice == "Save":
                saveDatabase("database.json",list_of_jobs)
            elif choice == "Exit":
                loop_flag = False
        except Exception as e:
            print(f"{e} as been reached")
