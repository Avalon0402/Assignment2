# Dangky

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

def test_registration_form(driver):
    # Mở trang đăng ký
    driver.get("http://localhost/Baitap/login_dangki.php")

    # Điền thông tin vào các trường nhập liệu
    driver.find_element(By.XPATH, "/html/body/div[1]/form/div[1]/input").send_keys("khoane1234567")
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
    driver.find_element(By.XPATH, "/html/body/div[1]/form/div[9]/input").send_keys("0123456789")
    time.sleep(1)

    # Nhấn nút đăng ký
    register_button = driver.find_element(By.XPATH, "/html/body/div[1]/form/input[2]")  # Giả sử nút đăng ký có thuộc tính name là "dangky"
    register_button.click()

    # Chờ phản hồi và kiểm tra kết quả (giả sử có thông báo thành công hiển thị)
    WebDriverWait(driver, 10).until(EC.url_to_be("http://localhost/Baitap/login.php"))
    assert driver.current_url == "http://localhost/Baitap/login.php", "Đăng ký thành công!"
    time.sleep(1)


def test_registration_with_existing_account(driver):
    # Mở trang đăng ký
    driver.get("http://localhost/Baitap/login_dangki.php")

    # Điền thông tin vào các trường nhập liệu với tài khoản đã tồn tại
    driver.find_element(By.XPATH, "/html/body/div[1]/form/div[1]/input").send_keys("khoane123456")  # Tên đăng nhập đã tồn tại
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
    driver.find_element(By.XPATH, "/html/body/div[1]/form/div[9]/input").send_keys("0123456789")
    time.sleep(1)

    # Nhấn nút đăng ký
    register_button = driver.find_element(By.XPATH, "/html/body/div[1]/form/input[2]")
    register_button.click()

    time.sleep(1)

    try:
        # Chờ và xử lý cảnh báo
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        assert "Tài khoản đã tồn tại" in alert.text, "Thông báo cảnh báo không đúng."
        alert.accept()  # Đóng cảnh báo bằng cách nhấn 'OK'
        print("Thông báo cảnh báo hiển thị đúng khi đăng ký với tài khoản đã tồn tại.")
    except Exception as e:
        pytest.fail(f"Không tìm thấy cảnh báo: {e}")
    
    
