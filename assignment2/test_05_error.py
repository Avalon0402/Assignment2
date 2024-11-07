import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()  # Đảm bảo ChromeDriver đã có trong PATH hoặc cung cấp đường dẫn chính xác
    yield driver
    driver.quit()

def test_registration_phone_number_validation(driver):
    # Mở trang đăng ký
    driver.get("http://localhost/Baitap/login_dangki.php")

    # Điền thông tin vào các trường nhập liệu
    driver.find_element(By.XPATH, "/html/body/div[1]/form/div[1]/input").send_keys("khoane123456")
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[1]/form/div[2]/input").send_keys("Khoa Khuu")
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[1]/form/div[3]/input").send_keys("12345678")
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[1]/form/div[4]/input").send_keys("12345678")
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[1]/form/div[5]/input").send_keys("Phường 1")
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[1]/form/div[6]/input").send_keys("Quận 1")
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[1]/form/div[7]/input").send_keys("Hồ Chí Minh")
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[1]/form/div[8]/input").send_keys("khoa@example.com")
    time.sleep(1)

    # Nhập số điện thoại dưới 10 chữ số
    driver.find_element(By.XPATH, "/html/body/div[1]/form/div[9]/input").send_keys("123456789")
    time.sleep(1)

    # Nhấn nút đăng ký
    register_button = driver.find_element(By.XPATH, "/html/body/div[1]/form/input[2]")
    register_button.click()
    time.sleep(1)

    # Chờ và kiểm tra thông báo alert
    alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
    assert alert.text == "Số điện thoại phải có đúng 10 chữ số!"
    
    # Đóng alert
    alert.accept()
