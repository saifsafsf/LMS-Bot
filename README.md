# LMS-Bot

For automated syllabus download from LMS-NUST.

### Technology Used
- Selenium

### How to Run
Run main.py file.

### Requirements
#### Selenium
pip install selenium

#### Chrome Driver
Download the chrome driver from here:
"https://chromedriver.storage.googleapis.com/index.html"
Make sure to check your chrome version from "chrome://version" before downloading the driver.
After downloading the driver, update the driver's path in the __init__() in lms.py.

#### Credentials (optional)
Save your LMS credentials as "LMS_USER" & "LMS_PASS" in your environment variables for security purposes.
It is optional & you can simply pass the credentials as arguments to login() function in main.py but it is not recommended.
You might need to restart your device before running the program if using environment variables to log in.

#### Subject IDs
in the main.py file, the argument to download_subject() is the subject ID.
Each subject has a specific ID assoicated with it.
Replace these IDs with your subjects' IDs.
Find these IDs from LMS-NUST as shown below:

![SubjID](https://user-images.githubusercontent.com/73883918/163570732-02743f86-09af-4223-8dbe-44a66d43b6f8.png)


Remember, subjects with their IDs passed as arguments should all be visible on the dashboard in "Course Overview" section of LMS-NUST.

Feel free to suggest any changes in the program.

## Happy Coding!
