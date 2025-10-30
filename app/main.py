from flask import Flask, jsonify, request
from datetime import datetime
import uuid
import json
from functools import wraps

app = Flask(__name__)

# Optional API key validation (for AgentCore Gateway compatibility)
def validate_api_key(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Check for API key in headers (optional)
        api_key = request.headers.get('X-API-Key') or request.headers.get('X-Dummy-Auth')
        
        # For now, we accept any API key or no API key (public access)
        # In production, you might want to validate against a list of valid keys
        
        # Log the API key usage for debugging
        if api_key:
            app.logger.info(f"Request with API key: {api_key[:10]}...")
        else:
            app.logger.info("Request without API key (public access)")
            
        return f(*args, **kwargs)
    return decorated_function

# Sample data
orders = [
    {
        "id": "ord_001",
        "customer_id": "cust_001",
        "items": [
            {"product_id": "prod_001", "name": "Laptop", "quantity": 1, "price": 999.99},
            {"product_id": "prod_002", "name": "Mouse", "quantity": 2, "price": 29.99}
        ],
        "total": 1059.97,
        "status": "completed",
        "created_at": "2024-01-15T10:30:00Z"
    },
    {
        "id": "ord_002", 
        "customer_id": "cust_002",
        "items": [
            {"product_id": "prod_003", "name": "Keyboard", "quantity": 1, "price": 79.99}
        ],
        "total": 79.99,
        "status": "pending",
        "created_at": "2024-01-16T14:20:00Z"
    }
]

products = [
    {"id": "prod_001", "name": "Laptop", "price": 999.99, "category": "Electronics", "stock": 50},
    {"id": "prod_002", "name": "Mouse", "price": 29.99, "category": "Electronics", "stock": 100},
    {"id": "prod_003", "name": "Keyboard", "price": 79.99, "category": "Electronics", "stock": 75},
    {"id": "prod_004", "name": "Monitor", "price": 299.99, "category": "Electronics", "stock": 30}
]

customers = [
    {"id": "cust_001", "name": "John Doe", "email": "john@example.com", "phone": "+1-555-0123"},
    {"id": "cust_002", "name": "Jane Smith", "email": "jane@example.com", "phone": "+1-555-0124"}
]

purchases = [
    {
        "id": "pur_001",
        "order_id": "ord_001",
        "payment_method": "credit_card",
        "payment_status": "completed",
        "amount": 1059.97,
        "transaction_id": "txn_abc123",
        "processed_at": "2024-01-15T10:35:00Z"
    }
]

@app.route('/health', methods=['GET'])
@validate_api_key
def health_check():
    return jsonify({"status": "healthy", "timestamp": datetime.utcnow().isoformat()})

@app.route('/orders', methods=['GET'])
@validate_api_key
def get_orders():
    return jsonify({"orders": orders, "count": len(orders)})

@app.route('/order/<order_id>', methods=['GET'])
@validate_api_key
def get_order(order_id):
    order = next((o for o in orders if o["id"] == order_id), None)
    if order:
        return jsonify(order)
    return jsonify({"error": "Order not found"}), 404

@app.route('/order', methods=['POST'])
@validate_api_key
def create_order():
    data = request.get_json()
    new_order = {
        "id": f"ord_{str(uuid.uuid4())[:8]}",
        "customer_id": data.get("customer_id"),
        "items": data.get("items", []),
        "total": sum(item.get("price", 0) * item.get("quantity", 1) for item in data.get("items", [])),
        "status": "pending",
        "created_at": datetime.utcnow().isoformat() + "Z"
    }
    orders.append(new_order)
    return jsonify(new_order), 201

@app.route('/purchase', methods=['POST'])
@validate_api_key
def create_purchase():
    data = request.get_json()
    new_purchase = {
        "id": f"pur_{str(uuid.uuid4())[:8]}",
        "order_id": data.get("order_id"),
        "payment_method": data.get("payment_method", "credit_card"),
        "payment_status": "completed",
        "amount": data.get("amount"),
        "transaction_id": f"txn_{str(uuid.uuid4())[:8]}",
        "processed_at": datetime.utcnow().isoformat() + "Z"
    }
    purchases.append(new_purchase)
    return jsonify(new_purchase), 201

@app.route('/purchases', methods=['GET'])
@validate_api_key
def get_purchases():
    return jsonify({"purchases": purchases, "count": len(purchases)})

@app.route('/products', methods=['GET'])
@validate_api_key
def get_products():
    return jsonify({"products": products, "count": len(products)})

@app.route('/product/<product_id>', methods=['GET'])
@validate_api_key
def get_product(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        return jsonify(product)
    return jsonify({"error": "Product not found"}), 404

@app.route('/customers', methods=['GET'])
@validate_api_key
def get_customers():
    return jsonify({"customers": customers, "count": len(customers)})

@app.route('/customer/<customer_id>', methods=['GET'])
@validate_api_key
def get_customer(customer_id):
    customer = next((c for c in customers if c["id"] == customer_id), None)
    if customer:
        return jsonify(customer)
    return jsonify({"error": "Customer not found"}), 404

@app.route('/inventory', methods=['GET'])
@validate_api_key
def get_inventory():
    inventory = [{"product_id": p["id"], "name": p["name"], "stock": p["stock"]} for p in products]
    return jsonify({"inventory": inventory, "total_products": len(inventory)})

@app.route('/analytics/sales', methods=['GET'])
@validate_api_key
def get_sales_analytics():
    total_sales = sum(order["total"] for order in orders if order["status"] == "completed")
    completed_orders = len([o for o in orders if o["status"] == "completed"])
    return jsonify({
        "total_sales": total_sales,
        "completed_orders": completed_orders,
        "average_order_value": total_sales / completed_orders if completed_orders > 0 else 0
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)