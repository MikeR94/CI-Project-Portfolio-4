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
      * Upon initial visit, the entire navigation bar will be transparent but upon scrolling 50px, the navigation bar will then apply a dark background. The dark background will also be applied when the navigation bar becomes responsive.
      * I decided to create 2 navigation bars for the main website. navbar.html is the home page navbar which is transparent at first then transitions to dark after 350px and navbar_2.html is a non-transparent navbar which is used for all subsequent pages
      * If a user has not logged in then the navigation bar will show the 'Account' option. After they have signed in, it will then display their username. To mitigate any responsive design issues, I have decided to slice the first 10 characters of their name and display that to the user.
      * When the navigation bar hits the breakpoint, it will then collapse into a hamburger which I have made animate into a red cross when clicked.  <br /><br />

<details><summary><b>Transparent Navigation Bar</b></summary>

![Transparent Navigation Bar](static/images/readme-images/navbar-transparent-image.png)
</details><br />

<details><summary><b>Navigation Bar Transition 50px</b></summary>

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

![Review Cards Image](static/images/readme-images/review-image.png)
</details><br />

<details><summary><b>Review Modal Image</b></summary>

![Review Modal Image](static/images/readme-images/review-modal-image.png)
</details><br />

  * ### Hours & Location

      * Informing the user where the restaurant is located is extremely important, therefore I decided to have clean, decisive information regarding the whereabouts of Cafe Manbo.
      * Integrated Google Maps so the user can visually see the location.
      * The address, location and phone number used are completely made up for security purposes.
      <br /><br />

<details><summary><b>Hours & Location Image</b></summary>

![Hours & Location Image](static/images/readme-images/hours-location-image.png)
</details><br />

  * ### Footer

      * A simplistic yet elegant design, used to naturally end the page and provide the user with some quick links so they can navigate the website faster if they wish to. <br /><br />

<details><summary><b>Footer Image</b></summary>

![Footer Image](static/images/readme-images/footer-image.png)
</details><br />

<details><summary><b>Footer Responsive Image</b></summary>

