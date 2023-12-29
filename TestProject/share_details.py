# from lib2to3.pgen2 import driver
import logging
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from BaseClass import LoginPageLocators

import pandas as pd


# driver = webdriver.Chrome(executable_path = f"C:\\Users\\lenovo\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")

# serv_obj = Service("C:\\Users\\lenovo\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
serv_obj = Service("C:\\Users\\lenovo\\Downloads\\chromedriver-win64_120\\chromedriver-win64\\chromedriver.exe")

driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.google.com/")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.XPATH, "//textarea[@title='Search']").send_keys("orangehrm demo", Keys.RETURN)
driver.find_element(By.XPATH, '//a[@href="https://opensource-demo.orangehrmlive.com/"]').click()
time.sleep(4)
list_u = {'Admin_invalid': 'admin123', 'admin123': 'admin123_invalid', 'Admin': 'admin123'}

for u, p in list_u.items():
    print(u, p)
    # driver.find_element(By.NAME, "username").send_keys(u)
    # driver.find_element(By.NAME, "password").send_keys(p)
    # driver.find_element(By.XPATH, '//button[@type="submit"]').click()

    log_obj = LoginPageLocators(driver)
    log_obj.set_username('Admin')
    log_obj.set_password('admin123')
    log_obj.click_login()
    time.sleep(2)
    captured_error_msg = driver.find_element(By.XPATH, "//p[text()='Invalid credentials']").text
    assert captured_error_msg == 'Invalid credentials'
    print('iteration done')
    # if captured_error_msg == 'Invalid credentials':
    #     captured_error_msg_Required = driver.find_element(By.XPATH, "(//span[text()='Required'])[1] | (//span[text()='Required'])[2]").text
    #     assert captured_error_msg_Required == 'Required'


# def read_credentials(file_path):
#     try:
#         df = pd.read_excel(file_path)
#         return df[['Username', 'Password']]
#     except FileNotFoundError:
#         print(f'Error: File "{file_path}" not found.')
#         return None


# # Example usage
# excel_file_path = 'C:\\Users\\lenovo\\PycharmProjects\\TestProject\\example.xlsx'
# # credentials_df = read_credentials(excel_file_path)
#
# read_df = pd.read_excel(excel_file_path)
# # read_df = pd.drop(0, axis=1)
# print('\nDataFrame read from Excel file:')
# print(read_df)
# print('***************')
# print(read_df['Username'])
# print(type(read_df['Username']))
#
# print('***************')
# print(read_df['Username'][1])
# for i, v in read_df['Username'].items():
#     # print(read_df['Username'][i])
#     print(i, v)


# data = {'A': 10, 'B': 20, 'C': 30}
# series_data = pd.Series(data)
# print(series_data)
#
# for index, value in series_data.items():
#     print(f'Index: {index}, Value: {value}')




# if credentials_df is not None:
#     print('Login Credentials:')
#     print(credentials_df)
#
# # Example usage
# input_username = input('Enter your username: ')
# input_password = input('Enter your password: ')
#
# if check_credentials(input_username, input_password):
#     print('Login successful!')
# else:
#     print('Invalid credentials. Please try again.')




print("Logged in successfully")

captured_title_Dashboard_txt = driver.find_element(By.LINK_TEXT, "Dashboard").text
assert captured_title_Dashboard_txt == 'Dashboard'
driver.find_element(By.XPATH, '//i[@class="oxd-icon bi-caret-down-fill oxd-userdropdown-icon"]').click()
driver.find_element(By.LINK_TEXT, "Logout").click()
time.sleep(1)
print("Logged out successfully")


# driver.get("https://www.tickertape.in/")
# driver.get("https://www.moneycontrol.com/")

