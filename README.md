# ArtBlog

![ArtBlog Logo](https://res.cloudinary.com/dyemjyefz/image/upload/v1741288631/favicon-32x32_zx3pmg.png)

[View the live project here.]( https://mirjanablog-09220d34d6de.herokuapp.com/)

<img src='https://res.cloudinary.com/dyemjyefz/image/upload/v1741535124/Screenshot_2025-03-09_154028_tstkg9.png'></h2>

# 🎨 BlockArt – A Community Blog for Artists

BlockArt is a full-stack blog application built with Django, where visual artists can post, share, and interact with creative content. It’s designed to help users overcome creative blocks by browsing others’ posts, receiving feedback, and maintaining their own digital gallery.

The platform features:
- User authentication and profile management
- Post creation, editing, and deletion (CRUD)
- Like functionality to engage with other artists’ work
- Clean, mobile-friendly interface
- Image hosting via Cloudinary


## 🌟 Why Use ArtBlock?  

✅ **Inspiration at Your Fingertips** – Browse unique artwork to spark new ideas.  
✅ **Showcase Your Art** – Upload your own paintings and share your creativity.  
✅ **Engaging Community** – Connect with fellow artists and receive valuable feedback.  
✅ **Easy & Accessible** – Works on all devices, so you can explore anytime, anywhere.  
✅ **Seamless Image Hosting** – Powered by **Cloudinary**, ensuring high-quality image storage.  

---

 **Join ArtBlock today and let your creativity flow!**  

## User Experience (UX)
<hr>

### First-Time Visitors
- Understand the purpose of ArtBlock at a glance
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


 
- ### Database planning 
<hr>  
  Database Structure     
     
![admin page](https://res.cloudinary.com/dyemjyefz/image/upload/v1741597522/Screenshot_2025-03-10_085828_o4tgp0.png)  
-   ### Design
    -  ## 🎨 ArtBlog Color Scheme

| Element      | Color Code | Description |
|-------------|------------|-------------|
| **Primary** | `#103E26` | Dark Green (Navbar, Buttons, Highlights) |
| **Background** | `#F5F1EA` | Light Beige (Main Content Area) |
| **Accent** | `#D5C4A1` | Muted Gold (Borders, Cards, Shadows) |
| **Text** | `#2D2D2D` | Deep Charcoal (Headings, Body Text) |
| **Secondary** | `#B0302D` | Rich Red (Icons, Hover Effects) |

This color scheme defines the aesthetic of **ArtBlog**, giving it a **classic, vintage, and artistic** look! 🎨✨


- Images  what are used are from mayself and my dother.

   #### Typography

 -   The fonts used are [Open Sans](https://fonts.google.com/specimen/Open+Sans) and [Lato](https://fonts.google.com/specimen/Lato).
   

*  ## Wireframe
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
- ![about.html](https://res.cloudinary.com/dyemjyefz/image/upload/v1741563301/Screenshot_2025-03-07_205721_uajgpw.png)

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
| `base.html`  | ![base.html](https://res.cloudinary.com/dyemjyefz/image/upload/v1741599020/base.html_wug6vn.png) |
| `about.html`   | ![about.html](https://res.cloudinary.com/dyemjyefz/image/upload/v1741599016/about.html_jpz6b9.png) |
| `post confirm delete.html`   | ![post_confirm_delete.html](https://res.cloudinary.com/dyemjyefz/image/upload/v1741599034/p_c_delete.html_rfk5mt.png) |
| `post detail.html`  | ![post_detail.html](https://res.cloudinary.com/dyemjyefz/image/upload/v1741599039/post_dital.html_ibqpmy.png) |
| `post form.html` | ![post_form.html](https://res.cloudinary.com/dyemjyefz/image/upload/v1741599044/post_form.html_fcg0th.png) |
| `password_reset_complete.html`  | ![password_reset_complete.html](https://res.cloudinary.com/dyemjyefz/image/upload/v1741599044/post_form.html_fcg0th.png) |




      ![HTML Validator]()

    | HTML Source Code/Page | Pass | Errors| Warnings
    | ---- | ------ | -------- | -------- |
    | Home | Yes | 0 |0
    | About | Yes | 0 |0
    | Profile| Yes | 0 |0
    | Register | Yes | 0 |0
    | Admin | Yes | 0 |0
    | Password Reset | No | 0 |0
    | Log In | Yes| 0 |0
    | Logout | Yes | 0 |0
    | Register | Yes | 0 |0
    | Error 403 | Yes | 0 |0
    | Error 404 | Yes | 0 |0
    | Error 500 |  | 0 |0

  <hr>  

- CSS 
     - No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/) validator.

    ![CSS Validator ](https://res.cloudinary.com/dyemjyefz/image/upload/v1741565382/css_o3tf14.png)

- JavaScript
    - errors were found when passing through the   [Jshint](https://jshint.com/) validator.

    ![js](https://res.cloudinary.com/dyemjyefz/image/upload/v1741566255/js_g7u24v.png)

- Python
    - No errors were found when passing through [CI Python Linter](https://pep8ci.herokuapp.com/#)validator.

[CI Python Linter](https://pep8ci.herokuapp.com/#)
 was used to validate the Python files . No issues presented and line length was kept under 80 characters.


|
<hr>

| File         | Preview |
|-------------|---------|
| `urls.py`   | ![URLS.PY](https://res.cloudinary.com/dyemjyefz/image/upload/v1741566794/urls.py_e1lx17.png) |
| `wsgi.py`   | ![WSG.PY](https://res.cloudinary.com/dyemjyefz/image/upload/v1741566833/wsg.py_vcqwmu.png) |
| `apps.py`   | ![APPS.PY](https://res.cloudinary.com/dyemjyefz/image/upload/v1741566829/users.apps.py_bdkctn.png) |
| `views.py`  | ![VIEWS.PY](https://res.cloudinary.com/dyemjyefz/image/upload/v1741566824/users_views.py_mdpmj5.png) |
| `models.py` | ![MODELS.PY](https://res.cloudinary.com/dyemjyefz/image/upload/v1741566817/users_models.py_dlara9.png) |
| `forms.py`  | ![FORMS.PY](https://res.cloudinary.com/dyemjyefz/image/upload/v1741566807/users_forms.py_ljefcv.png) |
| `manage.py` | ![MANAGE.PY](https://res.cloudinary.com/dyemjyefz/image/upload/v1741566802/user.manage.py_ovewls.png) |

### Lighthouse Scores

Lighthouse testing was carried out using the [Chrome DevTools](https://developers.google.com/web/tools/lighthouse/).


| File         | Preview |
|-------------|---------|
| PERFORMANCE | ![URLS.PY](https://res.cloudinary.com/dyemjyefz/image/upload/v1741570316/lihthous4_jjmksz.png) |
| ACCESSIBILITY   | ![WSG.PY](https://res.cloudinary.com/dyemjyefz/image/upload/v1741570332/lihthous5_d5yeuu.png) |
| BEST PRACTICES  | ![APPS.PY](https://res.cloudinary.com/dyemjyefz/image/upload/v1741570337/lihthous1_yvrbyk.png) |
| DIAGNOSTICS | ![VIEWS.PY](https://res.cloudinary.com/dyemjyefz/image/upload/v1741570347/lihthous6_w3ak8u.png) |



<hr>  

  
   

### Testing User Stories from User Experience (UX) Section

-   #### First Time Visitor Goals

 1. As a First Time Visitor, I want to easily understand the main purpose of the site and learn more about the an organisation.

 1. The blog has been designed to be informative and easy to navigate. The main purpose of the site is to help the organisation understand what they do and how they do it better.

 2. As a First Time Visitor, I want to be able to easily be able to navigate throughout the site to find content.

 1. The blog has been designed to be fluid and never to entrap the user. At the top of each page there is a clean navigation bar, each link describes what the page they will end up at clearly.
 2. At the bottom of the first 2 pages there is a redirection call to action to ensure the user always has somewhere to go and doesn't feel trapped as they get to the bottom of the page.
 3. On the Contact Us Page, after a form response is submitted, the page refreshes and the user is brought to the top of the page where the navigation bar is.

 3. As a First Time Visitor, I want to look for testimonials to understand what their users think of them and see if they are trusted. I also want to locate their social media links to see their following on social media to determine how trusted and known they are.
 1. Once the new visitor has read the About Us and What We Do text, they will notice the Why We are Different section.
 2. The user can also notes of any pages is locate social media links .
 3. At the bottom of the Contact Us page is a copyright statement.

-   #### Returning Visitor Goals

    1. As a Returning Visitor, I want to find information about the artist and their work.
    
-   #### Frequent User Goals

    1. As a Frequent User, I want to check to see if there are any newly new blog posts.

        1. The user would already be comfortable with the website layout and can easily click the blog link to see any new message.

    2. As a Frequent User, I want to check to see if there are any new blog posts.

        1. The user would already be comfortable with the website layout and can easily click the blog link



### Further Testing

-   The blog was tested on Google Chrome, Internet Explorer, Microsoft Edge and Safari browsers.
-   The blog was viewed on a variety of devices such as Desktop, Laptop, iPhone7, iPhone 8 & iPhoneX.
-   A large amount of testing was done to ensure that all pages were linking correctly.
-   Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

## Bugs
-  Bug is found in the password reset form, the usrr get massage but not redirected to the login page.

| PASSWORD RESET | ![APPS.PY](https://res.cloudinary.com/dyemjyefz/image/upload/v1741570443/Screenshot_2025-03-07_210331_zuzeq2.png) 
| APP PASSWORD | ![VIEWS.PY](https://res.cloudinary.com/dyemjyefz/image/upload/v1741570392/Screenshot_2025-03-08_230626_dkifuk.png) 

<hr>

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
Contributions are welcome! If you have suggestions for new questions or improvements to the game, please feel free to open an issue .
