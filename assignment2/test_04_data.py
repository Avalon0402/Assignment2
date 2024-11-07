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

def test_count_users_in_table(driver):
    # Mở trang hiển thị danh sách người dùng
    # Mở trang đăng nhập
    driver.get("http://localhost/Baitap/admin/login-admin.php")

    # Tìm và nhập tên đăng nhập
    username_field = driver.find_element(By.NAME, "username")
    username_field.send_keys("admin")
    time.sleep(1)

    # Tìm và nhập mật khẩu
    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys("123456")
    time.sleep(1)

    # Tìm và click vào nút đăng nhập
    login_button = driver.find_element(By.NAME, "dangnhap")
    login_button.click()
    time.sleep(1)

    # Chuyển đến trang quản lý tài khoản
    driver.get("http://localhost/Baitap/admin/admin2.php?action=quanlyaccounts&query=accounts")
    time.sleep(1)

    # Đợi bảng người dùng tải xong và tìm tất cả các hàng từ hàng có tên tài khoản "khoane" trở xuống
    start_row = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//td[text()='admin']/ancestor::tr"))
    )
    
    # Lấy tất cả các hàng từ hàng 'start_row' trở xuống
    user_rows_from_start = start_row.find_elements(By.XPATH, "following-sibling::tr")

    
    user_count = len(user_rows_from_start) + 1
    print(f"Số lượng người dùng từ hàng 'admin' trở xuống: {user_count}")

    # Kiểm tra nếu số lượng người dùng khớp với mong đợi của bạn (ví dụ: nếu bạn biết tổng là 15 từ hàng này trở xuống)
    assert user_count == 19, f"Số lượng người dùng không đúng, tìm thấy {user_count} thay vì 19."

