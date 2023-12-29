import time
from selenium.webdriver.common.by import By


class HomePageLocators:
    logout_downArrow_xpath = '//i[@class="oxd-icon bi-caret-down-fill oxd-userdropdown-icon"]'
    logout_xpath = "//a[text()='Logout']"
    Dashboard_title_xpath = "//h6[text()='Dashboard']"

    pim_tab_xpath = '// a[@href="/web/index.php/leave/viewLeaveModule"]'
    employeeInformation_Header_xpath = "//h5[text()='Employee Information']"

    Leave_tab_xpath = '//a[@href="/web/index.php/leave/viewLeaveModule"]'
    leaveList_Header_xpath = "//h5[text()='Leave List']"

    Time_tab_xpath = '//a[@href="/web/index.php/time/viewTimeModule"]'
    timesheetsPendingAction_Header_xpath = "//h6[text()='Timesheets Pending Action']"

    Recruitment_tab_xpath = '//a[@href="/web/index.php/recruitment/viewRecruitmentModule"]'
    candidates_Header_xpath = "//h5[text()='Candidates']"

    def __init__(self, driver):
        self.driver = driver

    def click_logout_downArrow(self):
        self.driver.find_element(By.NAME, self.logout_downArrow_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.logout_xpath).click()
        time.sleep(1)

    def capture_verify_title(self, title_name):
        captured_title_Dashboard_txt = self.driver.find_element(By.XPATH, self.Dashboard_title_xpath).text
        assert captured_title_Dashboard_txt == title_name

    def click_pim_tab(self):
        self.driver.find_element(By.XPATH, self.pim_tab_xpath).click()
        time.sleep(1)

    def capture_verify_pim_header(self, pim_header_name):
        captured_pim_header_txt = self.driver.find_element(By.XPATH, self.employeeInformation_Header_xpath).text
        assert captured_pim_header_txt == pim_header_name

    def click_leave_tab(self):
        self.driver.find_element(By.XPATH, self.Leave_tab_xpath).click()
        time.sleep(1)

    def capture_verify_leave_header(self, Leave_header_name):
        captured_leave_header_txt = self.driver.find_element(By.XPATH, self.leaveList_Header_xpath).text
        assert captured_leave_header_txt == Leave_header_name

    def click_time_tab(self):
        self.driver.find_element(By.XPATH, self.Time_tab_xpath).click()
        time.sleep(1)

    def capture_verify_time_header(self, time_header_name):
        captured_time_header_txt = self.driver.find_element(By.XPATH, self.timesheetsPendingAction_Header_xpath).text
        assert captured_time_header_txt == time_header_name

    def click_recruitment_tab(self):
        self.driver.find_element(By.XPATH, self.Recruitment_tab_xpath).click()
        time.sleep(1)

    def capture_verify_recruitment_header(self, recruitment_header_name):
        captured_recruitment_header_txt = self.driver.find_element(By.XPATH, self.candidates_Header_xpath).text
        assert captured_recruitment_header_txt == recruitment_header_name
