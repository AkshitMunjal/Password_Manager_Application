
# Password Manager Application

This project is a Password Manager built using Python and the tkinter library. It features a graphical user interface (GUI) to securely store, generate, and retrieve passwords for various websites. The application ensures a seamless and user-friendly experience for managing passwords efficiently.



## Features

1. Secure Password Storage:

➤ Store website credentials (email/username and password) in a local JSON file.

➤Update existing credentials for the same website.

2. Password Generator:

➤Generate strong, random passwords with a mix of letters, numbers, and symbols.

➤Automatically copy generated passwords to the clipboard for ease of use.

3. Password Search:

➤Quickly search for saved credentials using the website name.

➤Retrieve stored email/username and password.

4. Intuitive User Interface:

➤Built using tkinter, providing a clean and interactive design.

➤Easy-to-use forms for entering and managing data.





## How to Run

1. Clone this repository to your local machine.

2. Ensure you have Python installed (preferably version 3.6 or higher).

3. Required Python Libraries: 

    ➡ tkinter
    
    ➡ Pillow
    
    ➡ pyperclip
    
    ➡ json

    ➡ random


4. Install the required libraries using pip:

   pip install pillow pyperclip

5. Add new credentials, generate secure passwords, and 
   search for stored credentials.

## Project Structure

🔑password_manager.py: Main script containing the GUI and application logic.

🔑password.json: Local file used to store website credentials (created automatically).


## User Guide

1. Adding a New Password

✔️Enter the website name, email/username, and password.

✔️Generate a secure password using the Generate Password button (optional).

✔️Click Add to save the credentials.

2. Searching for a Password

✔️Enter the website name.

✔️Click Search to retrieve the email and password associated with the website.

3. Generating a Secure Password

✔️Click the Generate Password button.

✔️The generated password will be displayed in the password field and copied to the clipboard.  


![image alt](https://github.com/AkshitMunjal/Password_Manager_Application/blob/3aa01d89e3944a615d8aaf68e9366413f4d5e05b/Password_Manager_App.png)

