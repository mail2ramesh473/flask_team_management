## Team Management Application

##### Create virtual environment using below command
`virtualenv tm_venv`
    

##### Activate virtual environment
`source tm_venv/bin/activate`


##### Install requirements using below command
`pip install -r requirements.txt`


##### Install mysql (follow the steps mentioned in below url)
https://linode.com/docs/databases/mysql/install-mysql-on-ubuntu-14-04/

`Note: If you don't want to change configurations of mysql use "root" as user and passowrd as "mysql", else change the configurations(DATABASES) in team_management/settings.py file`
            

##### Create DB and Tables using below command
  - open Terminal using below command
        `ctl+alt+T`
  - login to mysql db console using below command
        `mysql -uroot -pmysql`
  - create database 'teams' using below command
        `create database teams;`
  - create table 'members' using below command
       `CREATE TABLE members (
          userId int(11) NOT NULL AUTO_INCREMENT,
          firstName varchar(50) NOT NULL,
          lastName varchar(50),
          phone varchar(20),
          emailId varchar(20),
          role varchar(20),
          PRIMARY KEY (userId)
        ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1
        `

##### Run Either of below command to run the application
`twistd -n web --port 8000 --wsgi hclprod.app`

`python run_app.py`


##### Use Below Commands to do the transactions
  - To Add Member
  `curl -XPOST -H"Content-Type:application/json" http://localhost:8000/teams/add -d'{"userId": 1, "firstName": "Ramesh", "lastName": "Kumar", "emailId": "ramesh@mail.com", "role": 0}'`
  
  - To update member
  `curl -XPOST -H"Content-Type:application/json" http://localhost:8000/teams/update -d'{"userId": 1, "firstName": "Ramesh", "lastName": "C"}'`
  `curl -XPUT -H"Content-Type:application/json" http://localhost:8000/teams/update -d'{"userId": 1, "firstName": "Ramesh", "lastName": "C"}'`
  
  - To delete member
  `curl -XDELETE -H"Content-Type:application/json" http://localhost:8000/teams/delete -d'{"userId": 1}'`
