import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()  # Đảm bảo ChromeDriver đã có trong PATH hoặc cung cấp đường dẫn chính xác
    yield driver
    driver.quit()

def test_click_facebook_icon_after_login(driver):
    # Bước 1: Mở trang đăng nhập và thực hiện đăng nhập
    driver.get("http://localhost/Baitap/login.php")

    # Nhập tên đăng nhập và mật khẩu
    driver.find_element(By.NAME, "username").send_keys("khoane")
    driver.find_element(By.NAME, "password").send_keys("1234")
    time.sleep(3)

    # Nhấn nút đăng nhập
    login_button = driver.find_element(By.NAME, "dangnhap")
    login_button.click()
    time.sleep(3)

    # Chờ cho đến khi chuyển hướng đến trang chính sau khi đăng nhập thành công
    WebDriverWait(driver, 10).until(EC.url_to_be("http://localhost/Baitap/index.php"))

    # Bước 2: Cuộn xuống và nhấp vào biểu tượng Facebook
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

    # Chờ biểu tượng Facebook hiển thị (giả sử biểu tượng có class là "fb-icon" hoặc có href đến Facebook)
    facebook_icon = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/section[4]/div/div[2]/a[1]"))  # Thay "fb-icon" bằng class hoặc ID của biểu tượng
    )
    # Sử dụng ActionChains để di chuyển chuột đến biểu tượng Facebook và nhấp vào nó
    ActionChains(driver).move_to_element(facebook_icon).click().perform()

    # Chờ tab mới hoặc cửa sổ mới được mở (nếu có)
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

    # Chuyển sang tab mới (tab Facebook)
    driver.switch_to.window(driver.window_handles[1])

    # Kiểm tra URL của tab mới để đảm bảo rằng đã mở đúng trang Facebook
    assert "facebook.com" in driver.current_url, "Không mở đúng trang Facebook!"

    # Đóng tab Facebook và quay lại tab chính
    driver.close()
    driver.switch_to.window(driver.window_handles[0])



def test_click_twitter_icon_after_login(driver):
    # Bước 1: Mở trang đăng nhập và thực hiện đăng nhập
    driver.get("http://localhost/Baitap/login.php")

    # Nhập tên đăng nhập và mật khẩu
    driver.find_element(By.NAME, "username").send_keys("khoane")
    driver.find_element(By.NAME, "password").send_keys("1234")
    time.sleep(3)

    # Nhấn nút đăng nhập
    login_button = driver.find_element(By.NAME, "dangnhap")
    login_button.click()
    time.sleep(3)

    # Chờ cho đến khi chuyển hướng đến trang chính sau khi đăng nhập thành công
    WebDriverWait(driver, 10).until(EC.url_to_be("http://localhost/Baitap/index.php"))

    # Bước 2: Cuộn xuống và nhấp vào biểu tượng Twitter
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

    # Chờ biểu tượng Twitter hiển thị và nhấp vào nó
    twitter_icon = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/section[4]/div/div[2]/a[2]"))  # Đảm bảo đúng XPath của biểu tượng Twitter
    )
    # Sử dụng ActionChains để di chuyển chuột đến biểu tượng Twitter và nhấp vào nó
    ActionChains(driver).move_to_element(twitter_icon).click().perform()

    # Chờ tab mới hoặc cửa sổ mới được mở (nếu có)
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

    # Chuyển sang tab mới (tab Twitter)
    driver.switch_to.window(driver.window_handles[1])

    # Kiểm tra URL của tab mới để đảm bảo rằng đã mở đúng trang Twitter
    assert "twitter.com" in driver.current_url, "Không mở đúng trang Twitter!"

    # Đóng tab Twitter và quay lại tab chính
    driver.close()
    driver.switch_to.window(driver.window_handles[0])


def test_click_instagram_icon_after_login(driver):
    # Bước 1: Mở trang đăng nhập và thực hiện đăng nhập
    driver.get("http://localhost/Baitap/login.php")

    # Nhập tên đăng nhập và mật khẩu
    driver.find_element(By.NAME, "username").send_keys("khoane")
    driver.find_element(By.NAME, "password").send_keys("1234")
    time.sleep(3)

    # Nhấn nút đăng nhập
    login_button = driver.find_element(By.NAME, "dangnhap")
    login_button.click()
    time.sleep(3)

    # Chờ cho đến khi chuyển hướng đến trang chính sau khi đăng nhập thành công
    WebDriverWait(driver, 10).until(EC.url_to_be("http://localhost/Baitap/index.php"))

    # Bước 2: Cuộn xuống và nhấp vào biểu tượng Twitter
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

    # Chờ biểu tượng Twitter hiển thị và nhấp vào nó
    instagram_icon = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/section[4]/div/div[2]/a[3]"))  # Đảm bảo đúng XPath của biểu tượng Twitter
    )
    # Sử dụng ActionChains để di chuyển chuột đến biểu tượng Twitter và nhấp vào nó
    ActionChains(driver).move_to_element(instagram_icon).click().perform()

    # Chờ tab mới hoặc cửa sổ mới được mở (nếu có)
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

    # Chuyển sang tab mới (tab Twitter)
    driver.switch_to.window(driver.window_handles[1])

    # Kiểm tra URL của tab mới để đảm bảo rằng đã mở đúng trang Twitter
    assert "instagram.com" in driver.current_url, "Không mở đúng trang instagram!"

    # Đóng tab instagram và quay lại tab chính
    driver.close()
    driver.switch_to.window(driver.window_handles[0])



