import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


# Định nghĩa danh sách các kích thước màn hình để kiểm tra tính phản hồi
KICH_THUOC_MAN_HINH = [
    {"width": 1920, "height": 1080},  # Máy tính để bàn

    {"width": 1024, "height": 768},   # Máy tính bảng (Chế độ ngang)

    {"width": 768, "height": 1024},   # Máy tính bảng (Chế độ dọc)
    
    {"width": 375, "height": 667}     # Điện thoại di động (ví dụ: iPhone 6/7/8)
]

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()  # Đảm bảo rằng ChromeDriver có trong PATH của bạn
    yield driver
    driver.quit()

@pytest.mark.parametrize("size", KICH_THUOC_MAN_HINH)
def test_thiet_ke_phan_hoi(driver, size):
    # Mở ứng dụng
    driver.get("http://localhost/Baitap/index.php?quanly=main")

    # Thiết lập kích thước cửa sổ theo kích thước màn hình đã chỉ định
    driver.set_window_size(size["width"], size["height"])

   
    if size["width"] <= 768:
        # Kiểm tra các phần tử hoặc điều chỉnh bố cục dành riêng cho di động
        assert driver.find_element(By.XPATH, "/html/body/section[2]/div/button/a"), "Biểu tượng menu di động không tìm thấy trên kích thước màn hình di động."
    else:
        # Kiểm tra các phần tử hoặc điều chỉnh bố cục dành riêng cho máy tính để bàn/máy tính bảng
        assert driver.find_element(By.XPATH, "/html/body/section[2]/div/button/a"), "Menu máy tính để bàn không tìm thấy trên kích thước màn hình lớn hơn."

    # Các kiểm tra bổ sung có thể được thêm vào đây cho các phần tử khác
    # Ví dụ, xác minh tính hiển thị của một số nút, tỷ lệ ảnh phản hồi, v.v.
