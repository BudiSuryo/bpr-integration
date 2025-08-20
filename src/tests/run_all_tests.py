import json, os
from src.payment_processor.processor import PaymentProcessor
from src.channel_integrations.qris import generateQR

processor = PaymentProcessor()
test_folder = "src/tests/sample_payment_requests"
for file_name in os.listdir(test_folder):
    if file_name.endswith(".json"):
        file_path = os.path.join(test_folder, file_name)
        with open(file_path) as f:
            request = json.load(f)
        result = processor.process_payment(request)
        print(f"=== {file_name} PaymentProcessor Result ===")
        print(result)
        if request.get("channel") == "qris":
            qr_result = generateQR(request["amount"])
            print(f"=== {file_name} QRIS QR Code Result ===")
            print(qr_result)
        print("\n")
