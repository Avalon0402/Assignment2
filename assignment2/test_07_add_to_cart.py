import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_empty_cart_logged(driver):  # giỏ hàng rỗng
    driver.get("http://localhost/Baitap/index.php")
    driver.find_element(By.CLASS_NAME, "menu-bar").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Đăng nhập").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/form/div[1]/input").send_keys("khoane")  # Username
    driver.find_element(By.XPATH, "/html/body/div/form/div[2]/input").send_keys("1234")  # Password
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, "button").click()
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, "menu-bar").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/section[1]/header/div/div/div[3]/ul/li[5]/a/i").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/section[3]/div/form/table/tbody/tr[8]/th/input").click()
    # Chờ cho alert xuất hiện và kiểm tra nội dung
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    time.sleep(1)
    # Xác minh nội dung của alert
    assert alert.text == "Vui lòng điền đầy đủ thông tin và thêm sản phẩm vào giỏ hàng trước khi thanh toán."
    
    # Đóng alert sau khi xác minh
    alert.accept()
    
    # Kiểm tra điều hướng đến trang giỏ hàng
    assert driver.current_url == "http://localhost/Baitap/index.php?quanly=giohang"

def test_add_to_cart_not_login(driver):  # giỏ hàng rỗng
    driver.get("http://localhost/Baitap/index.php")
    driver.find_element(By.CLASS_NAME, "menu-bar").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"/html/body/section[3]/div/div[2]/div/div[1]/div[2]/a/input").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"/html/body/div[1]/form/div[2]/input").click()
    time.sleep(2)
    assert driver.current_url == "http://localhost/Baitap/login.php"
def test_add_to_cart_logged(driver): 
    driver.get("http://localhost/Baitap/index.php") # hàm này để đã login và đặt sản phẩm vô được
    driver.find_element(By.CLASS_NAME, "menu-bar").click()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, "Đăng nhập").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div/form/div[1]/input").send_keys("khoane")  # Username
    driver.find_element(By.XPATH, "/html/body/div/form/div[2]/input").send_keys("1234")  # Password
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, "button").click()
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, "menu-bar").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"/html/body/section[3]/div/div[2]/div/div[1]/div[2]/a/input").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"/html/body/div[1]/form/div[2]/input").click()
    time.sleep(2)
    cart_items = driver.find_elements(By.XPATH, "//tbody[@id='giohang']/tr")
    time.sleep(2)
    assert len(cart_items)>0
    

def test_add_to_cart_with_size_topping_and_quantity(driver):
    driver.get("http://localhost/Baitap/index.php") # hàm này để đã login và đặt sản phẩm vô được
    driver.find_element(By.CLASS_NAME, "menu-bar").click()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, "Đăng nhập").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div/form/div[1]/input").send_keys("khoane")  # Username
    driver.find_element(By.XPATH, "/html/body/div/form/div[2]/input").send_keys("1234")  # Password
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, "button").click()
    time.sleep(2)
    
    # Chọn sản phẩm
    driver.find_element(By.XPATH,"/html/body/section[3]/div/div[2]/div/div[1]/div[2]/a/input").click()
    time.sleep(2)
    #chọn size
    driver.find_element(By.XPATH,"/html/body/div[1]/form/div[2]/div[1]/div[1]/input[3]").click()
    text_size = driver.find_element(By.XPATH,"/html/body/div[1]/form/div[2]/div[1]/div[1]/input[3]").get_attribute("value")
    time.sleep(2)
    #chọn topping
    driver.find_element(By.XPATH,"/html/body/div[1]/form/div[2]/div[1]/div[2]/input[1]").click()
    text_topping = driver.find_element(By.XPATH,"/html/body/div[1]/form/div[2]/div[1]/div[2]/input[1]").get_attribute("value")
    time.sleep(2)
    #chọn quantity
    input_element = driver.find_element(By.ID, "soluongdat")
    for _ in range(5):
        input_element.send_keys(Keys.ARROW_UP)
    text_quantity = driver.find_element(By.ID, "soluongdat").text
    time.sleep(2)
    driver.find_element(By.XPATH,"/html/body/div[1]/form/div[2]/input").click()
    time.sleep(2)

    test_col_topping = driver.find_element(By.XPATH,"/html/body/section[3]/div/table[1]/tbody[2]/tr/td[5]").text
    test_col_size = driver.find_element(By.XPATH,"/html/body/section[3]/div/table[1]/tbody[2]/tr/td[7]").text
    test_col_quantity = driver.find_element(By.XPATH,"/html/body/section[3]/div/table[1]/tbody[2]/tr/td[8]/input").text
    
    assert text_size == test_col_size
    assert test_col_topping.replace(",", "") == text_topping
    assert test_col_quantity == text_quantity
