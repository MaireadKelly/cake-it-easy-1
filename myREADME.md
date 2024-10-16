# The Bakery

[The Bakery](https://the-bakery-7e15a3228766.herokuapp.com/) is a fictional B2C ecommerce website that specializes in selling homemade baked goods to online consumers.

![Responsive Image](./documents/images/validation/responsive-screenshot.webp)

# Table Of Content

- [Business Ecommerce Model](#business-ecommerce-model)
- [User Experience](#user-experience)
  - [User Stories](#user-stories)
- [Design](#design)
  - [ERD](#erd)
  - [Wireframes](#wireframes)
  - [Fonts](#fonts)
  - [Colour Scheme](#colour-scheme)
- [Development](#development)
  - [Agile Methodology](#agile-methodology)
    - [EPICS(Milestones)](#epics---milestones)
  - [Technologies Used](#technologies-used)
- [Features](#features)
  - [Flow of the Website](#flow-of-the-website)
  - [Create Account](#create-account)
  - [User Profiles](#user-profiles)
  - [Social Interactions](#social-interactions)
  - [CRUD](#crud)
  - [Product Management](#product-management)
- [Testing](#testing)
- [Deployment](#deployment)
  - [Clone the Repository](#clone-the-repository)
  - [Fork the Repository](#fork-the-repository)
  - [Heroku](#heroku)
- [Credits](#credits)
  - [Content](#content)
  - [Code](#code)
  - [Acknowledgements](#acknowledgements)

## Business Ecommerce Model

The marketing strateing and seo techniques are documented in a separate file for organisation. It can be found here. [MARKETING.md](https://github.com/amy-1989/the-bakery/blob/main/MARKETING.md)

## User Experience

### User Stories

Site Owner:

- As a Site Owner I want to be able to add/remove and edit my goods with ease.
- As a Site Owner I want my website to appear in the top results of search engines like Google.

Site User:

- As a Site User I want to view goods to buy online.
- As a Site User I want to see a detailed view of a single item to buy.
- As a Site User I want to see user reviews of goods.
- As a Site User I want to see an image and price of the goods for sale.
- As a Site User I want to use a searchbar to easily find specific goods.
- As a Site User I want to be able to learn more about the business.
- As a Site User I want to be able to contact the business with any queries.
- As a Site User I want to create an account.
- As a Site User I want to view my previous orders.
- As a Site User I want to receive email confirmation of my order.
- As a Site User I want to save my shipping information for future use.
- As a Site User I want to be able to delete my personal details.
- As a Site User I want to be able to raise any issues I have with my orders.
- As a Site User I want to be able to add comments about products.
- As a Site User I want to be able to delete my comments.
- As a Site User I want to be able to delete my account.
- As a Site User I want to be able to delete my ratings.

## Design

### ERD

![ERD LucidChart](./documents/images/design/erd.png)

### Wireframes

- Products Wireframe

![Products Page Wireframe](./documents/images/design/the_bakery.PNG)

- Products Detail Wireframe

![Products Detail Page Wireframe](./documents/images/design/product_detail_page.PNG)

- Products Detail Ratings and Comments Section

![Products Detail Ratings and Comments View](./documents/images/design/product_detail_rating_comment_view.PNG)

- Checkout Wireframe

![Checkout Page](./documents/images/design/checkout_page.PNG)

### Fonts
Roboto from Google Fonts was chosen as the predominant font throughout the site for its clean lines and clarity. It is very easy to read and accessible.

### Colour Scheme
The colours of blue, pink, white and greys was chosen to match in with the business logo. White was chosen as the predominant background colour to let the products stand out for themselves, and not have to compete with a strong background hue. 

## Development

### Agile Methodology
This project was developed using the Agile methodology. All epics and user stories progress was tracked through Github projects ![Kanban Board](./documents/images/other/kanban-board.webp).

#### Epics(Milestones)

Epic 1: Initial Setup

- As a developer, I need to create the base.html template, including navbar and footer so that other pages can reuse the layout
- As a developer I need to create an env.py file to store sensitive data for security reasons.
- As a developer, I need to create a static folder so that images, css and javascript work on the website
- As a developer, I need to set up the models so that the websites main functions will work
- As a developer I need to set up the admin file so that I can test the backend functionality

Epic 2: User Authentication

- As a developer, I need to set up the Sign Up page using django-allauth.
- As a developer, I need to set up the Sign in page using django-allauth.
- As a developer, I need to set up the Sign out page using django-allauth.
- As a site owner, I would like the sites authentication pages to be styled to match the websites theming.
- As a user, I would like to be able to create my own account.
- As a user, I would like to be able to delete my account in the future if I wish.
- As a user, I would like to be able to sign in and sign out with ease.

Epic 3: Shopping

- As a Site User I want to view goods to buy online.
- As a Site User I want to see a detailed view of a single item to buy.
- As a Site User I want to see user reviews of goods.
- As a Site User I want to see an image and price of the goods for sale.
- As a Site User I want to use a searchbar to easily find specific goods.
- As a Site Owner I want to be able to add products to sell easily.
- As a Site Owner I want to be able to edit or remove products when necessary.

Epic 4: Checkout

- As a Site User I want to view my previous orders.
- As a Site User I want to receive email confirmation of my order.
- As a Site Owner I want to ensure my orders go through without issue.
- As a developer I need to set up webhooks to ensure Stripe creates orders if there is an error on our site.

Epic 5: User Profiles

- As a Site User I want to save my shipping information for future use.
- As a Site User I want to be able to view my previous orders.
- As a Site user I want to be able to send feedback about my orders.
- As a Site User I want to be able to delete my personal details.
- As a Site User I want to be able to set a primary delivery address.
- As a Site User I want to be able to delete my account.

Epic 6: Social Interactions

- As a Site User I want to be able to add comments about products.
- As a Site User I want to be able to delete my comments.
- As a Site User I want to be able to rate and review the products.
- As a Site User I want to be able to delete my ratings.
- As a Site User I want to be able to contact the business.
- As a Site User I want to see their social sites.

Epic 7: Deployment

- As a developer, I need to deploy the project to heroku so that users can visit and use the site.
- As a developer I need to ensure all sensitive information is stored in an env file so they are secure.
- As a developer I need to ensure that debug is set to false before deployment to prevent compromising the site.


Epic 8: Documentation

- As a developer I want to create the README.

### Technologies Used

- Python
- HTML
- CSS
- GitHub
- GitPod
- Git
- Heroku
- Cloudconvert
- Favicon.io
- Am I responsive
- Font Awesome
- Bootstrap5
- Google Fonts
- CI Python Validator
- HTML - W3C HTML Validator
- CSS - Jigsaw CSS Validator
- Javascrpt - JSHint
- TablesGenerator
- Chrome Dev Tools
- Cloudinary
- LightHouse
- Whitenoise
- Django
- Stripe

## Features

### Flow of the Website
The site was designed with the user in mind, and to intuitively guide them from product browsing to actual purchase. The home page greets the users with a carousel of product images complete with links to the products page.

<img src="./documents/images/other/home-page.webp">

The navbar contains links to products, accounts, the shopping bag and an about page.

<img src="./documents/images/other/about-page.webp">

In the products dropdown menu, users can choose to view all the products or by category. The products are displayed on individual cards containing an image, price and button to see more information about the item.

<img src="./documents/images/other/products-pages.webp">

Users will then be brought to the product detail page which contains description, price, reviews, ratings, comments and an option to purchase, or return to browsing.

<img src="./documents/images/other/product-detail.webp">

Upon adding an item to the shopping bag users can checkout by navigating to the shopping bag which will let users see an itemised list of what they have chosen so far.

<img src="./documents/images/other/bag.webp">

Users can then decide to continue shopping, to remove items from the bag or to proceed to a secure checkout. Users can fill out the checkout form and card information to complete their orders. Authenticated users with a primary address in their profile will find the checkout form already prepopulated for them.

<img src="./documents/images/other/checkout.webp">

Upon a successful checkout, users will be shown a checkout success page containing their order details and a confirmation email will also be sent. Authenticated users can revisit this order page through their user profiles.

### Create Account
Users have the ability to create their own accounts if they wish. By creating an account, a user profile is automatically created. Users with accounts can comment on products and provide product ratings and reviews.

<img src="./documents/images/other/create-account.webp">

### User Profiles
Users who have created accounts are automatically provided with user profiles. Here users can save multiple delivery addresses and view previous orders. Users can view their saved addresses and change which one is their primary one to be populated on the checkout form for future purchases. 
Users can also provide feedback about previous orders by filling out the feedback form on the order history card.

<img src="./documents/images/other/profile-page.webp">

<img src="./documents/images/other/address-page.webp">

### Social Interactions
Authenticated users can comment on products in the product detail page. They can also reply to other users comments. Replies to comments are designed to appear indented under the parent comment, to allow users to easily follow a conversation among users in the comments section.

Authenticated Users can also review products and give a star rating on the product detail page also. These star ratings are then gathered to provide an average rating displayed in the product detail card.

<img src="./documents/images/other/comment-review.webp">

### CRUD

Their is extensive CRUD functionality designed throughout the site. Site Owners can edit and delete their products. Users can also delete their own comments and/or replies to other comments if they so wish. They can delete their ratings and reviews. Users can delete their accounts if they wish. They can also edit or delete their saved addresses. 


### Product Management

Site Owners, once authenticated, can manage their products via a form on the front-end. They can edit products or delete them entirely. They can click the product management link to add new products to the site.

<img src="./documents/images/other/product-management.webp">

## Testing

Due to the large size of the testing section, I created a separate file to store all the tests and results. It can be found here [TESTING.md](https://github.com/amy-1989/the-bakery/blob/main/TESTING.md)

## Deployment

The site was deployed to GitHub pages. The steps to deploy are as follows:

- In the GitHub repository, navigate to the Settings tab
- From the source section drop-down menu, select the Main Branch
- Once the main branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment.
- The live link can be found here - [The Bakery live site](https://the-bakery-7e15a3228766.herokuapp.com/)

### Clone the Repository

- Navigate to the GitHub Repository you want to clone to use locally:

- Click on the code drop down button

- Click on HTTPS

- Copy the repository link to the clipboard

- Open your IDE of choice (git must be installed for the next steps)

- Type git clone copied-git-url into the IDE terminal

The project will now of been cloned on your local machine for use.

### Fork the repository

For creating a copy of the repository on your account and change it without affecting the original project, useFork directly from GitHub:

- On My Repository Page, press Fork in the top right of the page

- A forked version of my project will appear in your repository

### Heroku

The project was deployed using Code Institutes mock terminal for Heroku

Deployment steps:

- Fork or clone this repository.

- Ensure the Procfile is in place.

- Create a new app in Heroku

- Select "New" and "Create new app"

- Name the new app and click "Create new app"

- In "Settings" select "BuildPack" and select Python and Node.js. (Python must be at the top of the list)

- Whilst still in "Settings", click "Reveal Config Vars" and input the required hidden variables.

- Click on "Deploy" and select your deploy method and repository

- Click "Connect" on selected repository.

- Either choose "Enable Automatic Deploys" or "Deploy Branch" in the manual deploy section

- Heroku will now deploy the site

## Credits

### Content

- Product content was provided by Rob & Steves Confectioners Ltd.

### Code

- The code in this project was inspired by Code Institutes walkthrough project Boutique Ado
- Inspiration was taken from a previous project for the comment structure.
- Inspiration was also taken from Pyplanes youtube tutorials and Stack Overflow to develop the star rating functionality

### Acknowledgements

- Thank you, as always, to my mentor Narender Singh for his guidance and patience in developing this project.
- Thank you to tutor support for all their help on getting this project functional.
- Thank you to all those on slack who answered my questions at various stages of development.
- Thank you to my family and friends for their extensive testing of the finished site.