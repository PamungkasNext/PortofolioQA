from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# Setup WebDriver
driver = webdriver.Chrome()  # Pastikan driver Chrome terinstall dan path sudah diatur
driver.maximize_window()

# Navigate to the page
driver.get("https://demoqa.com/automation-practice-form")

# Fill in the form
try:
    # First Name
    driver.find_element(By.ID, "firstName").send_keys("Aditya")

    # Last Name
    driver.find_element(By.ID, "lastName").send_keys("Pamungkas")

    # Email
    driver.find_element(By.ID, "userEmail").send_keys("aditya.pamungkas@example.com")

    # Gender
    driver.find_element(By.XPATH, "//label[contains(text(),'Male')]").click()

    # Mobile Number
    driver.find_element(By.ID, "userNumber").send_keys("081905266109")

    # Date of Birth
    driver.find_element(By.ID, "dateOfBirthInput").click()
    time.sleep(1)  # Wait for calendar to appear
    driver.find_element(By.XPATH, "//select[@class='react-datepicker__month-select']").send_keys("May")
    driver.find_element(By.XPATH, "//select[@class='react-datepicker__year-select']").send_keys("1995")
    driver.find_element(By.XPATH, "//div[@class='react-datepicker__day react-datepicker__day--015']").click()

    # Subjects
    subject_field = driver.find_element(By.ID, "subjectsInput")
    subject_field.send_keys("Computer Science")
    subject_field.send_keys(Keys.RETURN)

    # Hobbies
    driver.find_element(By.XPATH, "//label[contains(text(),'Reading')]").click()

    # Upload Picture
    upload_field = driver.find_element(By.ID, "uploadPicture")
    upload_field.send_keys("C:\\path_to_your_image\\image.jpg")  # Replace with the path to your image

    # Current Address
    driver.find_element(By.ID, "currentAddress").send_keys("Jl. Merdeka, Jakarta")

    # State and City
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # Scroll down
    driver.find_element(By.ID, "react-select-3-input").send_keys("NCR")
    driver.find_element(By.ID, "react-select-3-input").send_keys(Keys.RETURN)
    driver.find_element(By.ID, "react-select-4-input").send_keys("Delhi")
    driver.find_element(By.ID, "react-select-4-input").send_keys(Keys.RETURN)

    # Submit
    driver.find_element(By.ID, "submit").click()

    # Wait to see the result
    time.sleep(5)

finally:
    # Close the browser
    driver.quit()