![Footer Responsive Image](static/images/readme-images/footer-responsive-image.png)
</details><br />

  * ### Our Menu

      * I decided that it was a lot more practical and also I think professional to design the menu on an external PDF and then host that for the user to view. 
      * The menu was designed using [Canva](https://www.canva.com/) and then hosted on [Cloudinary](https://cloudinary.com/) <br /><br />

<details><summary><b>Menu Image 1</b></summary>

![Menu Image 1](static/images/readme-images/menu-image-1.png)
</details><br />

<details><summary><b>Menu Image 2</b></summary>

![Menu Image 2](static/images/readme-images/menu-image-2.png)
</details><br />

<details><summary><b>Menu Image 3</b></summary>

![Menu Image 3](static/images/readme-images/menu-image-3.png)
</details><br />

  * ### Gallery

      * The gallery page is used as way to showcase images of the restaurant to users. As the saying goes, a picture paints a thousand words and being able to show appealing images will greatly increase the chances of guests visiting Cafe Manbo. <br /><br />

<details><summary><b>Gallery Image</b></summary>

![Gallery Image](static/images/readme-images/gallery-image.jpg)
</details><br />

  * ### Book Now

      * The book now page will only be accessible if the user has logged in with an account. If they have not logged in and they click the Book Now link, they will be redirected to the log in page
      * I have spent a lot of development time working on form validation since Cafe Manbo is a restaurant website, each booking needs to be unique and fully validated before a staff member needs to spend time processing it.
      * Alongside the standard input field validation, I have also added some additional validation which checks if the user is booking in the past. For example, if the time is 19:00 and they are trying to book for 17:00, then it will throw an error informing the user that they can't book in the past. The same goes for the date, if they try book for a date that isn't either today or in the year 2022, it will inform the user accordingly.
      * Additionally I have accounted for double bookings. When the user submits the form, I then collect all that data, check if the database holds a booking with very similar data and if so, inform the user that the booking was unsuccessful because we appear to already have this booking in the database. <br /><br />

<details><summary><b>Book Now Image</b></summary>

![Book Now Image](static/images/readme-images/book-now-image.png)
</details><br />

<details><summary><b>Book Now Responsive Image</b></summary>

![Book Now Responsive Image](static/images/readme-images/book-now-responsive-image.png)
</details><br />

<details><summary><b>Book Now Success Image</b></summary>

![Book Now Success Image](static/images/readme-images/book-now-success-image.png)
</details><br />

<details><summary><b>Book Now Duplicate Image</b></summary>

![Book Now Duplicate Image](static/images/readme-images/book-now-duplicate-image.png)
</details><br />

<details><summary><b>Date Of Visit Custom Validation</b></summary>

![Date Of Visit Custom Validation](static/images/readme-images/date-of-visit-validation-image.png)
</details><br />

<details><summary><b>Time Of Visit Custom Validation</b></summary>

![Time Of Visit Custom Validation](static/images/readme-images/time-of-visit-validation-image.png)
</details><br />

  * ### My Reservations

      * The My Reservations page was created so that a user can manage all of their bookings in one distinct place.
      * If a user does not have any bookings stored in the database, then they will be prompted with a "no bookings found" page.
      * Each booking is displayed individually for the user with some informative data about that booking and also a blue Details button which will load even further information about that users booking.
      * I decided that a user would have only a few pending bookings, however if a customer really enjoys Cafe Manbo then they could potentially have multiple completed bookings and therefore I decided to place all completed bookings within a collapsible bootstrap accordion to help with the page space and presentation
      * There are currently 5 different states that a users booking can be in. They are the following: <br /><br />
        * <strong>Awaiting Approval</strong> - <i>Booking has been submitted, awaiting staff members approval</i>
        * <strong>Booking Approved</strong> - <i>Staff member has approved the booking but the guest has not yet attended</i>
        * <strong>Booking Attended</strong>- <i>Booking has been approved and the guest has attended</i>
        * <strong>Booking Denied</strong> - <i>Booking has been submitted but a staff member denied the booking</i>
        * <strong>Booking Not Attended</strong> - <i> Staff member has approved the booking but the guest did not attend </i> <br /><br />
      * If a user clicks the blue details booking to load the additional information about their booking, if the booking has not been completed then they will have the option to Edit or Cancel the booking. Clicking the edit booking will launch a modal that will allow the user to submit new information for that booking. If it passes the form validation requirements then the booking state will be set back to "Awaiting Approval" and a staff member will need to approve this booking.
      * Alternatively if they click cancel booking, a separate modal will pop up and prompt the user asking them if they wish to cancel this booking. Doing so will completely delete this booking from the database.<br /><br />
    

<details><summary><b>No Bookings Found Image</b></summary>

![No Bookings Found Image](static/images/readme-images/my-reservations-empty-image.png)
</details><br />

<details><summary><b>My Reservations All States Image</b></summary>

![My Reservations All States Image](static/images/readme-images/my-reservations-all-states-image.png)
</details><br />

<details><summary><b>My Reservations Details Image</b></summary>

![My Reservations Details Image](static/images/readme-images/my-reservations-details-image.png)
</details><br />

<details><summary><b>My Reservations Edit Booking Image</b></summary>

![My Reservations Edit Booking Image](static/images/readme-images/my-reservations-edit-modal-image.png)
</details><br />

<details><summary><b>My Reservations Cancel Booking Image</b></summary>

![My Reservations Cancel Booking Image](static/images/readme-images/my-reservations-cancel-image.png)
</details><br />

  * ### Account Creation

      * To enable users to be able to create an account on the website, I used a brilliant package called [Django AllAuth](https://django-allauth.readthedocs.io/en/latest/installation.html) and then customised the html pages to fit the theme of the website.
      * <br /><br />

<details><summary><b>Signup Image</b></summary>

![Signup Image](static/images/readme-images/signup-image.png)
</details><br />

<details><summary><b>Login Image</b></summary>

![Login Image](static/images/readme-images/login-image.png)
</details><br />

<details><summary><b>Password Reset Image</b></summary>

![Password Reset Image](static/images/readme-images/password-reset-image.png)
</details><br />

  * ### Write A Review

      * If a user has logged in, they are able to submit a review for the restaurant.
      * This review then has to be approved by a member of staff before it gets rendered on the home page for other users to view.
      * Standard form validation applies to all fields with the additional form validation on the body field asking the user to submit a review that is at least 80 characters long. This is done for two reasons, firstly it helps with the presentation of the preview cards and secondly, it can can prevent users submitting very small reviews that don't give a very insightful look at what it's like to dine at Cafe Manbo.
      * When a user has successfully submitted a review, they will be presented with a thank you page, thanking the user for their review and also provide them with a preview of how their review will look like on the home page if their review is approved by a member of staff. <br /><br />

<details><summary><b>Write A Review Image</b></summary>

![Write A Review Image](static/images/readme-images/write-review-image.png)
</details><br />

<details><summary><b>Review Submitted Image</b></summary>

![Review Submitted Image](static/images/readme-images/review-submitted-image.png)
</details><br />


## Existing Features For Site Staff Member

  * ### Staff Dashboard

      * The staff dashboard was created to give staff members a visually appealing but more importantly, an insightful way of viewing statistical data about Cafe Manbo.
      * 4 bootstrap cards are located at the top of the page giving information about Total Bookings, Total Guests, Total Reviews and Total Income. All this data is completely dynamic and is gathered from the database.
      * I have used a brilliant piece of third-party software from [ChartJS](https://www.chartjs.org/) which allows me to display data in a visually appealing way such as a bar or pie chart. Using this software I am able to immediately display to staff members how many bookings and how many guests have attended given a 12 month period.
      * To complete the staff dashboard, I have created a 'Quick Statistics' section which gives additional fast and basic information about Cafe Manbo. All the data is completely dynamic <br /><br />

<details><summary><b>Staff Dashboard Image</b></summary>

![Staff Dashboard Image](static/images/readme-images/staff-dashboard-image.png)
</details><br />

<details><summary><b>Staff Dashboard Cards Image</b></summary>

![Staff Dashboard Cards Image](static/images/readme-images/staff-dashboard-cards-image.png)
</details><br />

<details><summary><b>Staff Dashboard Bar Chart Image</b></summary>

![Staff Dashboard Bar Chart Image](static/images/readme-images/staff-dashboard-bar-chart-image.png)
</details><br />

<details><summary><b>Staff Dashboard Pie Chart Image</b></summary>

![Staff Dashboard Pie Chart Image](static/images/readme-images/staff-dashboard-pie-chart-image.png)
</details><br />

<details><summary><b>Staff Dashboard Quick Statistics Image</b></summary>

![Staff Dashboard Quick Statistics Image](static/images/readme-images/staff-dashboard-quick-statistic-image.png)
</details><br />

  * ### Responsive Navigation Bar

      * The navigation bar for the staff dashboard is positioned on the left hand side to give an administrative feel to this part of the website.
      * 7 available links for a staff member to click. Home, Dashboard, Bookings, Check In, Payments, Reviews and Staff Help <br /><br />
        * <strong>Home</strong> - <i>Returns the staff member back to the home page of the main website</i>
        * <strong>Dashboard</strong> - <i>Loads the staff dashboard page</i>
        * <strong>Bookings</strong> - <i>Loads the bookings page</i>
        * <strong>Check In</strong> - <i>Loads the check in page</i>
        * <strong>Payments</strong> - <i>Loads the payments page</i>
        * <strong>Reviews</strong> - <i>Loads the reviews page</i>
        * <strong>Staff Help</strong> - <i>Loads a modal to aid staff members</i><br /><br />
    
    * Bookings, Check In, Payments and Reviews have a red notification number that will be rendered to the side of the link if there is any form of information that is required for a staff member to deal with. For example, if there is a new booking that has come in from a guest, the Booking link will show a (1) next to it informing the staff member that there is a booking that requires attention.<br /><br />

<details><summary><b>Staff Navigation Bar Image</b></summary>

![Staff Navigation Bar Image](static/images/readme-images/staff-navbar-image.png)
</details><br />

<details><summary><b>Staff Navigation Bar Responsive Image</b></summary>

![Staff Navigation Bar Responsive Image](static/images/readme-images/staff-navbar-responsive-image.png)
</details><br />

  * ### Bookings

      * This is the first part of the booking flow system. When a guest makes a booking, it will then be displayed here for a staff member to either approve or deny. When a staff member has approved or denied a booking, it will be removed from this page and a flash message will appear giving the staff member additional feedback that their action has been submitted
      * A staff member can click the "All bookings View Here" which will render a new page which utilises [DataTables](https://datatables.net/). I've decided to use Data Tables to help with presentation and aid staff members in locating specific bookings. If and when the restaurant has hundreds, even thousands of bookings, a staff member can use the search feature to quickly identify and navigate to that booking.
      * I have integrated automatic email sending which will send an email to the users booking email informing them that their booking has either been approved or denied.   <br /><br />

<details><summary><b>Staff Bookings Image</b></summary>

![Staff Bookings Image](static/images/readme-images/staff-bookings-image.png)
</details><br />

<details><summary><b>Staff Bookings Responsive Image</b></summary>

![Staff Bookings Responsive Image](static/images/readme-images/staff-bookings-responsive-image.png)
</details><br />

<details><summary><b>Staff All Bookings Image</b></summary>

![Staff All Bookings Image](static/images/readme-images/staff-all-bookings-image.png)
</details><br />

<details><summary><b>Staff All Bookings Responsive Image</b></summary>

![Staff All Bookings Responsive Image](static/images/readme-images/staff-all-bookings-responsive-image.png)
</details><br />

<details><summary><b>Staff Details Booking Image</b></summary>

![Staff Details Bookings Image](static/images/readme-images/staff-details-booking.png)
</details><br />

<details><summary><b>Staff Bookings Approved Flash Image</b></summary>

![Staff Bookings Approved Flash Image](static/images/readme-images/staff-booking-approved-flash-image.png)
</details><br />

<details><summary><b>Staff Bookings Denied Flash Image</b></summary>

![Staff Bookings Denied Flash Image](static/images/readme-images/staff-booking-denied-flash-image.png)
</details><br />

  * ### Check In

      * This is the second part of the booking flow system. After a staff member has approved a booking, the booking will then be displayed here if the booking in question is on todays date. For example if a booking is made and approved for 15/05/2022, that booking will only be displayed on the check in page on 15/05/2022. This is done to aid staff members when it comes to checking guests in.
      * If a staff member checks a guest in, the booking will then be removed from the check in page and then it will be sent to the third and final stage of the booking flow system which is the payments page.
      * If a staff member marks a guest as no show then the booking will not be sent to the payments stage.
      * Additionally, if a staff member is too busy and doesn't "no-show" a guest because they didn't turn up, the following day when the staff member clicks the 'Check In' link on the navigation bar, the system will send an automatic email out to the guest informing them that they did not show up.
      * An email will be sent out to the guest for both 'Check In' and 'No Show'. This is sent out for security measures.<br /><br />

<details><summary><b>Staff Check In Image</b></summary>

![Staff Check In Image](static/images/readme-images/staff-check-in-responsive-image.png)
</details><br />

<details><summary><b>Staff Check In Responsive Image</b></summary>

![Staff Check In Responsive Image](static/images/readme-images/staff-check-in-image.png)
</details><br />

  * ### Payments

      * This is the third and final part of the booking flow system. After a staff member has checked the booking in, the booking will then be displayed here.
      * When the staff member clicks the yellow Payment button, it will then render a new page which will display additional information about that booking along with 2 input fields where a staff member can submit payment information.
      * To prevent staff members submitting payments that have not been settled, I have included some simple form validation that will check if the amount paid is equal or more than the amount owed. 
      * When a staff member has successfully submitted payment details for that booking, the payment form will be removed and the details page will be updated.
      * This is then the end of the booking flow system however a staff member will still be able to access this booking through the Bookings > All Bookings page <br /><br />

<details><summary><b>Staff Payment Image</b></summary>

![Staff Payment Image](static/images/readme-images/staff-payment-image.png)
</details><br />

<details><summary><b>Staff Payment Responsive Image</b></summary>

![Staff Payment Responsive Image](static/images/readme-images/staff-payment-responsive-image.png)
</details><br />

<details><summary><b>Staff Payment Details Image</b></summary>

![Staff Payment Details Image](static/images/readme-images/staff-payment-details-image.png)
</details><br />

<details><summary><b>Staff Payment Details Submitted Image</b></summary>

![Staff Payment Details Submitted Image](static/images/readme-images/staff-payment-details-submitted-image.png)
</details><br />

<details><summary><b>Staff Payment Validation Image</b></summary>

![Staff Payment Validation Image](static/images/readme-images/staff-payment-validation-image.png)
</details><br />

  * ### Reviews

      * This is the section which will present all reviews that have been submitted by guests. 
      * Upon clicking the Reviews link on the navigation bar, the reviews that have not yet been actioned by a staff member will be presented here. At the top of the page is a link that will take the staff member to a page that will render all reviews. Here they can reset a review which will send it back to pending so they can either re-approve or re-deny the review.<br /><br />

<details><summary><b>Staff Reviews Image</b></summary>

![Staff Reviews Image](static/images/readme-images/staff-reviews-image.png)
</details><br />

<details><summary><b>Staff All Reviews Image</b></summary>

![Staff All Reviews Image](static/images/readme-images/staff-all-reviews-image.png)
</details><br />

  * ### Staff Help

      * This is a simple link that will pop a modal up which is aimed to help and aid the staff member when navigating the staff dashboard.<br /><br />

<details><summary><b>Staff Help Booking Modal Image</b></summary>

![Staff Help Booking Modal Image](static/images/readme-images/staff-help-booking-image.png)
</details><br />

<details><summary><b>Staff Help Check In Modal Image</b></summary>

![Staff Help Check In Modal Image](static/images/readme-images/staff-help-booking-image.png)
</details><br />

<details><summary><b>Staff Help Payment Modal Image</b></summary>

![Staff Help Payment Modal Image](static/images/readme-images/staff-help-payment-image.png)
</details><br />

<details><summary><b>Staff Help Review Modal Image</b></summary>

![Staff Help Review Modal Image](static/images/readme-images/staff-help-review-image.png)
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
