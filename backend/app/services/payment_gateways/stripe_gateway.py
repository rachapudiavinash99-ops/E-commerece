"""
Module: Stripe Payment Gateway Integration Adapter
"""

import hmac
import hashlib
import time
from typing import Dict, Any, Optional


class StripeGateway:
    """Stripe Payment Gateway adapter supporting PaymentIntents and Webhook verification."""

    def __init__(self, api_key: str = "sk_test_demo", webhook_secret: str = "whsec_demo") -> None:
        self.api_key = api_key
        self.webhook_secret = webhook_secret

    def create_payment_intent(self, amount: float, currency: str, order_id: int, metadata: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Creates a simulated Stripe PaymentIntent with client secret."""
        cents = int(round(amount * 100))
        intent_id = f"pi_mock_{int(time.time())}_{order_id}"
        client_secret = f"{intent_id}_secret_test123"

        return {
            "id": intent_id,
            "object": "payment_intent",
            "amount": cents,
            "currency": currency.lower(),
            "status": "requires_payment_method",
            "client_secret": client_secret,
            "metadata": metadata or {"order_id": str(order_id)},
            "created": int(time.time())
        }

    def confirm_payment_intent(self, intent_id: str) -> Dict[str, Any]:
        """Confirms a PaymentIntent to simulate payment success."""
        return {
            "id": intent_id,
            "status": "succeeded",
            "charges": {
                "data": [{
                    "id": f"ch_{intent_id[3:]}",
                    "paid": True,
                    "receipt_url": f"https://pay.stripe.com/receipts/{intent_id}"
                }]
            }
        }

    def verify_webhook_signature(self, payload: bytes, signature_header: str) -> bool:
        """Verifies Stripe HMAC-SHA256 signature on incoming webhooks."""
        if not signature_header or not self.webhook_secret:
            return False

        try:
            parts = dict(pair.split("=") for pair in signature_header.split(","))
            timestamp = parts.get("t", "")
            expected_v1 = parts.get("v1", "")

            signed_payload = f"{timestamp}.".encode("utf-8") + payload
            computed_sig = hmac.new(
                self.webhook_secret.encode("utf-8"),
                signed_payload,
                hashlib.sha256
            ).hexdigest()

            return hmac.compare_digest(computed_sig, expected_v1)
        except Exception:
            return False
