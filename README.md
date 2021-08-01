# Milestone 3 - 

## About

This is a website is a platfrom for sharing recipes that are healthy and will be ready fast. Real food really fast. Its main purpose is recipe sharing among users. Users can register an account, add recipes and search through existing recipes. Fast Food is an educational project used for the purpose of my Milestone 3/Data Centric Module project for the Code Institute.
![picture of site](/static/img/amIResponsive.png)

A live version of the website can be found [site](https://flask-milestone-three-lamcg.herokuapp.com/) along with its repository [repository](https://github.com/LAMcGuinness/MS3)

## UX Design 

The aim of FastFood was to create an online cookbook of fast and healthy recipes. User will be able to make real healthy food really fast, recipes should all be 30 minutes or less start to finish! Users will be able to find and share recipes with each other. 

### Business Scope
As the site owner I want to;
    - a functioning website with no broken links
    - create a fun and easy to naviate recipe sharing app
    - be able to create, read, update and delete recipes
    - if it is easy to use with no issue should increase traffic
    - in the future link up with cookware and food brands link sale to there products from recipes
    - securely log in and out of site no compromise of passwords

### User Stories

1. As as user I want to;
    * Navigate through with ease and find all information presented clearly and consciously.
    * Search for recipes 
    * Easily register an account
    * Share my own recipes

2. As a returning user I want to;
    * Find the log in to my account area
    * Share recipes with other users
    * Edit and delete my own recipes
    * Navigate throughout with ease

3. As the owner/adiminitrator I want to;
    * Add new categories
    * Edit and delete recipes
    * Display results that are visually appealing and user friendly

### Design
#### Color
Used [Abode Color](https://color.adobe.com/explore) to get an idea of a color scheme for site. Type in 'healthy food' and went with a red/green/orange there. Colors associated with fruits and vegetables/healthy foods. 
Colors used in this project were;
    - #1B5E20 Green
    - #FBC02D Yellow
    - #FF6F00 Amber
    - #FF3D00 Oranage

#### Font
Font was imported from [GoogleFonts](https://fonts.google.com/). I choose the Montserrat font as it was a clean clear and easy to read font.

### Wireframes

wireframes were created using balsamic and can be found here [balsamiq](https://balsamiq.cloud/sugq8ue/p64h7n6/rC1D1)

## Features
* Navigation Bar & Side Nav Bar
    - Users can navigate throughout the website easily with the aid of the navigation bar. 
    - SideNav on smaller screens shows navigation links in drop down menu.
* Create Account
    - New users can create account to share, edit and delete their own recipes with other users.
* Log In 
    - Log In section where users are brought to their profiles and can see their recipes
* Log Out
    - Allows user to log out and removes cookies
* Recipe section
    - Users can see recipes clearly broken into sections:
        1. Name /type of meal
        2. Ingredients for meal
        3. Method for meal
        4. Who the creator of the recipe is
* Create Recipe
    - Recipes can be added by registered users
* Read Recipes
    - All visitors to the site can read recipes
* Update Recipe
    - Registered Users can Update recipes they have submitted to the site
* Delete Recipe
    - Registered users can delete recipes theyve entered on the website
* Footer
    - It also contains links to their social media accounts along with company name, moto and copyright.
  
## Future Release Updates
* Improve on design and display. Making sure all areas are uniform in padding, margins, text color etc.
* Colaborate with a cooking untensil brand to promote there products and create revenue from advertising.
* 


## Technologies Used
### Languages
* HTML
* CSS
* Javascript
* Python3

### Frameworks, Libraries and Programs Used
1. [Balsamiq] wireframes created at the design stage in website devolopment

2. Flask 
    * Python web framework
    
3. Jinga
    * Template from Python/Flask

4. [Github](https://github.com)
    * Project was stored sd

5. Gitpod
    * Project code written here

6. [Heroku](https://www.heroku.com)
    * Used to deploy Milestone 3 project.

7. [MongoDB Atlas](https://account.mongodb.com/account/login)
    * Used as database for MS3

8. [Materialize](https://materializecss.com/)
    * Used to help make app responsive and style

9. [JQuery](https://jquery.com/download/)
    * Javascript library used for this project

10. [FontAwesome](https://fontawesome.com/)
    * Used font awesome icons throughout the app

11. [Workzeug](https://werkzeug.palletsprojects.com/en/2.0.x/)
    * Used for security

12. [Canva](https://www.canva.com/)
    * Used to make logo for website

13. [Responsive Viewer](https://chrome.google.com/webstore/detail/responsive-viewer/inmopeiepgfljkpkidclfgbgbmfcennb?hl=en)
    * Used to see what site with look like on various devices. Made sure was responsive on small, medium and large screens.

14. [Shutterstock](https://www.shutterstock.com/home)
    * Landing page image found here

15. [GoogleFonts](https://fonts.google.com/) 
    * Font was found here

## Testing
### Issues Encountered
- Problem: Jinga errors when testing if register.html page was working 
    - Fix: Human error {% end block %} was entered instead of {% endblock %}

- Problem: NameError: name 'session' is not defined
    - Fix: Human error spelling mistake

- Problem: NameError: name 'flash' is not defined
    - Fix: Forgot to import 'flash' from 'flask'

- werkzeug.routing.BuildError: Could not build url for endpoint 'edit_recipe'. Did you mean 'add_recipe' instead?
    - ???? Removed Edit recipe/@app.route('edit_recipe') ..... Still throwing up this error?
    - preemptively put links in href on the base template(working again)

- Problem: admin can see 'manage categories'.. Currently showing manage category to all users who log in
    - Fix: forgot to update Jinga {% if session.user|lower == "admin"|lower %} {% endif %} in side nav as well as navbar.
    Once put in only when logged in as admin manage categories appears.

### Testing User Stories
#### Testing Site Owner Stories
1. a functioning website with no broken links
    - all buttons on the page were tested manually no broken links found
2. create a fun and easy to navigate recipe sharing app
    - very easy to navigate with the nav bar at the top and on smaller devices the drop down menu
3. be able to create, read, update and delete recipes
    - CRUDs can be done with recipes on site
4. securely log in and out of site no compromise of passwords
    - log in/out and passwords store in db are done securely with the help of Werkzeug

#### First time user
1. Easy to navigate:
    - navigate is easy using the navbar and side nav 
2. Search for recipes:
    - 
3. Register an account: 
    - link for this can be found in side nav and navbar
4. Post Recipies:
    - Once the new user has created an account and is logged it can add recipies via 'add recipe' section

#### Returning User
1. Find log in area on site:
    - this can be found easily in both the navbar on top for larger screens, and sidebar dropdown for smaller mobile devices.
2. Share recipes :
    - once logged in user can share recipes in the 'add recipe' section
3. Edit and delete users own recipes:
    - can be done with ease in that section
4. Navigate with ease:
    - can be done through the navbar and side nav. also links to social media open on a separate page so do no disrupt viewing while on the site.

#### Owner/Admin
1. Add new categories
    - can be done once logged in as admin
2. Edit and delete recipes
    - can be done 
3. Have visually appealing website
    - aesthetically looks good, but there are some areas that need to be tweaked in future updates.

### Testing Functionality
### Errors encountered
- human error... made a spelling mistake in my mongodb spelt 'recipies' instead of 'recipe' in database. Carried the typo through here. 

#### Checked for broken links
- all links manually check and appear to be working fine
#### Tested browser back/forward actions
- appear to all be working fine
#### Tested form validation
-forms all working and data showing up in database. also deleting data from database when tested

### Testing Compatibility

#### Responsiveness
[Responsive Viewer](https://chrome.google.com/webstore/detail/responsive-viewer/inmopeiepgfljkpkidclfgbgbmfcennb?hl=en)
#### Devices Test
- MacBook Pro (13-inch)
- iPhone 11 Pro Max
- iPad Pro
    - Site looks fine on all these devices

#### Browser Test
- Safari
- Google Chrome
- Mozilla Firefox
    - Site appeared fine on all browsers if was viewd on

### Testing Performance & Accessibility
[Lighthouse](https://developers.google.com/web/tools/lighthouse)
[a11y color contrast](https://color.a11y.com/Contrast/)

### Code validation
#### HTML
[W3C Validator](https://validator.w3.org/)
- no issues found

#### CSS
[W3C CSS](https://validator.w3.org/)
- unused css removed

#### JavaScript
[JSHint](https://jshint.com/)
- No warning displayed when code from script.js was entered into JSHint.

#### Python

## Deployment
### Heroku
This project is deployed using Heroku. The following steps were taken to do this.
1. Database was created using MongoDB Atlas
2. Created a Flask Application in Heroku:
    - Log Into Heroku
    - Selected "Create New App"
    - Selected a name for app (flask-milestone-three-lamcg)
    - Selected region 
    - After this "Create App" 
3. In GitPod took following steps:
    - created .gitignore file
    - added eny.py and __pycache__ to the .gitignore
    - in eny.py set the following:
        - os.environ.setdefault("IP", "0.0.0.0")
        - os.environ.setdefault("PORT", "5000")
        - os.environ.setdefault("SECRET_KEY", "YOUR_SECRET_KEY")
        - os.environ.setdefault("MONGO_URI", "MongoDB link here")
        - os.environ.setdefault("MONGO_DBNAME", "DATABASE_NAME")
    - saved eny.py
    - created and opened app.py file here we:
        - import OS, Flask, but using 'pip3 install ..."
    - created Procfile
        - typed 'echo web: python app.py > Procfile' into terminal 
        - deleted empty bottom line on Profile to avoid any future issues
    - created requirements.txt 
        - done by typing 'pip3 freeze --local > requirements.txt'
4. Back on Heroku
    - Clicked on "deploy" in tab menu
    - Deployment method select "GitHub"
    - Click on the settings tab next
    - Here clicked on "Reveal config vars"
    - Entered the following information as per the eny.py
        - "IP", "0.0.0.0"
        - "PORT", "5000"
        - "SECRET_KEY", "YOUR_SECRET_KEY"
        - "MONGO_URI", "MongoDB link here"
        - "MONGO_DBNAME", "DATABASE_NAME"
    - After these are updates clicked "hide config vars"
    - Go back to deploy tab, clicked "enable automatic deployment".
    - Still in deploy tab, furthur down, clicked "deploy branch". 
    - Once complete a message appear "app was successfully deployed"
    - At the top of the page can now "open app" by clicking on said button. 

### GitHub Pages
### Forking the GitHub repository
Forking the orginal respository on GitHub account can be used to make changes to copy with out affecting the orignal repository. Use the following steps if doing this:

1. Login to GitHub and locate Milestone3- Respitory.
2. At the top of Repository just above "Settings" button there is a "Fork" button.
3. There should now be a copy of the orginal repository in our GitHub account.

## Credits
### Code
[Materialize](https://materializecss.com/about.html) 
* Materialize templeates used throughout project

[Code Institute](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+DCP101+2017_T3/courseware/9e2f12f5584e48acb3c29e9b0d7cc4fe/6449dcd23ca14016aa83dc7313d91a02/?child=first)
* Code used from this video to provide the proper form validation on the category selection of the 'add_recipe.html' pagef

[Code Institute](https://learn.codeinstitute.net/dashboard)
* Followed same pattern as miniproject/task manager for this project

### Recipes
[BBC Good Food](https://www.bbcgoodfood.com/)
* Recipes taken and edited from here
[The Body Coach](https://www.thebodycoach.com/blog/tags/recipes)
* Recipes taken and edited from here

### Acknowledgements
