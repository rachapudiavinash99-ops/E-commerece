def get_welcome_email(user_name: str) -> str:
    return f"""
    <div style="font-family: Arial, sans-serif; background-color: #0f172a; color: #f8fafc; padding: 30px; border-radius: 8px;">
        <h2 style="color: #38bdf8;">Welcome to CodePulse Academy, {user_name}!</h2>
        <p>Your account is ready. Explore our extensive catalog of interactive coding courses, practice in real-time programming environments, and earn verified industry certificates.</p>
        <p><a href="http://localhost:5173/courses" style="display: inline-block; background-color: #0284c7; color: white; padding: 12px 24px; text-decoration: none; border-radius: 6px; font-weight: bold;">Browse Courses</a></p>
        <hr style="border-color: #334155;" />
        <p style="font-size: 12px; color: #94a3b8;">CodePulse Academy - Master Full-Stack Engineering.</p>
    </div>
    """

def get_order_receipt_email(user_name: str, order_number: str, total: float, items: list) -> str:
    items_html = "".join([f"<li>{item['title']} - ${item['price']:.2f}</li>" for item in items])
    return f"""
    <div style="font-family: Arial, sans-serif; background-color: #0f172a; color: #f8fafc; padding: 30px; border-radius: 8px;">
        <h2 style="color: #22c55e;">Order Confirmation #{order_number}</h2>
        <p>Hi {user_name}, thank you for your purchase!</p>
        <h3>Purchased Courses:</h3>
        <ul>{items_html}</ul>
        <p><strong>Total Paid: ${total:.2f} USD</strong></p>
        <p><a href="http://localhost:5173/student/dashboard" style="display: inline-block; background-color: #22c55e; color: white; padding: 12px 24px; text-decoration: none; border-radius: 6px; font-weight: bold;">Start Learning Now</a></p>
    </div>
    """
