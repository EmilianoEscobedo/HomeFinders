# HomeFinders - CRUD System
Do you know someone who knows about a house for rent?

A software to CRUD a DB in order to save potential finders for your next rented house.
Written in python, with sqlite DB and Tk as GUI.
<br><br>
Usually in Argentina, my country of residence, the houses rented by individuals are cheaper and have better conditions than those rented by real estate businesses.
<br><br>
This project was born because I was looking for a house to rent and my father told me that surely if I told 100 people that I was looking for a house, one house would appear. So I wanted to keep a little more proper record while learning about SQL and relational database foundations.

<div align="center">
  <img src="https://i.ibb.co/gvrqRxT/home.png" alt="Home Interface"/>
  <p>Home Interface</p>
</div>

## How does it work

### Creating a new DB
Click at DataBase dropdown option and select "Create". <br> 
This creates a SQLite DB in the actual folder, there will be all the records you create.

<div align="center">
  <img src="https://i.ibb.co/zXBKNhR/db.png" alt="Create DB"/>
  <p>New DB created</p>
</div>
<br>

### Creating a new Register
Let's start loading information into our database <br> 
Fill in the fields with the information of the house finder, do not put anything in ID field, it is an auto incrementing field. We will talk about that later. When you are ready, click into the create button.<br>
Tip: You can clean the fields with clean option in the same name dropdown

<div align="center">
  <img src="https://i.ibb.co/xY0Tmpp/register.png" alt="Register succsefully"/>f
  <p>Creating</p>
</div>

### Reading a Register
Read a Register of the database <br> 
To read a register from the database, put the ID number in the corresponding field and click the read button. <br>

<div align="center">
  <img src="https://i.ibb.co/mJ8KwSv/read.png" alt="Read a register"/>
  <p>Reading</p>
</div>

### Updating a Register
Update a Register of the database <br> 
To update a register from the database, after reading it, make some modifications on the fields you want and click the update button. <br>

<div align="center">
  <img src="https://i.ibb.co/Ns3Hjmj/update.png" alt="Update a register"/>
  <p>Updating</p>
</div>

### Deleting a Register
Delete a Register of the database <br> 
If you want to delete a register from the database, after reading it, click the delete button, and accept the warning pop-up.  <br>

<div align="center">
  <img src="https://i.ibb.co/3zCy5Cd/delete.png" alt="Delete a register"/>
  <p>Deleting</p>
</div>
