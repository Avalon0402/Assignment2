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


def test_search_functionality(driver):
    driver.get("http://localhost/Baitap/login.php")

    # Nhập tên đăng nhập và mật khẩu
    driver.find_element(By.NAME, "username").send_keys("khoane")
    driver.find_element(By.NAME, "password").send_keys("1234")
    time.sleep(3)

    # Nhấn nút đăng nhập
    login_button = driver.find_element(By.NAME, "dangnhap")
    login_button.click()
    time.sleep(3)
    # Mở trang sau khi đăng nhập
    driver.get("http://localhost/Baitap/index.php?quanly=main")

    # Nhấn vào thanh menubar
    menubar = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/section[1]/header/div/div/div[2]")))
    menubar.click()
    time.sleep(1)

    # Tìm thanh tìm kiếm và nhập từ khóa
    search_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/section[1]/header/div/div/div[3]/ul/li[1]/form/input[1]"))
    )
    search_input.send_keys("sữa")
    time.sleep(1)

    # Thực hiện tìm kiếm
    search_button = driver.find_element(By.XPATH, "/html/body/section[1]/header/div/div/div[3]/ul/li[1]/form/input[2]")
    search_button.click()
    time.sleep(1)


    # Cuộn từ từ đến cuối trang
    last_height = driver.execute_script("return window.pageYOffset;")
    while True:
        # Cuộn xuống từng chút một
        driver.execute_script("window.scrollBy(0, 100);")
        time.sleep(0.5)  # Thời gian chờ để tạo hiệu ứng cuộn từ từ

        # Lấy vị trí mới và kiểm tra nếu đã đến cuối trang
        new_height = driver.execute_script("return window.pageYOffset;")
        if new_height == last_height:
            break  # Thoát khi không còn cuộn được nữa
        last_height = new_height