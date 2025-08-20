class PaymentProcessor:
    def process_payment(self, payment_request):
        print(f'Processing payment: {payment_request}')
        return {'status':'success','amount':payment_request.get('amount',0)}