# company_list = ['Reliance Industries Ltd', 'HDFC Bank Ltd', 'Infosys Ltd', 'ICICI Bank Ltd']
# # 'Housing Development Fin Corp Ltd', 'Tata Consultancy Services Ltd', 'Kotak Mahindra Bank Ltd',
# # 'ACC Ltd', 'Larsen & Toubro Ltd', 'Axis Bank Ltd', 'Bharti Airtel', 'Eicher Motar', 'Bajaj Finance',
# # 'Hindalco', 'Bajaj Finserv', 'Hindustan Unilever', 'ONGC', 'ITC', 'SBIN', 'Asian Paint', 'Tata Steel',
# # 'HCL Tech', 'Sun Pharma', 'Tech Mahindra']
# for i in company_list:
#     company_name = i
#     print(company_name)
#     search_obj = driver.find_element(By.XPATH, "//form[@id='form_topsearch']//input[@id='search_str']").send_keys("" + company_name + "", Keys.RETURN)
#
# # //form[@id="form_topsearch"]//input[@id="search_str"]
#
# # //div[@id="autosuggestlist"]/ul/li/a[1]
#
# driver.find_element(By.XPATH, "//button[text()='Login']").click()
# time.sleep(5)
#
#
# company_list = ['Reliance Industries Ltd', 'HDFC Bank Ltd', 'Infosys Ltd', 'ICICI Bank Ltd']
# # 'Housing Development Fin Corp Ltd', 'Tata Consultancy Services Ltd', 'Kotak Mahindra Bank Ltd',
# # 'ACC Ltd', 'Larsen & Toubro Ltd', 'Axis Bank Ltd', 'Bharti Airtel', 'Eicher Motar', 'Bajaj Finance',
# # 'Hindalco', 'Bajaj Finserv', 'Hindustan Unilever', 'ONGC', 'ITC', 'SBIN', 'Asian Paint', 'Tata Steel',
# # 'HCL Tech', 'Sun Pharma', 'Tech Mahindra']
# for i in company_list:
#     company_name = i
#     print(company_name)
#     # driver.find_element(By.ID, "search-stock-input").send_keys(company_name)
#     # time.sleep(2)
#     try:
#         # driver.find_element(By.XPATH, "(//span[text()=\'"+company_name+"\'])[1]").click()
#
#         search_obj = driver.find_element(By.ID, "search-stock-input").send_keys("" + company_name + "", Keys.RETURN)
#         time.sleep(5)
#         # driver.implicitly_wait(10)
#         # driver.refresh()
#         # time.sleep(5)
#
#         # driver.find_element(By.ID, "search-stock-input").send_keys("Tata Motors Ltd")
#         # print("After value entered")
#         # driver.find_element(By.ID, "search-stock-input").send_keys(u'\ue007')
#         # print("After hit enter")
#         # time.sleep(1)
#         # driver.find_element(By.XPATH,"(//span[text()='Tata Motors Ltd'])[1]").click()
#         # time.sleep(5)
#     except Exception as e:
#         print("Exception is: ", e)
#         raise Exception('My error!')
#     try:
#         button = driver.find_element(By.XPATH, "(//span[text()=\'" + company_name + "\'])[1]")
#         driver.execute_script("arguments[0].click();", button)
#     except Exception as e:
#         print("Exception is: ", e)
#         # raise Exception('My error!')
#
#     driver.find_element(By.XPATH, "//a[@data-label='Overview']").click()
#     # logging.info("After click on Overview")
#     TTM_PE_Ratio = driver.find_element(By.XPATH,
#                                        "((//span[text()='TTM PE Ratio'])[1]/../following::tbody/tr/td)[1]").text
#     logging.info("After captured_TTM_PE_Ratio")
#     # print("After captured_TTM_PE_Ratio")
#     print("TTM_PE_Ratio : ", TTM_PE_Ratio)
#     Sector_PE = driver.find_element(By.XPATH,
#                                     "((//span[text()='Sector PE'])[1]/../following::tbody/tr/td)[1]").text
#     print("Sector_PE : ", Sector_PE)
#     if TTM_PE_Ratio > Sector_PE:
#         print("\'" + company_name + "\' is good for technical analysis")
#     print("*****************************************")
# print("Script executed successfully")


# # Create a sample DataFrame
# data = {'Stock_Name': ['John', 'Alice', 'Bob'],
#         'Age': [25, 30, 35],
#         'City': ['New York', 'London', 'Paris']}
#
# df = pd.DataFrame(data)
#
# # Write DataFrame to an Excel file
# excel_file_path = 'example.xlsx'
# df.to_excel(excel_file_path, index=False)
#
# print(f'DataFrame written into file {excel_file_path}')
#
# # Read data from an Excel file into a DataFrame
# read_df = pd.read_excel(excel_file_path)
#
# # Display the read DataFrame
# print('\nDataFrame read from Excel file:')
# print(read_df)
