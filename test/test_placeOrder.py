import pytest
from ..pages.placeOrder import PlaceOrder

@pytest.mark.order(5)
def testSelectManCategory(driver):
    callPlaceOrder = PlaceOrder(driver)
    selected_category = callPlaceOrder.selectManCategory()
    assert "tshirts" in selected_category.lower(), f"Expected selected category to contain 'Tshirts', got '{selected_category}'"
    

@pytest.mark.order(6)
def testGetTotalProducts(driver):
    callPlaceOrder = PlaceOrder(driver)
    total_products = callPlaceOrder.getTotalProducts()
    assert total_products > 0, f"Expected total products to be greater than 0, got {total_products}"    

@pytest.mark.order(7)
def testSelectProduct(driver):
    callPlaceOrder = PlaceOrder(driver)
    selected_product = callPlaceOrder.selectProduct()

@pytest.mark.order(8)
def testGetProductDetails(driver):
    callPlaceOrder = PlaceOrder(driver)
    product_name, product_price = callPlaceOrder.getProductDetails()
    assert product_name != "", "Expected product name to be non-empty"
    assert product_price != "", "Expected product price to be non-empty"

@pytest.mark.order(9)
def testAddToCart(driver):
    callPlaceOrder = PlaceOrder(driver)
    callPlaceOrder.addToCart()

@pytest.mark.order(10)
def testVerifyCart(driver):
    callPlaceOrder = PlaceOrder(driver)
    callPlaceOrder.getProductDetails()
    callPlaceOrder.verifyCart()

@pytest.mark.order(11)  
def placeOrderDetsils(driver):
    callPlaceOrder = PlaceOrder(driver)
    callPlaceOrder.proceedToCheckout()
    callPlaceOrder.placeOrder()
    callPlaceOrder.payment()