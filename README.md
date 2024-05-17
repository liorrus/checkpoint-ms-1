"# checkpoint-ms-1" 

This repo is part of checkpoint assigment 
building and runing container: 
git clone 
cd
docker build -t <name> .
docker run -p 5000:5000 <name>

runing direct with python:
pip install -r requirements.txt
py main.py 

testing:
make sure localstack is runing and checkpoint-terraform was apllied
>>> my_dict={"token":"notsecured","data":{"email_subject":"subject1","email_sender":"sender1","email_content":"content","email_timestream":"123"}}
>>> res=requests.post(url="http://localhost:5000/api/add_message", json=my_dict)
check res http status if it is 200 all good 



