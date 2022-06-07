# **_Cafe Manbo - Project Portfolio 4 - Full Stack_**

Cafe Manbo is a family restaurant located in England, Wakefield. Guests are able to visit restaurant after they have placed a booking via the website. The website itself has been designed with a "real world application" in mind, therefore the website has been designed in two parts. First, users will see a visually appealing front-end website which shows users information about the restaurant, allows users to create an account, make a booking, write a review, contact the restaurant and more. The other half of the website acts as a management system for staff members that work at Cafe Manbo. If an account has the correct permissions, the staff member will be able to see a staff dashboard which will allow them to manage everything related to Cafe Manbo such as bookings, reviews, payments and also see informative statistical data about the restaurant.

You can view the live site here - <a href="https://cafe-manbo.herokuapp.com/" target="_blank" rel="noopener">Cafe Manbo</a>

![Cafe Manbo responsive design](static/images/readme-images/responsive-design-preview-image.png)

# Contents

* [**Objective**](<#objective>)
* [**User Experience UX**](<#user-experience-ux>)
    * [User Stories](<#user-stories>)
    * [Design Prototype](<#design-prototype>)
    * [Site Structure](<#site-structure>)
    * [Design Choices](<#design-choices>)
    *  [Typography](<#typography>)
    *  [Colour Scheme](<#colour-scheme>)
    * [Project Management](<#project-management>)
* [**Features**](<#features>)
    * [Feature 1](<#feature-1>)
    * [Feature 2](<#feature-2>)
* [**Future Features**](<#future-features>)
    * [Future Feature 1](<#future-feature-1>)
    * [Future Feature 2](<#future-feature-2>)
* [**Technologies Used**](<#technologies-used>)
* [**Python Packages**](<#python-packages>)
* [**Testing**](<#testing>)
* [**Deployment To Heroku**](<#deployment-to-heroku>)
* [**Credits**](<#credits>)
    * [**Content**](<#content>)
    * [**Media**](<#media>)
*  [**Acknowledgments**](<#acknowledgements>)
*  [**Personal Development**](<#personal-development>)


# Objective

For my fourth project, I intend to create an authentic, practical and useful restaurant website which could potentially be used in a real world environment. The main objective is to demonstrate a strong level of competency in HTML, CSS, JavaScript, Python and the Django Framework alongside showcasing high attention to detail and the importance of robust testing throughout.

[Back to top](<#contents>)

# User Experience (UX)

## User Stories

### Site User

* As a Site User I can book online to come visit the restaurant
* As a Site User I can view all my bookings in one place
* As a Site User I can amend and cancel my booking
* As a Site User I can create a review about my visit to Cafe Manbo
* As a Site User I can view the menu
* As a Site User I can view images relating to Cafe Manbo
* As a Site User I can see reviews from other guests

### Site Staff Member

* As a Site Staff Member I can approve, deny and amend bookings
* As a Site Staff Member I can approve and deny submitted reviews
* As a Site Staff Member I can check guests in or not check guests
* As a Site Staff Member I can submit payment information about a completed booking
* As a Site Staff Member I can view a Staff Dashboard to view statistical data about Cafe Manbo


## Design Prototype

The very first design prototype was created using [Balsamiq](https://balsamiq.com/). Descriptive text<br /><br />


![Balsamiq Start Prototype]()


[Back to top](<#contents>)

## Site Structure

As mentioned above, the website for Cafe Manbo has been designed to be a fully encompassing website that acts as a central hub for both users and staff members.

* Main Website
    * Home, Our Menu, Gallery, Book Now, My Reservations and Write A Review.
    * Visually appealing, minimalistic and welcoming design.
    * Simple, easy and fast booking with strong form validation.
    * All bookings are easily manageable for the user in the 'My Reservations' page.

* Staff Dashboard
    * Home, Dashboard, Bookings, Check In, Payments, Reviews, Staff Help.
    * A separate, detached part of the website theme for staff members to manage everything at Cafe Manbo.
    * Informative dashboard panel which showcases a vast range of statistical data about Cafe Manbo.
    * A simple and logical booking flow system.
    * A staff help modal to aid staff members.

## Design Choices

 * ### Typography
      The fonts chosen were 'Oswald' for the golden headings and I decided to use the standard 'sans-serif' for the body text however different font-weights and font-sizes were used to give further clarity. All fonts fall back to sans-serif respectively if the 'Oswald' font can't be loaded.

    * 'Oswald' was chosen primarily to give a touch of style and elegance to the website. The font-style is very     modern, stylish, clean and gives a professional and inviting feeling to the website.

 * ### Colour Scheme
      The colour scheme chosen is one based on a rich gold, eerie-black and off-white. This colour scheme gives off a warm, clean, minimalistic and positive feeling to the website.<br /><br />

![Colour Palette image](static/images/readme-images/colour-palette-image.png)

## Project Management

 * ### Trello
      I used an excellent application called [Trello](https://trello.com/en-GB) which greatly improved organisation and productivity. This tool allows the individual to properly plan and create a systematic work flow so you are always aware of what needs to be done next.

      I would first create a very basic overview of what I wanted to achieve and then break it down into smaller more manageable steps. Before finishing for the day, I would spend at least 15 minutes planning for the next day so that when I came back to developing I could open my Trello board and instantly get back developing since I would know immediately what I need to be working on. I highly recommend this tool to any developer or development team. <br /><br />

![Trello Image](static/images/readme-images/trello-image.png)


## Existing Features For Site User

  * ### Responsive Navigation Bar

      * The navigation bar is an extremely important and integral part of any website so I decided to spend a lot of time trying to make one that is very user friendly that would promote a positive emotional response for the user.
      * Using a mixture of both CSS, JavaScript and Bootstrap, I've created a dynamic, responsive and animated navigation bar.
      * Upon initial visit, the entire navigation bar will be transparent but upon scrolling 350px, the navigation bar will then apply a dark background. The dark background will also be applied when the navigation bar becomes responsive.
      * I decided to create 2 navigation bars for the main website. navbar.html is the home page navbar which is transparent at first then transitions to dark after 350px and navbar_2.html is a non-transparent navbar which is used for all subsequent pages
      * If a user has not logged in then the navigation bar will show the 'Account' option. After they have signed in, it will then display their username. To mitigate any responsive design issues, I have decided to slice the first 10 characters of their name and display that to the user.
      * When the navigation bar hits the breakpoint, it will then collapse into a hamburger which I have made animate into a red cross when clicked.  <br /><br />

<details><summary><b>Transparent Navigation Bar</b></summary>

![Transparent Navigation Bar](static/images/readme-images/navbar-transparent-image.png)
</details><br />

<details><summary><b>Navigation Bar Transition 350px</b></summary>

![Navigation Bar Transition 350px](static/images/readme-images/navbar-transition-image.png)
</details><br />

<details><summary><b>Navigation Bar Transition Code</b></summary>

![Navigation Bar Transition Code](static/images/readme-images/navbar-transition-code-image.png)
</details><br />

<details><summary><b>Navigation Bar Responsive Image</b></summary>

![Navigation Bar Responsive Image](static/images/readme-images/navbar-responsive-image.png)
</details><br />

<details><summary><b>Navigation Bar Responsive Dropdown Image</b></summary>

![Navigation Bar Responsive Dropdown Image](static/images/readme-images/navbar-responsive-dropdown-image.png)
</details><br />

  * ### Dynamic Reviews 

      * Reviews from other guests can be the deciding factor when it comes to new guests deciding whether to dine at the restaurant, therefore I had decided that being able to display dynamic reviews to the user was important and worth the development time.
      * 4 Reviews will be displayed at random given that they have been approved and verified by a member of staff.
      * Each review is housed in it's own card, showing the guests name, the star rating the guest selected, the first 80 characters (including spaces) of their review and then a Read More button.
      * Clicking the Read More button will trigger a modal that will show the user the full review <br /><br />

<details><summary><b>Review Cards Image</b></summary>

![Image](static/images/readme-images/review-image.png)
</details><br />

<details><summary><b>Review Modal Image</b></summary>

![Image](static/images/readme-images/review-modal-image.png)
</details><br />

  * ### Hours & Location

      * Text 1
      * Text 2<br /><br />

<details><summary><b>Feature Image</b></summary>

![Image]()
</details><br />

  * ### Footer

      * Text 1
      * Text 2<br /><br />

<details><summary><b>Feature Image</b></summary>

![Image]()
</details><br />

  * ### Our Menu

      * Text 1
      * Text 2<br /><br />

<details><summary><b>Feature Image</b></summary>

![Image]()
</details><br />

  * ### Gallery

      * Text 1
      * Text 2<br /><br />

<details><summary><b>Feature Image</b></summary>

![Image]()
</details><br />

  * ### Book Now

      * Text 1
      * Text 2<br /><br />

<details><summary><b>Feature Image</b></summary>

![Image]()
</details><br />

  * ### My Reservations

      * Text 1
      * Text 2<br /><br />

<details><summary><b>Feature Image</b></summary>

![Image]()
</details><br />

  * ### Account Creation

      * Text 1
      * Text 2<br /><br />

<details><summary><b>Feature Image</b></summary>

![Image]()
</details><br />

  * ### Write A Review

      * Text 1
      * Text 2<br /><br />

<details><summary><b>Feature Image</b></summary>

![Image]()
</details><br />


## Existing Features For Site Staff Member

  * ### Staff Dashboard

      * Text 1
      * Text 2<br /><br />

<details><summary><b>Feature Image</b></summary>

![Image]()
</details><br />

  * ### Responsive Navigation Bar

      * Text 1
      * Text 2<br /><br />

<details><summary><b>Feature Image</b></summary>

![Image]()
</details><br />

  * ### Bookings

      * Text 1
      * Text 2<br /><br />

<details><summary><b>Feature Image</b></summary>

![Image]()
</details><br />

  * ### Check In

      * Text 1
      * Text 2<br /><br />

<details><summary><b>Feature Image</b></summary>

![Image]()
</details><br />

  * ### Payments

      * Text 1
      * Text 2<br /><br />

<details><summary><b>Feature Image</b></summary>

![Image]()
</details><br />

  * ### Reviews

      * Text 1
      * Text 2<br /><br />

<details><summary><b>Feature Image</b></summary>

![Image]()
</details><br />

  * ### Staff Help

      * Text 1
      * Text 2<br /><br />

<details><summary><b>Feature Image</b></summary>

![Image]()
</details><br />

[Back to top](<#contents>)


* ## Future Features 

* ### Future Feature 1

    * Text.

* ### Future Feature 2

    * Text.

# Technologies Used
* [HTML5](https://en.wikipedia.org/wiki/HTML) - Provides the content and structure for the website.
* [CSS3](https://en.wikipedia.org/wiki/CSS) - Provides the styling for the website.
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) - Provides the functionality of the website.
* [a11y](https://color.a11y.com/Contrast/) - Used to test the contrast and accessibility.
* [Favicon](https://favicon.io/) - Used to create the favicon.
* [Compressor](https://compressor.io/) - Used to compress the images.
* [VSCode](https://code.visualstudio.com/) - Used to create and edit the website.
* [GitHub](https://github.com/) - Used to host and deploy the website.
* [GitBash](https://en.wikipedia.org/wiki/Bash_(Unix_shell)) - Terminal used to push changes to the GitHub repository.
* [removebg](https://www.remove.bg/) - Used to remove background images.
* [Google Chrome DevTools](https://developer.chrome.com/docs/devtools/) - Used to test responsiveness and debug.
* [Responsive Design Checker](https://www.responsivedesignchecker.com/) - Used to test responsiveness.
* [Balsamiq](https://balsamiq.com/) - Used to create the wire-frame.
* [Draw.io](https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio) - Used to create the logic flow chart.
* [Trello](https://trello.com/en-GB) - Used as a project management tool to organise my work flow.

# Python Packages

* [Random](https://docs.python.org/3/library/random.html) - Used to implement pseudo-random number generators.
* [Datetime](https://docs.python.org/3/library/datetime.html) - Used to manipulate dates and times.
* [OS](https://docs.python.org/3/library/os.html) - Used to provide a way of using operating system dependent functionality.
* [Time](https://docs.python.org/3/library/time.html) - Used to provide various time-related functions.


[Back to top](<#contents>)

# Testing

* ## Code Validation

    * Cafe Manbo has been validated by using online validation tools [W3C HTML Validator](https://validator.w3.org/), [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) and the [PEP8 Online Validator](http://pep8online.com/). I encountered many PEP8 errors and warnings however these have now been fixed and documented below. 

* ### HTML Validation Image

    ![HTML Validation]()

* ### CSS Validation Image

    ![CSS Validation]()

* ### PEP8 Validation Image (run.py)

    ![PEP8 Validation (run.py)]()

* ### PEP8 Validation Image (print.py)

    ![PEP8 Validation (print.py)]()

* ### PEP8 Validation Image (questions.py)

    ![PEP8 Validation (questions.py)]()

* ## Lighthouse Testing 

    * Furthermore the website has been through the [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) and [Microsoft Edge Dev Tools](https://docs.microsoft.com/en-us/microsoft-edge/devtools-guide-chromium/open/?tabs=cmd-Windows) Lighthouse Testing which tests the website for the following:
        * Performance - How the page performs whilst loading.
        * Accessibility - Is the site accessible for all players and how can it be improved.
        * Best Practices - Site conforms to industry best practices.
        * SEO - Search Engine Optimisation. Is the site optimised for search engine result rankings.

    * The lighthouse tests were conducted in incognito/private windows due to extensions interfering with the results.<br /><br />

* ### Edge Desktop Lighthouse Result

    ![Edge Desktop Lighthouse]()

* ### Edge Mobile Lighthouse Result

    ![Edge Mobile Lighthouse]()

* ### Chrome Desktop Lighthouse Result

    ![Chrome Desktop Lighthouse]()

* ### Chrome Mobile Lighthouse Result

    ![Chrome Mobile Lighthouse]()

* ## Accessibility Testing
    * I also put the website through [a11y](https://color.a11y.com/Contrast/) to further test the contrast and found no issues. <br /><br />

    ![a11y Test]()

* ## Responsiveness Testing
    * I conducted responsive tests manually with [Google Chrome DevTools](https://developer.chrome.com/docs/devtools/) and [Responsive Design Checker](https://www.responsivedesignchecker.com/).<br /><br />

    ![Responsive Test Sheet]()


* ## Compressing Images
    * All images that are displayed within the website have been compressed with [Compressor](https://compressor.io/) and I managed to save a total of XXX KB.<br /><br />

    ![Compressed Image 1])

* ## Manual Testing
    * In addition to the other tests, I have conducted a manual check list for myself to carry out to make sure that everything is working as intended.

   * ### Manual Tests Conducted
      * **Manual Test 1**
        * Verification step
        * Verification step
        * Verification step
      * **Manual Test 2**
        * Verification step
        * Verification step
        * Verification step
        <br /><br />

* ## Browser Compatibility
    * The website has had manual and responsive tests conducted on the below browsers with additional Lighthouse testing on Google Chrome and Microsoft Edge and I was presented with no issues.
        * Google Chrome
        * Microsoft Edge
        * Safari
        <br /><br />

[Back to top](<#contents>)

* ## Bugs Fixed 

    ### Bug Fixed 1
        
    * Text <br /><br />

    ![Leaderboards Fixed]()


* ## Bugs Unresolved

    ### Bugs Unresolved 1

    * Text <br /><br />

    ### navigator.userAgent/appVersion and platform
    
    * When inspecting the website with [Google Chrome DevTools](https://developer.chrome.com/docs/devtools/), the website is showing one issue which is the same issue I had on my Project Portfolio 1 and Project Portfolio 2 so I'm familiar with it.<br /><br />

    ![Site Issue](assets/images/readme-images/navigator-agent-issue-image.png)
    
    * I've done some research and apparently this is a Google Chrome issue as per this [source](https://forum.codewithmosh.com/t/the-ultimate-javascript-console-issue-at-beginning-of-course/6535) and has been reported [here](https://githubmemory.com/repo/zalmoxisus/redux-devtools-extension/issues/808). Additionally, I have tested this website with Microsoft Edge and the issue doesn't show.



[Back to top](<#contents>)

# Deployment To Heroku
  
The project was deployed to [Heroku](https://www.heroku.com). The deployment process is as follows: 
  
1. Log in to Heroku or create an account if required.

<details><summary><b>Heroku Step 1</b></summary>

![Heroku Step 1]()
</details><br />

2. Click the button labeled New from the dashboard in the top right corner, just below the header and then select "Create new app".

<details><summary><b>Heroku Step 2</b></summary>

![Heroku Step 2]()
</details><br />

3. Enter a unique application name and then select your region. Once you are ready, click "Create app".

<details><summary><b>Heroku Step 3</b></summary>

![Heroku Step 3]()
</details><br />

4. This will bring you to the project "Deploy" tab. From here, click the "Settings" tab and scroll down to the "Config Vars" section and click on "Reveal Config Vars". In the KEY input field, enter "PORT" and in the VALUE input field, enter "8000". After that, click the "Add" button to the right.

<details><summary><b>Heroku Step 4</b></summary>

![Heroku Step 4]()
</details><br />

5. Scroll down to the buildpacks section of the settings page and click the button "Add buildpack".

<details><summary><b>Heroku Step 5</b></summary>

![Heroku Step 5]()
</details><br />

6. Add both "Python" and "node.js" and make sure that Python is above node.js. If it isn't you can just drag it above.

<details><summary><b>Heroku Step 6</b></summary>

![Heroku Step 6]()
</details><br />

7. Scroll back to the top of the settings page, and navigate to the "Deploy" tab. Select Github as the deployment method.

<details><summary><b>Heroku Step 7</b></summary>

![Heroku Step 7]()
</details><br />

8. Search for the repository name and click the connect button next to the intended repository.

<details><summary><b>Heroku Step 8</b></summary>

![Heroku Step 8]()
</details><br />

9. From the bottom of the deploy page select your preferred deployment type. I personally enabled automatic deployments. After that, click "Deploy Branch".

<details><summary><b>Heroku Step 9</b></summary>

![Heroku Step 9]()
</details><br />

The live link to the Github repository can be found here - https://github.com/MikeR94/CI-Project-Portfolio-4

[Back to top](<#contents>)

# Credits
### Content

* Text

### Media
* The photos were compressed using [Compressor](https://compressor.io/).
* The favicon image came from [encrypted-tbn0](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTjtOmemr76GOUK79y3itlIDr5bYfWiS-F2xixdV1qg4e9WI8POOvZ0TV06TKCmL7zE3Ko&usqp=CAU) and then turned into a favicon by [Favicon](https://favicon.io/).

[Back to top](<#contents>)

# Acknowledgments
The site was completed as a part of a Full Stack Software Developer Diploma at the [Code Institute](https://codeinstitute.net/) and is my Portfolio Project 4. I would like to thank my mentor [Precious Ijege](https://www.linkedin.com/in/precious-ijege-908a00168/), my educator [Luke Walters](https://www.linkedin.com/in/luke-walters-leatherbarrow-531107101/), and my brother [Jack Ralph](https://www.linkedin.com/in/jackthomasralph/), the Slack community, and all at the Code Institute for their help and support.

# Personal Development
Text

Mike Ralph 2022.

[Back to top](<#contents>)
