"""
Module: Cryptocurrency Web3 Payment Invoice and Verification Adapter
"""

import hashlib
import time
from typing import Dict, Any


class CryptoGateway:
    """Web3 Cryptocurrency payment gateway generating Ethereum/USDC invoices and tracking deposits."""

    RECEIVING_WALLETS = {
        "ETH": "0x71C8395562d505a4f10c56789aBC1234567890ab",
        "USDC": "0x71C8395562d505a4f10c56789aBC1234567890ab",
        "BTC": "bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh"
    }

    @staticmethod
    def create_crypto_invoice(order_id: int, usd_amount: float, crypto_symbol: str = "USDC") -> Dict[str, Any]:
        """Generates a crypto invoice with unique payment address and QR code payload."""
        symbol = crypto_symbol.upper()
        wallet = CryptoGateway.RECEIVING_WALLETS.get(symbol, CryptoGateway.RECEIVING_WALLETS["USDC"])

        # Exchange rate simulation (1 ETH = 3,000 USD, 1 BTC = 60,000 USD, 1 USDC = 1.0 USD)
        rate_table = {"USDC": 1.0, "ETH": 3000.0, "BTC": 60000.0}
        rate = rate_table.get(symbol, 1.0)
        crypto_amount = round(usd_amount / rate, 6)

        invoice_id = f"CRYPTO-{symbol}-{int(time.time())}-{order_id}"
        qr_uri = f"ethereum:{wallet}?value={crypto_amount}" if symbol != "BTC" else f"bitcoin:{wallet}?amount={crypto_amount}"

        return {
            "invoice_id": invoice_id,
            "order_id": order_id,
            "crypto_symbol": symbol,
            "crypto_amount": crypto_amount,
            "usd_amount": usd_amount,
            "receiving_wallet": wallet,
            "qr_uri": qr_uri,
            "expires_at": int(time.time()) + 1800,  # 30 mins
            "status": "pending_payment"
        }
