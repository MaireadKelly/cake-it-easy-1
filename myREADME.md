Cake it Easy
Cake it Easy is an e-commerce website for a custom occasion cake shop. Customers can browse through a variety of cakes, place orders with custom inscriptions, leave comments, and rate the cakes they've purchased.

<!-- [View the live project here.](#) -->
<!-- Replace '#' with the link to your image -->

User Experience (UX)
User Stories
To be filled later with specific user stories.

Technologies Used
Languages Used
Python 3: Used for backend development with Django.
HTML5: For structuring the web pages.
CSS3: For styling the web pages.
JavaScript: If applicable, for interactive elements on the frontend.
Frameworks, Libraries & Programs Used
Django 3.2.25: The main Python web framework used to build the backend of the application.

Django Allauth 0.51.0: Used for user authentication, registration, and account management.

Pillow 10.4.0: A Python Imaging Library used for handling image uploads for cakes.

asgiref 3.8.1: Asynchronous Server Gateway Interface reference implementation, required by Django.

sqlparse 0.5.1: A non-validating SQL parser used by Django.

Bootstrap (Version 5.2.3): Used for responsive design and styling.

SQLite3: Used as the development database.

Git: For version control.

GitHub: For hosting the project's repository.

Visual Studio Code / Code Institute's IDE: Used as the development environment.

Cloudinary: (If applicable) For hosting media files like images.

Third-Party Packages
Listed in requirements.txt:

asgiref==3.8.1
Django==5.1.2
django-allauth==65.0.2
pillow==10.4.0
pytz==2024.2
sqlparse==0.5.1
Features
Existing Features
User Authentication and Profiles

Registration and Login: Users can create an account, log in, and log out securely using Django Allauth.
Profile Management: Users have a profile (Customer model) where additional information like address and phone number is stored.
Previous Orders: Users can view their previous orders through their profile.
Product Management

Cake Catalog: A list of cakes (Cake model) with details such as name, description, price, image, category, and available stock.
Categories: Cakes are categorized by occasions like Wedding, Birthday, Anniversary, etc.
Dynamic Slug Generation: Unique slugs are automatically generated for each cake for clean URLs.
Ordering System

Order Placement: Users can place orders for cakes, specifying quantity and custom inscriptions.
Price Calculation: The total price is automatically calculated based on the cake price and quantity.
Order Status: Orders have statuses like Pending, Shipped, and Delivered.
Delivery Time: Users can select a desired delivery date and time using a calendar input.
Comments and Reviews

Comments: Users can leave comments on cakes they've purchased.
Comments Administration: Comments are registered in the admin panel for moderation if needed.
Rating System

Star Ratings: Users can rate cakes on a scale of 1 to 5.
Validation: Ensures ratings are within the specified range.
Responsive Design

Bootstrap Integration: The site uses Bootstrap for a responsive and mobile-friendly design.
Features Left to Implement
Stripe Integration

Payment Processing: Implementing Stripe to handle secure payments.
Guest Checkout

Purchasing Without Registration: Allowing users to make purchases without creating an account.
Enhanced Rating Display

Average Ratings: Displaying average star ratings on cake listings.
Delivery Address Option

Order-specific Address: Adding an option to specify a delivery address for each order.
User Interface Improvements

Header and Navbar Redesign: Modifying the layout for better navigation and aesthetics.
Hover Effects and Animations: Adding interactive elements for improved UX.
Backlog Features for Next Iteration

Star Rating Feature: Implementing a visual star rating system.
Newsletter Signup: Adding a feature for users to subscribe to a newsletter.
SEO Enhancements: Adding meta tags, robots.txt, and sitemap.xml.
Technologies Used
(Repeated section—this can be removed if preferred, or we can combine the two sections.)

Testing
Validation
W3C Markup Validator: Used to validate HTML files.
W3C CSS Validator: Used to validate CSS files.
PEP8 Compliance: Ensuring Python code follows PEP8 style guidelines.
User Story Testing
To be filled with specific user stories and how each was tested.

Further Testing
Cross-Browser Compatibility: Tested on modern browsers like Chrome, Firefox, Safari, and Edge.
Responsive Design Testing: Ensured the site is responsive on various devices and screen sizes.
Functionality Testing: Tested all forms, links, and interactive features to ensure they work as intended.
Known Bugs
No known bugs at this time.
Deployment
Local Deployment
To run this project locally:

Clone the Repository

bash
Copy code
git clone https://github.com/yourusername/cake-it-easy.git
Install Dependencies

Navigate to the project directory and install the required packages:

Copy code
pip install -r requirements.txt
Set Up Environment Variables

Create a .env file in the root directory.
Add your SECRET_KEY and any other necessary environment variables.
Apply Migrations

Copy code
python manage.py migrate
Create a Superuser

Copy code
python manage.py createsuperuser
Run the Server

Copy code
python manage.py runserver
Heroku Deployment
Deployment instructions for Heroku or your chosen hosting platform can be added here once the project is live.

Credits
Code
Django Documentation: For guidance on models, views, and templates.
Django Allauth Documentation: For setting up authentication.
Bootstrap Documentation: For frontend components and responsive design.
Content
All content was created by the developer.
Media
Images: Placeholder images used during development are sourced from Unsplash or created by the developer.
Acknowledgements
Mentor: For continuous support and guidance.
Code Institute: For the sample README template and educational resources.
Stack Overflow Community: For solutions to specific coding challenges.