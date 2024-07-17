from pages.product_page import ProductPage
import pytest # type: ignore
import time


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer'

@pytest.mark.parametrize('promo', [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9])
def test_guest_can_add_product_to_basket(browser, promo):
    page = ProductPage(browser, link + str(promo))
    page.open()
    page.should_be_add_to_basket_btn()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    # time.sleep(1000)
    page.should_add_to_basket()