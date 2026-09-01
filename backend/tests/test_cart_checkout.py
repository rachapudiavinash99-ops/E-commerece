import secrets

def test_cart_coupon_and_checkout(client):
    # Create a fresh student user for clean cart test
    unique_email = f"shopper_{secrets.token_hex(4)}@codepulse.io"
    r_reg = client.post("/api/auth/register", json={
        "email": unique_email,
        "password": "Password123!",
        "full_name": "Cart Shopper",
        "role": "student"
    })
    token = r_reg.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # 1. Add course to cart
    r_add = client.post("/api/cart/items", json={"course_id": 2}, headers=headers)
    assert r_add.status_code == 200
    cart_data = r_add.json()
    assert cart_data["item_count"] == 1

    # 2. Validate Coupon
    r_coupon = client.get("/api/coupons/validate?code=CODEPULSE50&subtotal=59.99")
    assert r_coupon.status_code == 200
    assert r_coupon.json()["valid"] is True
    assert r_coupon.json()["discount_amount"] > 0

    # 3. Checkout Order
    r_order = client.post("/api/orders/checkout", json={"coupon_code": "CODEPULSE50"}, headers=headers)
    assert r_order.status_code == 201
    order_data = r_order.json()
    order_id = order_data["id"]

    # 4. Initiate Payment
    r_pay_init = client.post("/api/payments/initiate", json={"order_id": order_id}, headers=headers)
    assert r_pay_init.status_code == 200
    txn_id = r_pay_init.json()["transaction_id"]

    # 5. Verify Payment
    r_pay_verify = client.post("/api/payments/verify", json={"transaction_id": txn_id, "order_id": order_id}, headers=headers)
    assert r_pay_verify.status_code == 200
    assert r_pay_verify.json()["status"] == "successful"
