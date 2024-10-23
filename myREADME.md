# **Cake it Easy**

*Cake it Easy* is an e-commerce website for a custom occasion cake shop. Customers can browse through a variety of cakes, place orders with custom inscriptions, leave comments, and rate the cakes they've purchased.

<!-- [View the live project here.](#) -->

![Cake it Easy Mockup](#) <!-- Replace '#' with the link to your image -->

## **User Experience (UX)**

### **User Stories**

#### **First Time Visitor Goals**

1. **As a First Time Visitor, I want to easily understand the main purpose of the site and learn about the products offered.**
   - Upon entering the site, users are greeted with a welcoming hero section that highlights the site's purpose and offers a clear call-to-action button to "Shop Now".

2. **As a First Time Visitor, I want to navigate through the site effortlessly to find cakes suitable for my occasion.**
   - The navigation bar provides links to "Home", "Our Story", and "Shop Now", making it easy to explore the site.

3. **As a First Time Visitor, I want to be able to register an account to place orders.**
   - Users can access the "Login / Register" option in the header to create a new account.

#### **Returning Visitor Goals**

1. **As a Returning Visitor, I want to log in to my account quickly.**
   - The "Login / Register" button allows returning users to access their accounts easily.

2. **As a Returning Visitor, I want to view and manage my previous orders.**
   - Users can view their order history through their customer profile page.

3. **As a Returning Visitor, I want to leave comments and ratings on cakes I've purchased.**
   - Users can add comments and ratings to cakes, sharing their experiences with others.

#### **Frequent User Goals**

1. **As a Frequent User, I want to stay updated on new cake offerings and promotions.**
   - The homepage features sections like "Featured Cakes" and a newsletter subscription form in the footer.

2. **As a Frequent User, I want to quickly access the shopping cart and proceed to checkout.**
   - The shopping cart icon is readily accessible in the header with the current total displayed.

3. **As a Frequent User, I want to search for specific cakes or categories.**
   - The search bar in the header allows users to search for cakes by name or category.

### **Design**

- **Colour Scheme**
  - The website uses a warm and inviting color palette, featuring pastel colors that evoke a sense of sweetness and celebration.

- **Typography**
  - The site uses elegant and legible fonts to enhance readability and match the aesthetic of a cake shop. Fonts are consistent across the site for a cohesive look.

- **Imagery**
  - High-quality images of cakes are used throughout the site to showcase products and entice customers.

### **Wireframes**

- Home Page Wireframe - [View](#) <!-- Replace '#' with your wireframe link -->
- Mobile Wireframe - [View](#)
- Cake List Page Wireframe - [View](#)
- Order Form Wireframe - [View](#)

---

## **Features**

### **Existing Features**

1. **Responsive Navigation Bar**
   - Located at the top of the page, the navigation bar includes links to "Home", "Our Story", and "Shop Now" on the left, a search bar in the center, and "Login / Register" and the shopping cart on the right.
   - The navigation bar is fully responsive and collapses into a hamburger menu on smaller screens.

2. **Homepage Hero Section**
   - Features a welcoming message with the site's tagline: "Delicious cakes made to perfection for every occasion."
   - Includes a prominent "Shop Now" button that directs users to the cake catalog.

3. **Featured Cakes Section**
   - Displays a selection of featured cakes with images, names, descriptions, and links to view more details.
   - Helps to showcase popular or new products.

4. **About Us Section**
   - Provides a brief introduction to the business with the message: "Cake it Easy baking sweet memories to last a lifetime..."
   - Builds trust and connects with customers by sharing the brand's story.

5. **Footer**
   - Contains important links like "About Us", "Contact", "Terms of Service", and "Privacy Policy".
   - Includes social media icons linking to Facebook, Twitter, Instagram, and Pinterest.
   - Features a newsletter subscription form for users to stay updated.

6. **Customer Profile Page**
   - Users can view their profile information, including address and phone number.
   - Displays previous orders associated with the customer.

7. **Cake Catalog (`cake_list` View)**
   - Users can browse all available cakes.
   - Each cake displays an image, name, price, and a link to view more details.

8. **Order Creation (`order_create` View)**
   - Users can place orders for cakes, specifying quantity and custom inscriptions.
   - Delivery time can be selected using a calendar input.

9. **Comments and Ratings**
   - Users can add comments and ratings to cakes.
   - Helps build a community and provides feedback for other customers.

10. **Search Functionality**
    - The search bar allows users to find cakes by name or category.

11. **Shopping Cart**
    - Accessible from the header, displaying the total amount.
    - Users can view items in their cart and proceed to checkout.

### **Features Left to Implement**

1. **Basket and Checkout Apps**
   - **Basket Functionality**: Allow users to add cakes to a basket and adjust quantities before checkout.
   - **Checkout Process**: Streamlined process for users to enter payment and delivery details.

2. **Stripe Integration**
   - **Payment Processing**: Securely handle online payments through Stripe.

3. **Guest Checkout**
   - **Purchase Without Registration**: Enable users to place orders without creating an account.

4. **Enhanced Product Filtering**
   - **Occasion Categories**: Allow users to filter cakes based on occasions like Wedding, Birthday, etc.

5. **Improved User Profile Management**
   - **Edit Profile**: Users can update their personal information and address.

6. **Order Tracking**
   - **Order Status Updates**: Users can track the status of their orders from their profile.

7. **Responsive Design Enhancements**
   - **Mobile Optimization**: Ensure all pages and features are fully optimized for mobile devices.

8. **Custom 404 Error Page**
   - Provide a user-friendly error page for non-existent routes.

9. **SEO Enhancements**
   - Add meta tags, `robots.txt`, and `sitemap.xml` for better search engine indexing.

10. **Accessibility Improvements**
    - Ensure the site meets WCAG accessibility guidelines.

---

## **Technologies Used**

### **Languages Used**

- **Python 3**
- **HTML5**
- **CSS3**
- **JavaScript**

### **Frameworks, Libraries & Programs Used**

1. **Django 3.2.25**
   - The main web framework used for backend development.

2. **Django Allauth**
   - For user authentication and account management.

3. **Bootstrap 5.2.3**
   - Used for responsive design and styling.

4. **Pillow 10.4.0**
   - For handling image uploads.

5. **SQLite3**
   - Used as the development database.

6. **Git & GitHub**
   - For version control and repository hosting.

7. **Visual Studio Code / Code Institute's IDE**
   - Development environment.

8. **Font Awesome & Bootstrap Icons**
   - For icons used in navigation and other UI elements.

9. **Cloudinary** (if applicable)
   - For media storage and management.

---

## **Testing**

### **Validation**

- **HTML Validation**
  - Used the W3C Markup Validation Service to check HTML files for errors.

- **CSS Validation**
  - Used the W3C CSS Validation Service to ensure CSS files are error-free.

- **Python Code Validation**
  - Ensured PEP8 compliance using tools like Flake8.

### **Testing User Stories from User Experience (UX) Section**

#### **First Time Visitor Goals**

1. **Understanding the site's purpose**
   - Tested that the homepage clearly communicates the site's purpose with a welcoming hero section and tagline.

2. **Easy Navigation**
   - Verified that all navigation links work correctly and that the site is responsive on various devices.

3. **Account Registration**
   - Tested the registration process to ensure users can create accounts without issues.

#### **Returning Visitor Goals**

1. **Logging In**
   - Confirmed that existing users can log in and are redirected appropriately.

2. **Viewing Previous Orders**
   - Checked that the customer profile page displays past orders.

3. **Adding Comments and Ratings**
   - Ensured that logged-in users can add comments and ratings to cakes.

#### **Frequent User Goals**

1. **Staying Updated**
   - Verified that the newsletter subscription form works and that featured cakes are updated.

2. **Accessing Shopping Cart**
   - Tested that the shopping cart icon displays the correct total and links to the cart page.

3. **Using the Search Bar**
   - Confirmed that the search functionality returns relevant results.

### **Further Testing**

- **Browser Compatibility**
  - Tested the site on Chrome, Firefox, Safari, and Edge.

- **Responsive Design**
  - Ensured the site looks good and functions well on desktop, tablet, and mobile devices.

- **Link and Form Testing**
  - Checked all internal and external links, ensuring they work correctly and open in the appropriate tabs.

---

## **Deployment**

### **Local Deployment**

To run this project locally:

1. **Clone the Repository**


