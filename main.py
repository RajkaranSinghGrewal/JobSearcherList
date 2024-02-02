import json


class Jobs:
    company_name = ""
    job_role = ""
    job_description = ""
    date = ""
    job_link = ""
    status = ""
    json_object = {}
    def __init__(self,company_name = "",job_role = "",job_description = "",job_location = "",date = "",job_link = "",status = ""):
        self.company_name = company_name
        self.job_role = job_role
        self.job_description = job_description
        self.date = date
        self.job_link = job_link
        self.status = status
        self.json_object = {}
    def create_json_object(self):
        for key in [attr for attr in dir(Jobs) if not callable(getattr(Jobs,attr)) and not attr.startswith("__")]:
            if key != "json_object":
                self.json_object.update({key:self.get_values(key)})
            #print(key + " : " + self.get_values(key) )
    def save(self,filename):
        with open(filename) as my_file:
            my_file.write(json.dumps(self.json_object,indent=3,sort_keys=True))
        print("File has been saved")
    def get_values(self,field_name):
        var = vars(self)
        return var[field_name]
job = Jobs(company_name="hello_world")
job.create_json_object()
print(job.get_values("company_name"))
print(job.json_object)
