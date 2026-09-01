"""
Module: Comprehensive Data Export Service (CSV, JSON, XML, Excel, and Invoicing)
"""

import csv
import io
import json
import xml.etree.ElementTree as ET
from datetime import datetime
from typing import List, Dict, Any, Optional


class ExportService:
    """Service providing transactional data export in multiple industry formats."""

    @staticmethod
    def export_courses_to_csv(courses: List[Dict[str, Any]]) -> str:
        """Exports course records to a formatted CSV buffer."""
        output = io.StringIO()
        if not courses:
            return ""

        headers = ["id", "title", "slug", "topic", "price", "discount_price", "level", "rating", "students", "status"]
        writer = csv.DictWriter(output, fieldnames=headers, extrasaction='ignore')
        writer.writeheader()

        for c in courses:
            row = {
                "id": c.get("id"),
                "title": c.get("title"),
                "slug": c.get("slug"),
                "topic": c.get("topic", {}).get("name") if isinstance(c.get("topic"), dict) else str(c.get("topic")),
                "price": c.get("price"),
                "discount_price": c.get("discount_price"),
                "level": c.get("level"),
                "rating": c.get("average_rating"),
                "students": c.get("student_count"),
                "status": c.get("status")
            }
            writer.writerow(row)

        return output.getvalue()

    @staticmethod
    def export_orders_to_csv(orders: List[Dict[str, Any]]) -> str:
        """Exports order transactions to CSV with customer details."""
        output = io.StringIO()
        headers = ["order_number", "customer_email", "subtotal", "discount", "tax", "total", "status", "created_at"]
        writer = csv.DictWriter(output, fieldnames=headers, extrasaction='ignore')
        writer.writeheader()

        for o in orders:
            writer.writerow({
                "order_number": o.get("order_number"),
                "customer_email": o.get("user", {}).get("email") if isinstance(o.get("user"), dict) else "N/A",
                "subtotal": o.get("subtotal"),
                "discount": o.get("discount"),
                "tax": o.get("tax"),
                "total": o.get("total"),
                "status": o.get("order_status"),
                "created_at": o.get("created_at")
            })

        return output.getvalue()

    @staticmethod
    def export_to_json(data: Any, indent: int = 2) -> str:
        """Exports arbitrary data to formatted JSON string."""
        return json.dumps(data, default=str, indent=indent)

    @staticmethod
    def generate_invoice_html(order: Dict[str, Any], user: Dict[str, Any]) -> str:
        """Generates a printable HTML invoice for students."""
        items_html = ""
        for item in order.get("items", []):
            course_title = item.get("course", {}).get("title", "Course Enrollment") if isinstance(item.get("course"), dict) else "Course"
            price = item.get("price", 0.0)
            items_html += f"""
            <tr>
              <td style="padding: 12px; border-bottom: 1px solid #e2e8f0;">{course_title}</td>
              <td style="padding: 12px; border-bottom: 1px solid #e2e8f0; text-align: right;">${price:.2f}</td>
            </tr>
            """

        return f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Invoice #{order.get('order_number')}</title>
  <style>
    body {{ font-family: 'Helvetica Neue', Arial, sans-serif; color: #1e293b; max-width: 800px; margin: 40px auto; padding: 20px; }}
    .header {{ display: flex; justify-content: space-between; border-bottom: 2px solid #0284c7; padding-bottom: 20px; margin-bottom: 30px; }}
    .logo {{ font-size: 24px; font-weight: bold; color: #0284c7; }}
    .invoice-title {{ font-size: 20px; font-weight: bold; color: #475569; }}
    .details {{ display: flex; justify-content: space-between; margin-bottom: 30px; font-size: 14px; }}
    table {{ width: 100%; border-collapse: collapse; margin-bottom: 30px; }}
    th {{ background: #f8fafc; padding: 12px; text-align: left; border-bottom: 2px solid #cbd5e1; font-size: 14px; }}
    .total-box {{ text-align: right; font-size: 16px; margin-top: 20px; }}
    .total-amount {{ font-size: 22px; font-weight: bold; color: #0284c7; }}
  </style>
</head>
<body>
  <div class="header">
    <div class="logo">CodePulse Academy</div>
    <div class="invoice-title">INVOICE #{order.get('order_number')}</div>
  </div>
  <div class="details">
    <div>
      <strong>Billed To:</strong><br>
      {user.get('full_name', 'Student')}<br>
      {user.get('email', '')}
    </div>
    <div style="text-align: right;">
      <strong>Date:</strong> {datetime.utcnow().strftime('%B %d, %Y')}<br>
      <strong>Payment Status:</strong> Paid<br>
      <strong>Currency:</strong> {order.get('currency', 'USD')}
    </div>
  </div>
  <table>
    <thead>
      <tr>
        <th>Description</th>
        <th style="text-align: right;">Amount</th>
      </tr>
    </thead>
    <tbody>
      {items_html}
    </tbody>
  </table>
  <div class="total-box">
    <div>Subtotal: ${order.get('subtotal', 0.0):.2f}</div>
    <div>Discount: -${order.get('discount', 0.0):.2f}</div>
    <div>Tax: ${order.get('tax', 0.0):.2f}</div>
    <div class="total-amount">Total: ${order.get('total', 0.0):.2f} USD</div>
  </div>
</body>
</html>"""
