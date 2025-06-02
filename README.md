# BlockArt

![ArtBlog Logo](https://res.cloudinary.com/dyemjyefz/image/upload/v1741288631/favicon-32x32_zx3pmg.png)

[View the live project here.]( https://mirjanablog-09220d34d6de.herokuapp.com/)

<img src='https://res.cloudinary.com/dyemjyefz/image/upload/v1741535124/Screenshot_2025-03-09_154028_tstkg9.png'></h2>

#  BlockArt – A Community Blog for Artists

BlockArt is a full-stack blog application built with Django, where visual artists can post, share, and interact with creative content. It’s designed to help users overcome creative blocks by browsing others’ posts, receiving feedback, and maintaining their own digital gallery.

The platform features:
- User authentication and profile management
- Post creation, editing, and deletion (CRUD)
- Like functionality to engage with other artists’ work
- Clean, mobile-friendly interface
- Image hosting via Cloudinary


##  Why Use BlockArt?  

 **Inspiration at Your Fingertips** – Browse unique artwork to spark new ideas.  
 **Showcase Your Art** – Upload your own paintings and share your creativity.  
 **Engaging Community** – Connect with fellow artists and receive valuable feedback.  
 **Easy & Accessible** – Works on all devices, so you can explore anytime, anywhere.  
 **Seamless Image Hosting** – Powered by **Cloudinary**, ensuring high-quality image storage.  

---

 **Join BlockArt today and let your creativity flow!**  

## User Experience (UX)
<hr>

### First-Time Visitors
- Understand the purpose of BlockArt at a glance
- View public art posts without needing to log in
- Register for an account to join the community

### Returning Users
- Log in quickly and access their posts
- Browse recent posts and find inspiration
- Like other users' artwork

### Frequent Users
- Create, edit, and delete their own blog posts
- Update their profile picture
- Explore and engage with new content regularly

##  Agile User Stories

The following user stories were planned and tracked using GitHub Projects during development:

 A full list of issues and progress can be viewed on the [GitHub Project Board](https://github.com/users/mirjanacale/projects/9).


### User Stories Table
| ID  | User Story                                                                            | Status      |
|-----|----------------------------------------------------------------------------------------|-------------|
| US1 | As a new visitor, I want to register so that I can start posting and liking content.  |  Completed |
| US2 | As a user, I want to log in and manage my profile and posts.                          |  Completed |
| US3 | As a user, I want to create blog posts with images.                                   |  Completed |
| US4 | As a user, I want to like or unlike posts.                                            |  Completed |
| US5 | As a user, I want to edit and delete my posts.                                        |  Completed |
| US6 | As a user, I want to upload a profile picture.                                        |  Completed |
| US7 | As a user, I want to reset my password securely.                                      |  Completed |
| US8 | As a user, I want to view other artists’ posts without logging in.                    |  Completed |
| US9 | As a user, I want to receive feedback on my work.                                     |  Completed |
| US13| As a user, I want to comment on other artists’ posts.                                 |  Completed |
| US14| As a user, I want to edit or delete my comments.                                      |  Completed |


### Facebook Page Mockup

To support the marketing aspect of BlockArt, a mock Facebook Business Page has been included.  
While originally designed for my Mollavie e-commerce art store, the branding, artwork, and messaging are consistent with BlockArt, as both platforms represent my personal creative work and visual identity.

This mockup simulates how BlockArt could be promoted through social media to attract a wider artistic audience, share updates, and foster community engagement.



<details>
<summary>Facebook Page Mockup</summary>  

![Facebook Page Mockup](https://res.cloudinary.com/dyemjyefz/image/upload/v1748442920/mockuper_zkfnns.png)
</details>    

- ### Database planning 
<hr>  
  Database Structure     
     
![admin page](https://res.cloudinary.com/dyemjyefz/image/upload/v1748464678/database_ic60sj.png)  
-   ### Design
    -  ##  BlockArt Color Scheme

| Element      | Color Code | Description |
|-------------|------------|-------------|
| **Primary** | `#103E26` | Dark Green (Navbar, Buttons, Highlights) |
| **Background** | `#F5F1EA` | Light Beige (Main Content Area) |
| **Accent** | `#D5C4A1` | Muted Gold (Borders, Cards, Shadows) |
| **Text** | `#2D2D2D` | Deep Charcoal (Headings, Body Text) |
| **Secondary** | `#B0302D` | Rich Red (Icons, Hover Effects) |

This color scheme defines the aesthetic of **BlockArt**, giving it a **classic, vintage, and artistic** look! 


- Images  what are used are from mayself and my dother.

   #### Typography

 -   The fonts used are [Open Sans](https://fonts.google.com/specimen/Open+Sans) and [Lato](https://fonts.google.com/specimen/Lato).
   

  ## Wireframe
***

<details open>
<summary>Wireframe - Homepage  </summary>  

![homepage wireframe-mobile & desktop](https://res.cloudinary.com/dyemjyefz/image/upload/v1741533439/image_3_vlofr4.png)
</details> 
<details >
<summary>Wireframe - About page </summary>  

![homepage wireframe-mobile & desktop](https://res.cloudinary.com/dyemjyefz/image/upload/v1741533439/image_4_xzhwwy.png)
</details> 
<details>
<summary>Wireframe - New Post</summary>  

![homepage wireframe-mobile & desktop](https://res.cloudinary.com/dyemjyefz/image/upload/v1741533439/image_eczdwg.png)
</details>    
<details>
<summary>Wireframe - SignUp page </summary>  

![homepage wireframe-mobile & desktop](https://res.cloudinary.com/dyemjyefz/image/upload/v1741533439/image_5_sv0d3m.png)
</details> 
<details>
<summary>Wireframe - Mobile </summary>  

![homepage wireframe-mobile & desktop](https://res.cloudinary.com/dyemjyefz/image/upload/v1741533439/image_1_nvylgr.png)
</details>              


## Features

## Features

- ### Home Page
- Lists all published blog posts
![home.html](https://res.cloudinary.com/dyemjyefz/image/upload/v1741563565/Screenshot_2025-03-07_205640_nwq4qw.png)


- ### About Page
    - The about page maintains a clean and minimalist design for easy readability. It offers a concise description of the organization’s values and approach.
 ![about.html](https://res.cloudinary.com/dyemjyefz/image/upload/v1741563301/Screenshot_2025-03-07_205721_uajgpw.png)

- ### New Post Page

    - The new post page allows users to create content effortlessly with a simple and clean design. It ensures an easy and intuitive navigation experience for posting new updates.
- ![new_post.html](https://res.cloudinary.com/dyemjyefz/image/upload/v1741563966/Screenshot_2025-03-09_072530_jljphd.png)

- ### Profile Page
    - The profile page showcases a user-friendly interface with a simple and clean layout. It enables users to view and manage their personal information with ease.
- ![profile.html](https://res.cloudinary.com/dyemjyefz/image/upload/v1741564157/Screenshot_2025-03-07_205835_sjavsx.png)

- ###  Login / Logout Page
    - The logout page provides a straightforward, easy-to-navigate design. It ensures that users can exit their session quickly and securely.
- ![login.html](https://res.cloudinary.com/dyemjyefz/image/upload/v1741564441/Screenshot_2025-03-07_205941_bolx7r.png)
- ![logout.html](https://res.cloudinary.com/dyemjyefz/image/upload/v1741564493/Screenshot_2025-03-09_072652_ddfrq9.png)


- ### Register Page
    -   Registered users can view their profile page.
    -   Registered users can view their blog posts.
    -   Registered users can create new blog posts.
    -   Registered users can edit their blog posts.
    -   Registered users can delete their blog posts.
- ![register.html](https://res.cloudinary.com/dyemjyefz/image/upload/v1741564757/Screenshot_2025-03-07_210019_p7kqzq.png)


- ###  Comments Feature
    - egistered users can now leave comments on any post to encourage discussion and community feedback.  
     - Comments display the username, date, and message.
    - Only logged-in users can add comments.
    - The "Add Comment" button matches the site's primary green color for consistent branding.  
     
  
![comments](https://res.cloudinary.com/dyemjyefz/image/upload/v1748626355/coment_bdzqja.png)


## Newsletter Signup

The BlockArt site features a newsletter signup form in the footer section, inviting visitors to subscribe for future updates.

- The form is fully integrated with Django’s CSRF protection for security.
- Users can enter their email address and submit the form.
- At this stage, the form simply redirects users to the homepage after submission.
- Email addresses are not stored or processed further, as this functionality is reserved for a future enhancement.

> **Future Enhancement:**  
> In the next development phase, submitted email addresses could be saved to the database and managed through the Django admin panel, or integrated with a third-party newsletter service.

This implementation demonstrates understanding of Django’s form handling and CSRF security best practices.
![newsletter signup](https://res.cloudinary.com/dyemjyefz/image/upload/v1748882890/Screenshot_2025-06-02_174646_j2oofw.png)


- ## Admin Page
    -   Admin users can view all user profiles.
    -   Admin users can view all blog posts.
    -   Admin users can create new blog posts.
    -   Admin users can edit blog posts.
    -   Admin users can delete blog posts.
![admin page](https://res.cloudinary.com/dyemjyefz/image/upload/v1741563344/Screenshot_2025-03-07_210202_dicsl6.png)



- **Interactive Elements**:

  - **CRUD Operations**: Enables users to leave feedback or insights about their experience with the tool. 
    - Users can post likes after logging in, fostering community engagement and discussions.
    -Likes include success/error messages for transparency.
    ![Comment Success ](https://res.cloudinary.com/dyemjyefz/image/upload/v1741599075/Screenshot_2025-03-07_205540_zyf1eg.png)
   




## Technologies Used

### Languages used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [Javascript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [SQL](https://en.wikipedia.org/wiki/SQL)



### Frameworks, Libraries & Programs Used


- [Git](https://git-scm.com/)
  - Version control.
- [GitHub](https://github.com/)
  - For storing code and deploying the site.
- [Gitpod](https://www.gitpod.io/)
  - Used for building and editing my code.
- [Django](https://www.djangoproject.com/)
  - A python based framework that was used to develop the site.
- [Bootstrap](https://getbootstrap.com/)
  - For help designing the html templates.
- [Google Fonts](https://fonts.google.com/)
  - Used to style the website's logo.
- [Font Awesome](https://fontawesome.com/)
  - Used to obtain the icons used.
- [Google Developer Tools](https://developers.google.com/web/tools/chrome-devtools)
  - Used to help fix problem areas and identify bugs.
- [Cloudinary](https://cloudinary.com/)
  - Used to store static files and images.
- [Favicon.io](https://favicon.io/)
  - Used to generate the site's favicon.
- [SQlite](https://www.sqlite.org/index.html)
  - Used when performing unit tests.
- [PostgreSQL](https://www.postgresql.org/)
  - Database used through heroku.
- [Lucidchart](https://www.lucidchart.com/)
  - To draw out the database schema.
- [W3C Markup Validation Service](https://validator.w3.org/) 
  - Used to validate HTML code.
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/#validate_by_input)
- Used to validate CSS code.
- [Pep8](http://pep8online.com/)
  - Used to validate Python code.
- [JSHint](https://jshint.com/)
  - Used to validate JS code.
- [Tinyjpg](https://tinyjpg.com/)
  - Used to compress images.
- [Convertio](https://convertio.co/)
  - To convert images to a webp format(better performance)
- [Heroku](https://www.heroku.com/)
  - To deploy the project.
- [ChatGPT](https://chatgpt.com/)
  - Used for general queries and quick help.
- [Claude3.5](https://claude.ai/)
  - For insightful explanations of topic. 
- [ YouTube](https://www.youtube.com/) 
  - For tutorials and other learnigs.



## Validators

- HTML
    - Results of HTML official[W3C validator] (https://validator.w3.org/).

    <hr>

| File         | Preview |
|-------------|---------|
| `base.html`  | ![base.html](https://res.cloudinary.com/dyemjyefz/image/upload/v1747918081/base.htmlval_m8grrz.png) |
| `about.html`   | ![about.html](https://res.cloudinary.com/dyemjyefz/image/upload/v1747918044/about.htmlval_jqz3oq.png) |
| `edit_profile.html`   | ![edit_profile.html](https://res.cloudinary.com/dyemjyefz/image/upload/v1747918066/editprofileval_kp2qvl.png) |
| `signup.html`  | ![signup.html](https://res.cloudinary.com/dyemjyefz/image/upload/v1747918071/signup.html_nmohsf.png) |
| `index.html` | ![index.html](https://res.cloudinary.com/dyemjyefz/image/upload/v1747918052/index.htmlval_fgkwsq.png) |
| `login.html`  | ![login.html](https://res.cloudinary.com/dyemjyefz/image/upload/v1747918091/login.html_val_euy3fk.png) |
| `logout.html`  | ![logout.html](https://res.cloudinary.com/dyemjyefz/image/upload/v1747918748/logout.htmlval_vlrqpx.png) |
| `post_detail.html`  | ![post_detail.html](https://res.cloudinary.com/dyemjyefz/image/upload/v1747921382/post_detailval_c8kjk4.png)
##  HTML Validation

All HTML files were tested using the [W3C Markup Validation Service](https://validator.w3.org/). The results are as follows:

| Page                   | Valid | Errors | Warnings |
|------------------------|:-----:|:------:|:--------:|
| Home                   |    |   0    |    0     |
| About                  |    |   0    |    0     |
| Profile                |    |   0    |    0     |
| Register               |    |   0    |    0     |
| Admin                  |    |   0    |    0     |
| Password Reset         |    |   0    |    0     |
| Login                  |    |   0    |    0     |
| Logout                 |    |   0    |    0     |


  <hr> 

  ##  Custom Error Pages

The BlockArt project includes fully custom-designed error pages to ensure a smooth and branded user experience, even during failures.

### Implemented Errors:

| Code | Description            |
|------|------------------------|
| 403  | Forbidden              |
| 404  | Page Not Found         |
| 500  | Internal Server Error  |

Each template extends the base layout, uses consistent colors and styling, and includes helpful messages and navigation.

---

###  Examples

#### 404 – Page Not Found  
When a user accesses a missing page:

![404 Error Page](https://res.cloudinary.com/dyemjyefz/image/upload/v1746998155/Screenshot_2025-05-11_210413_biezbh.png)

#### 403 – Forbidden  
When permission is denied (e.g., accessing someone else's post):

![403 Error Page](https://res.cloudinary.com/dyemjyefz/image/upload/v1746997795/Screenshot_2025-05-11_213306_xzhvba.png)

#### 500 – Server Error  
When something unexpected crashes:

![500 Error Page](https://res.cloudinary.com/dyemjyefz/image/upload/v1746997787/Screenshot_2025-05-11_210057_miztfh.png)

---

###  Testing Summary

Error templates were tested locally using debug routes and `DEBUG = False`. After verification, test routes were removed from the project before final deployment.

All error templates are stored in:
 
---
- CSS 
     - No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/) validator.

    ![CSS Validator ](https://res.cloudinary.com/dyemjyefz/image/upload/v1741565382/css_o3tf14.png)


---


- JavaScript
  
This project does not include any custom JavaScript code.
All dynamic or interactive functionality is handled by external libraries (such as Bootstrap) via CDN links in the template files.

As a result, no custom JavaScript files needed to be validated with JSHint.

---
- Python
    - No errors were found when passing through [CI Python Linter](https://pep8ci.herokuapp.com/#)validator.

[CI Python Linter](https://pep8ci.herokuapp.com/#)
 was used to validate the Python files . No issues presented and line length was kept under 80 characters.



---

| File         | Preview |
|-------------|---------|
| `urls.py`   | ![URLS.PY](https://res.cloudinary.com/dyemjyefz/image/upload/v1741566794/urls.py_e1lx17.png) |
| `wsgi.py`   | ![WSG.PY](https://res.cloudinary.com/dyemjyefz/image/upload/v1741566833/wsg.py_vcqwmu.png) |
| `apps.py`   | ![APPS.PY](https://res.cloudinary.com/dyemjyefz/image/upload/v1741566829/users.apps.py_bdkctn.png) |
| `views.py`  | ![VIEWS.PY](https://res.cloudinary.com/dyemjyefz/image/upload/v1741566824/users_views.py_mdpmj5.png) |
| `models.py` | ![MODELS.PY](https://res.cloudinary.com/dyemjyefz/image/upload/v1741566817/users_models.py_dlara9.png) |
| `forms.py`  | ![FORMS.PY](https://res.cloudinary.com/dyemjyefz/image/upload/v1741566807/users_forms.py_ljefcv.png) |
| `manage.py` | ![MANAGE.PY](https://res.cloudinary.com/dyemjyefz/image/upload/v1741566802/user.manage.py_ovewls.png) |


---

### Lighthouse Scores

Lighthouse testing was carried out using the [Chrome DevTools](https://developers.google.com/web/tools/lighthouse/).

--- 

| File         | Preview |
|-------------|---------|
| PERFORMANCE | ![URLS.PY](https://res.cloudinary.com/dyemjyefz/image/upload/v1741570316/lihthous4_jjmksz.png) |
| ACCESSIBILITY   | ![WSG.PY](https://res.cloudinary.com/dyemjyefz/image/upload/v1741570332/lihthous5_d5yeuu.png) |
| BEST PRACTICES  | ![APPS.PY](https://res.cloudinary.com/dyemjyefz/image/upload/v1741570337/lihthous1_yvrbyk.png) |
| DIAGNOSTICS | ![VIEWS.PY](https://res.cloudinary.com/dyemjyefz/image/upload/v1741570347/lihthous6_w3ak8u.png) |



<hr>  

### Manual Testing

| Feature               | Test Steps                                              | Expected Result                                         | Actual Result | Pass/Fail | Bug/Notes |
|-----------------------|---------------------------------------------------------|----------------------------------------------------------|---------------|-----------|-----------|
| Register New Account  | Go to /register/, fill in form and submit               | Redirect to login, success message displayed             |               |       pass    |           |
| Login                 | Go to /login/, enter correct credentials                | Redirect to homepage, welcome message shown              |               |    pass       |           |
| Logout                | Click Logout button from navbar                         | Redirect to homepage, user logged out                    |               |   pass        |           |
| View Homepage         | Visit / and check if posts are displayed                | Homepage shows list of posts                             |               |    pass       |           |
| View Single Post      | Click a post title from homepage                        | Post detail view shows title, image, content             |               |   pass        |           |
| Create Blog Post      | Click 'New Post', submit a new post form                | New post appears on homepage                             |               |    pass       |           |
| Edit Blog Post        | Click 'Update' on a post and submit changes             | Post updates and shows changed content                   |               |    pass       |           |
| Delete Blog Post      | Click 'Delete' on a post and confirm                    | Post no longer appears                                   |               |    pass       |           |
| Like/Unlike Post      | Click 'Like' or 'Unlike' button under a post            | Like count increases/decreases                           |               |     pass      |           |
| View Profile          | Click 'Profile' in navbar                               | Profile info shown, including image and email            |               |    pass       |           |
| Update Profile Info   | Update username or profile image and submit             | Profile changes are saved and shown                      |               |    pass       |           |
| Password Reset        | Request password reset and follow email link           | Password reset email sent and flow works                 |               |   pass        |           |
| Error 404 Page        | Visit a non-existent URL like /doesnotexist/           | 404 page is displayed                                    |               |  pass         |           |
| Error 403 Page        | Try restricted page without permissions                | 403 page is displayed                                    |               |   pass        |           |
| Error 500 Page        | Simulate server error (e.g., raise error in view)       | 500 error page shown with custom template                |               |   pass        |           |


  
 ---  

### Testing User Stories from User Experience (UX) Section

##  UX Testing Based on User Stories

The following user goals were identified and tested to ensure a smooth experience across different user types.

---

### 🔹 First-Time Visitor Goals

**Goal:** Understand the site's purpose  
-  The home page explains that BlockArt is a space for artists to share their work. The title, tagline, and sample posts are visible without logging in.

**Goal:** Navigate easily  
-  A clean navigation bar is present on every page. All main routes (Home, Register, Login, About) are clearly labeled and accessible.

**Goal:** View content without logging in  
- Posts from other users are visible on the home page even if not logged in.

---

### 🔹 Returning Visitor Goals

**Goal:** Log in and manage posts  
-  A registered user can log in, access the profile page, view their own posts, and create or update new ones.

**Goal:** Browse new content  
-  The home page shows the latest posts sorted by creation date.

---

### 🔹 Frequent User Goals

**Goal:** Create new posts  
-  Authenticated users can create blog posts via a simple form with validation and image upload.

**Goal:** Like posts and engage  
-  Users can like and unlike posts. The like count updates correctly. Messages appear confirming the action.

**Goal:** Update profile  
-  Users can update their profile image. The change is saved and displayed throughout the site.

<hr>



### Further Testing

-   The blog was tested on Google Chrome, Internet Explorer, Microsoft Edge and Safari browsers.
-   The blog was viewed on a variety of devices such as Desktop, Laptop, iPhone7, iPhone 8 & iPhoneX.
-   A large amount of testing was done to ensure that all pages were linking correctly.
-   Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

## Bugs fixed

---


 - fix: disable SMTP and enforce console email backend to prevent connection errors
 - fix: Removed SMTP settings to avoid WinError 10061 and ensured console email backend is used for password reset in local testing.

 PASSWORD RESET   
     ![APPS.PY](https://res.cloudinary.com/dyemjyefz/image/upload/v1741570443/Screenshot_2025-03-07_210331_zuzeq2.png) 


 PASSWORD RESET     
   ![VIEWS.PY](https://res.cloudinary.com/dyemjyefz/image/upload/v1746829065/Screenshot_2025-05-09_225405_ppff57.png) h


---

##  Future Features

The following features are not part of the current MVP but are planned for future development:

- **Comments on posts**  
  Users will be able to leave comments under each post to offer feedback or discuss artwork.

- **User following**  
  Users will be able to follow their favorite artists and see their latest posts in a dedicated feed.

- **Search functionality**  
  Add a search bar to find posts by keywords, titles, or artist names.

- **Trending posts**  
  Display posts with the most likes in a separate section for popular content.

- **Bookmark posts**  
  Users can save favorite posts to view later from their profile.

- **Report content**  
  Allow users to report inappropriate or abusive content, which can be reviewed by an admin.

- **Tags and filters**  
  Posts can be organized by tags or categories for easier discovery.

## Manual Testing Summary

All forms and CRUD features were manually tested on the live site using both valid and invalid data. Scenarios included registering with existing usernames, invalid emails, weak or mismatched passwords, logging in with incorrect credentials, creating, editing, and deleting posts with missing fields, and ensuring users cannot delete posts they do not own. In all cases, the site displayed proper validation messages and handled errors gracefully, with no unexpected server errors or 500 responses.

## Test Cases
The following test cases were executed to ensure the functionality of the BlockArt blog application. Each test case includes the feature being tested, the specific test case, the expected result, the actual result, and whether it passed or failed.

| Feature        | Test Case                          | Expected Result                | Actual Result    | Pass/Fail |
| -------------- | ---------------------------------- | ------------------------------ | --------------- | --------- |
| Registration   | Valid data                         | User registered, redirect      | As expected     | Pass      |
| Registration   | Existing username                  | Error message shown            | As expected     | Pass      |
| Registration   | Invalid email                      | Error message shown            | As expected     | Pass      |
| Registration   | Weak/mismatched passwords          | Error message shown            | As expected     | Pass      |
| Login          | Valid credentials                  | User logged in, redirect       | As expected     | Pass      |
| Login          | Wrong credentials                  | Error message shown            | As expected     | Pass      |
| Create Post    | Valid data                         | Post appears on homepage       | As expected     | Pass      |
| Create Post    | Missing fields                     | Form error message             | As expected     | Pass      |
| Edit Post      | Update post data                   | Changes saved and displayed    | As expected     | Pass      |
| Delete Post    | Delete own post                    | Post removed                   | As expected     | Pass      |
| Delete Post    | Try to delete another user’s post  | 403 Forbidden or not allowed   | As expected     | Pass      |




## Deployment
This project utilizes [Heroku](http://heroku.com) , for deployment, allowing developers to build, run, and manage applications in the cloud.
Follow these steps to deploy the ArtBlog on Heroku:

1. Create a New Heroku App
- Log in to Heroku or sign up for a new account.
- Navigate to your Heroku dashboard and click on the "New" button.
- Select "Create new app" from the dropdown menu.
- Choose a unique name for your app, select a region (EU or USA), and click "Create app".
2. Configure Environment Variables
- In your app's settings, navigate to the "Config Vars" section.
- Click on "Reveal Config Vars" and add the following variables:
  - PORT: Set the value to 8000.
  - Any other confidential credentials or configuration settings required by the blog.
3. Add Buildpacks
- In the "Buildpacks" section, add the following buildpacks in the specified order:
  - Python
  - Node.js
4. Prepare Required Files
- Ensure your project includes the following files:
  - requirements.txt: Contains the project's Python dependencies.
  - Procfile: Specifies the commands to run the app.
5. Connect GitHub Repository

- Under the "Deploy" tab, select "GitHub" as the deployment method.
- Connect your GitHub repository to the Heroku app.
- Enable automatic deploys for continuous deployment.
6. Deploy Your App
- Trigger a manual deployment by clicking "Deploy Branch" or wait for automatic deployments to occur.
- Once deployed successfully, your blog will be accessible via the provided Heroku URL.




## Deployment

The site was deployed to GitHub Pages. The steps to deploy are as follows:

- In the [GitHub repository](https://github.com/mirjanacale/BlockArt), navigate to the Settings tab
- From the source section drop-down menu, select the **Main** Branch, then click "Save".
- The page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment.

The live link can be found [here](https://mirjanablog-09220d34d6de.herokuapp.com/)

### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/mirjanacale/BlockArt)
2. Locate the Code button above the list of files and click it
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
   - `git clone https://github.com/mirjanacale/.git`
7. Press Enter to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/mirjanacale//)

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed.
A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://mirjanacale.github.io//)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

### Local VS Deployment

There are no major differences between the local (Gitpod) version and the deployed (GitHub Pages) version that I'm aware of.

## Contributing
Contributions are welcome! If you have suggestions for new questions or improvements to the blog, please feel free to open an issue .
