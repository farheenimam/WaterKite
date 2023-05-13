# WaterKite
## Video Demo:  [video](https://youtu.be/9Evhs5bbppA)
## Description:
### WHAT IS WaterKite ?
**WaterKite** is a fictional website for tourism with my fictional WaterKite team. We provide services at the 10 top most beautiful Island around the world that includes:<br>
- Bahamas<br>
- Fiji Island<br>
- Grand Turk<br>
- Komodo Island<br>
- Lefkada island<br>
- Mahe Island<br>
- Palwan<br>
- Saint Lucia<br>
- Seychelles<br>
- Tahiti Island<br><br>
Our services include a tourist guide, five-star resorts, meals, and other activities such as boat riding, etc.<br>
The payment method is by the **$50,000** cash which we wil provide to any user who will register themselves. For the preview of the page, it is important to login in so you can view all information about the vacation point you want to choose.

### ON WHAT LANGUAGES DOES THIS WEBSITE DEPEND ?
I have done coding of the WaterKite website with the help of *python along with the web frame* *flask*, *CSS*, *SQL*, and *HTMl* languages as I am more languages more comfortable with these three languages.

### INSIDE THE PROJECT FOLDER
The **project** is the folder that includes all my code
The project folder includes the following files:<br>

#### money.db:
Money.db is the database of our website. It consists of three SQL tables: **users**, **history**, and **info**.<br>
- ##### users:
The **users** table consists of four columns one is for id which is automatically assigned to each user as it will register itself, the username column is for the name of the users, the hash column contains all the hashed password and the cash column by default will give each user **$50,000** dollars as they will register themselves.
- ##### history:
History** table consist of 8 columns: **user_id**, **island**, **ticket**, **price**, **time**, **day**, **month** and **year**. This table stores all the required data of the users that on what Island he/she decided to spend their vacation, when, at what time the purchase is made, and how many tickets they need.
- ##### info:
The **info** table consists of only two columns: **island** and **price**. This table has all the names of the Island and the cost of the package over there. As each Island has individually different prices.

#### App.py :
App.py includes all the AJAX needed for this website. First I have described all the necessary libraries,then a web frame and a folder required which are mentioned below:<br>
 - ##### Flask:
 I used flask because I have worked on my project with this web frame and the only web frame I know to use as I am a beginner.<br>
 - ##### Werkzueg.security:
  I used this library to automate the process of hashing the password and comparing the hashed password with the password the user typed in.<br>
 - ##### Helpers:
 Helpers is helpers.py written in python in which I have defined the **login_required** function, this function checks if the user is logged in or not it gives access the routes. In this, I have also defined **apology function** (inspired by the pset9:Finance).<br>
 - ##### CS50:
 I have used the CS50 library to import the SQL function to run my SQL query within the code.<br>
After declaring all these libraries I have mentioned my SQLite database file **money.db**.
The API key and the part where I set the session is with the help of pset9:Finace. After this, I have declared routes which are the following:<br>

- ##### ("/")route:
This route uses two methods **GET** and **POST**. On **GET** request this takes the user to the very first page of the website *home.html* while on the **POST** request it takes the user to the **(/login)** route.

- ##### /history:
This uses only **GET** method which made the website remember the user and renders the user to *history.html* about which in a bit. Over here I have used SQL query to select all the required data from the SQL table and tuck it in the *history.html*.

- ##### /login:
In this I made the website forget an user_id. /login also consist of **GET** and **POST** method. In **GET** method it renders the **login.html** while in the **POST** method it requests the users for their username and password. It compares the username and password from the data, here I used the *check_password_hash* which compares with the hashed passwords in the database. If the password or username or either both is incorrect so it returns an apology saying *not found*.

- ##### /logout:
This simply forgets the user_id by clearing the session and redirects the user to the ("/")route.

- ##### /register:
This route uses two methods. The **GET** method simply displays the *register.html* while the **POST** method requests the users to type their username, password, and password again for confirmation. If the user is already registered it returns an apology. It also returns an apology in cases like incomplete or wrong input.

- ##### /index:
This simply renders the *index.html* which consists of all the main portions of our website.

- ##### /book:
This route uses two methods. The **GET** method selects the cash of the user by remembering its user-id and tucking it in the HTML. This also selects all the name of the island from the **info** table, tucks the value in the HTML, and render *book.html*.<br>
While in the **POST** request as implied by the name it asks the user for the "Island" they want to go on, how many "tickets" they want, and on want date with the help of *buy.html*. It also returns an apology in case of incomplete or wrong information. Over here after purchasing it deducts the total amount from the user's cash and renders the *confirm.html*.

- ##### /pasword:
With the help of this route, users can change their passwords. The /password route also uses two methods. The **GET** method displays the *password.html*.<br>
While asking the user for their previous password, the password they want to set, and the new password again for confirmation. If the new password does not match the previous password or if the old password is incorrect or if any input is missing it will render an apology.

####  Templates:
The templates folder consists of all the HTML required for the website:
- ##### layout.html:
The **layout.html** consists of the layout of the website. First in the *head* I have mentioned the bootstrap link as this website is made using bootstrap and the viewport of the website then I have added an icon (logo) in the title. The logo is taken from Google.<br> In the body I have defined the navbar and its aesthetics along with the fluid background image of water, and at the very end I have defined the copyright claim in my footer.<br>
In layout.html I have defined the navbar button because for every HTML my website shows different buttons.
- ##### apology.html:
The **apology.html** consists of the background image and the underwater plants' image  [image](https://ychef.files.bbci.co.uk/624x351/p0bts7f3.jpg)  (taken from google) which is shown with the apology text. This was made with the help of the [memegen](https://memegen.link/).
- ##### book.html:
This HTML consists of the form which will be filled with the *POST* request. In the main, it will render a form that consists of a dropdown option, input, and submit button. This form is filled out when your a purchasing a ticket to a specific Island.<br>
In the head, it has different navbar buttons. This HTML also comes with a fluid background image.
- #####  confirm.html:
This simply renders letters from the **WaterKite** to the users who purchased, with the background image aesthetics.
- ##### history.html:
This HTML displays the total amount in the credit of the user and a table showing all the purchases made by the user, and at what time. This HTML does not display any background image because the information on the background looks messy.
- ##### home.html:
The home.html just simply displays a page and tells the user to start their journey and as the user clicks the *start* button it will take the user to the **login.html**.
- ##### login.html:
The login.html shows a form needed for login and it consists of a navbar button called *register* which takes the users to the **/register** route.
- ##### register.html:
This HTML page displays a form for data entry into the **users** table so that the user can loggin'.
- ##### index.html:
This HTML displays different navbar buttons as compared to others: *history* that leads to **/history** route, *purchase tickets* that takes the user to **/book** route, *password* that takes to **/password**, and *logout* that takes to **/logout** route and logout the users of the website.<br>
In the main, it shows all the information about each island and their prices. The users can also access the **/book** route by clicking the book button below the description of each island. This index.html does not display any background image because the information on the background looks messy.
- ##### password.html:
The password.html gives a form to the users so they can change their password and set a new one.<br>
This HTML consists of the same navbar button as of *index.html* except the **Home** button which takes the users to the **/index** route.

### STATIC FOLDER:
The static folder consists of my page **CSS** with name *styles.css* and all the images required from my page like logo, background image, islands, and resorts images.

#### WHY DOES MY WEBSITE LOOK SO BLUE AND WHY NAME THE WEBSITE WATERKITE?
The reason for **WaterKite** being so blue is because as blue is the color of the sea and the sky, it also symbolizes serenity, and calmness> The **WaterKite** is randomly chosen by me, and also represents one of the beach activity.