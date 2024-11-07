import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()  # Đảm bảo rằng ChromeDriver đã có trong PATH hoặc cung cấp đường dẫn chính xác
    yield driver
    driver.quit()

def test_login(driver):
    # Mở trang đăng nhập
    driver.get("http://localhost/Baitap/login.php")

    # Tìm và nhập tên đăng nhập
    username_field = driver.find_element(By.NAME, "username")
    username_field.send_keys("khoane")

    # Tìm và nhập mật khẩu
    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys("1234")

    # Tìm và click vào nút đăng nhập
    login_button = driver.find_element(By.NAME, "dangnhap")
    login_button.click()
    time.sleep(2)

    # Chờ trang chính tải xong
    WebDriverWait(driver, 10).until(EC.url_contains("index.php"))
    

    # Kiểm tra đăng nhập thành công
    assert "index.php" in driver.current_url, "Đăng nhập không thành công!"
    time.sleep(3)

    # Tìm và click vào menu bar
    menu_bar = driver.find_element(By.CLASS_NAME, "menu-bar")
    menu_bar.click()
    time.sleep(2)

    # Tìm và click vào nút đăng xuất
    logout_button = driver.find_element(By.LINK_TEXT, "Đăng xuất")
    logout_button.click()
    time.sleep(2)

    WebDriverWait(driver, 10).until(EC.url_to_be("http://localhost/Baitap/login.php?dangxuat=1"))
    assert driver.current_url == "http://localhost/Baitap/login.php?dangxuat=1", "Đăng xuất thành công!"

    time.sleep(3)


def test_loginfail(driver):
    # Mở trang đăng nhập
    driver.get("http://localhost/Baitap/login.php")

    # Tìm và nhập tên đăng nhập
    username_field = driver.find_element(By.NAME, "username")
    username_field.send_keys("khoane")

    # Tìm và nhập mật khẩu sai
    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys("123456")

    # Tìm và click vào nút đăng nhập
    login_button = driver.find_element(By.NAME, "dangnhap")
    login_button.click()

    # Kiểm tra nếu có thông báo lỗi hoặc vẫn ở trang đăng nhập
    WebDriverWait(driver, 10).until(EC.url_contains("login.php"))
    assert "login.php" in driver.current_url, "Không nhận thông báo lỗi khi đăng nhập thất bại!"
