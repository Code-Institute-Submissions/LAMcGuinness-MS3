# Milestone 3 - 

## About

This is a website is a platfrom for sharing recipes that are healthy and will be ready fast. Real food really fast. Its main purpose is recipe sharing among users. Users can register an account, add recipes and search through existing recipes. Fast Food is an educational project used for the purpose of my Milestone 3/Data Centric Module project for the Code Institute.

A live version of the website can be found .... along with its repository ....

## UX Design 

The aim of FastFood was to create an online cookbook of fast and healthy recipes. User will be able to make real healthy food really fast, recipes should all be 30 minutes or less start to finish! Users will be able to find and share recipes with each other. 

### Business Scope


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

Used [Abode Color](https://color.adobe.com/explore) to get an idea of a color scheme for site. Type in 'healthy food' and went with a red/green/orange there. Colors associated with fruits and vegetables/healthy foods.

### Wireframes

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
* Add Recipe
    -
* Recipe section
    - Users can see recipes clearly broken into sections:
        1. Name /type of meal
        2. Ingredients for meal
        3. Method for meal
        4. Who the creator of the recipe is
* Footer
    - It also contains links to their social media accounts along with company name, moto and copyright.
  
## Future Release Updates


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

## Testing
### Issues Encountered
- Problem: Jinga errors when testing if register.html page was working 
    - Fix: Human error {% end block %} was entered instead of {% endblock %}

- Problem: NameError: name 'session' is not defined
    - Fix: Human error spelling mistake

- Problem: NameError: name 'flash' is not defined
    - Fix: Forgot to import 'flash' from 'flask'
### Testing User Stories

#### First time user
#### Returning User

### Testing Functionality
### Errors encountered

#### Checked for broken links
#### Tested browser back/forward actions
#### Tested form validation

### Testing Compatibility

#### Responsiveness
#### Devices Test
#### Browser Test

### Testing Performance & Accessibility
[Lighthouse](https://developers.google.com/web/tools/lighthouse)
[a11y color contrast](https://color.a11y.com/Contrast/)

### Code validation
#### HTML
[W3C Validator](https://validator.w3.org/)
#### CSS
[W3C CSS](https://validator.w3.org/)
#### JavaScript
#### Python

## Deployment
### GitHub Pages
### Forking the GitHub repository
### Heroku

## Credits
### Code
[Materialize](https://materializecss.com/about.html) 
* Materialize templeates used throughout project

[Code Institute](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+DCP101+2017_T3/courseware/9e2f12f5584e48acb3c29e9b0d7cc4fe/6449dcd23ca14016aa83dc7313d91a02/?child=first)
* Code used from this video to provide the proper form validation on the category selection of the 'add_recipe.html' pagef

### Recipes
[BBC Good Food](https://www.bbcgoodfood.com/)
* Recipes taken and edited from here
[The Body Coach](https://www.thebodycoach.com/blog/tags/recipes)
* Recipes taken and edited from here


### Acknowledgements