def test_decrease_quantity (driver):
    driver.get("http://localhost/Baitap/index.php") # hàm này để đã login và đặt sản phẩm vô được
    driver.find_element(By.CLASS_NAME, "menu-bar").click()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, "Đăng nhập").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div/form/div[1]/input").send_keys("khoane")  # Username
    driver.find_element(By.XPATH, "/html/body/div/form/div[2]/input").send_keys("1234")  # Password
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, "button").click()
    time.sleep(2)
    # Chọn sản phẩm
    driver.find_element(By.XPATH,"/html/body/section[3]/div/div[2]/div/div[1]/div[2]/a/input").click()
    time.sleep(2)
    #chọn quantity
    input_element = driver.find_element(By.XPATH, "/html/body/div[1]/form/div[2]/div[2]/input")
    input_element.send_keys(Keys.ARROW_DOWN)
    
    # Lấy giá trị số lượng sau khi giảm
    text_quantity = input_element.get_attribute('value')
    time.sleep(1)
    
    # Kiểm tra giá trị số lượng
    assert text_quantity == "1"
def test_invalid_quantity_input(driver):
    driver.get("http://localhost/Baitap/index.php") # hàm này để đã login và đặt sản phẩm vô được
    driver.find_element(By.CLASS_NAME, "menu-bar").click()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, "Đăng nhập").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div/form/div[1]/input").send_keys("khoane")  # Username
    driver.find_element(By.XPATH, "/html/body/div/form/div[2]/input").send_keys("1234")  # Password
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, "button").click()
    time.sleep(2)
    # Chọn sản phẩm
    driver.find_element(By.XPATH,"/html/body/section[3]/div/div[2]/div/div[1]/div[2]/a/input").click()
    time.sleep(2)
    #chọn quantity
    driver.find_element(By.XPATH, "/html/body/div[1]/form/div[2]/div[2]/input").clear()
    input_element = driver.find_element(By.XPATH, "/html/body/div[1]/form/div[2]/div[2]/input").send_keys("0")
    quantity_alert = driver.find_element(By.XPATH, "/html/body/div[1]/form/div[2]/div[2]/input")
    driver.find_element(By.XPATH,"/html/body/div[1]/form/div[2]/input").click()
    time.sleep(5)
    custom_message = quantity_alert.get_attribute("validationMessage")
    assert "Value must be greater than or equal to 1." in custom_message
    driver.quit()
def test_pagination(driver):
    # Mở trang web
    driver.get("http://localhost/Baitap/index.php")
    
    # Tìm menu và nhấn vào Thực đơn
    driver.find_element(By.CLASS_NAME, "menu-bar").click()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, "Thực đơn").click()
    time.sleep(2)

    # Lấy tất cả các phần tử <a> trong danh sách phân trang
    page_links = driver.find_elements(By.CSS_SELECTOR, 'ul.listPage li a')
    
    # Lặp qua từng liên kết trang và thực hiện click, từ trang 1 đến cuối
    for i in range(len(page_links)):
        try:
            # Click vào liên kết trang (chỉ click vào trang kế tiếp sau khi hoàn thành trang trước)
            page_links[i].click()
            
            # Chờ trang tải sau khi click
            time.sleep(2)  # Tùy chỉnh thời gian chờ nếu cần
            
            # Kiểm tra URL sau khi chuyển trang (đảm bảo có tham số "trang")
            current_url = driver.current_url
            if "trang=" in current_url:
                print(f"Đã chuyển đến trang: {current_url}")
            else:
                print(f"Lỗi chuyển trang: {current_url}")
                
            # Sau khi click một trang, lấy lại các liên kết trang sau khi trang mới tải
            page_links = driver.find_elements(By.CSS_SELECTOR, 'ul.listPage li a')

        except Exception as e:
            print(f"Không thể truy cập trang: {e}")
            break

    # Đóng trình duyệt sau khi hoàn thành
    driver.quit()