# coffee-store

#### to run the project you will need 

* mongo server locally on your machine 
* pipenv installed 
* install the requirements from Pipfile and Pipfile.lock

#### to populate the database quickly => there is a file called *setup.py* just run it.

#### for urls and paths

for coffee machines list
> localhost:8000/cm/?param1=val&param2=val...
##### available parameters :
  * *type_* : LRG, SML, ESP
  * *wl* : yes, no


for coffee pods list
> localhost:8000/cp/?param1=val&param2=val...
##### available parameters :
  * *type_* : LRG, SML, ESP
  * *flavor* : VAN, CAR, PSL, MOC, HAZ
  * *size* : 1, 2, 3, ...


also there is paths for details using ids but not tested yet
