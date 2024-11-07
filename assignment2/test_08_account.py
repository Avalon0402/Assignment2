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


def test_changepass(driver):
    driver.get("http://localhost/Baitap/login.php")

    # Tìm và nhập tên đăng nhập
    username_field = driver.find_element(By.NAME, "username")
    username_field.send_keys("khoane")

    # Tìm và nhập mật khẩu sai
    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys("1234")

    # Tìm và click vào nút đăng nhập
    login_button = driver.find_element(By.NAME, "dangnhap")
    login_button.click()
    time.sleep(2)
    # Mở trang đăng ký
    driver.get("http://localhost/Baitap/index.php?quanly=thaydoimatkhau")

    # Điền thông tin vào các trường nhập liệu
    driver.find_element(By.XPATH, "/html/body/section[3]/div/div/form/table/tbody/tr[8]/td[2]/input").send_keys("khoa@gmail.com")
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/section[3]/div/div/form/table/tbody/tr[9]/td[2]/input").send_keys("1234")
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/section[3]/div/div/form/table/tbody/tr[10]/td[2]/input").send_keys("1234")
    time.sleep(1)

    # Nhấn vào nút thay đổi
    change_button = driver.find_element(By.XPATH, "/html/body/section[3]/div/div/form/table/tbody/tr[11]/td/input")
    change_button.click()

    # Đợi 2 giây để trang load (có thể điều chỉnh nếu cần)
    time.sleep(2)

    # Kiểm tra thông báo thay đổi thành công
    success_message = driver.find_element(By.XPATH, "/html/body/p")
    assert success_message.is_displayed(), "Thông báo thay đổi thành công không hiển thị."



    time.sleep(3)




def test_changepassfail(driver):
    # Mở trang đăng ký
    driver.get("http://localhost/Baitap/index.php?quanly=thaydoimatkhau")

    # Điền thông tin vào các trường nhập liệu
    driver.find_element(By.XPATH, "/html/body/section[3]/div/div/form/table/tbody/tr[8]/td[2]/input").send_keys("khoa@gmail.com")
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/section[3]/div/div/form/table/tbody/tr[9]/td[2]/input").send_keys("123456")
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/section[3]/div/div/form/table/tbody/tr[10]/td[2]/input").send_keys("1234")
    time.sleep(1)

    # Nhấn vào nút thay đổi
    change_button = driver.find_element(By.XPATH, "/html/body/section[3]/div/div/form/table/tbody/tr[11]/td/input")
    change_button.click()

    # Đợi 2 giây để trang load (có thể điều chỉnh nếu cần)
    time.sleep(2)

    # Kiểm tra thông báo thay đổi thành công
    success_message = driver.find_element(By.XPATH, "/html/body/p")

    assert success_message.is_displayed(), "Thông báo thay đổi thành công không hiển thị."

    
