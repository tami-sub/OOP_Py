from abc import ABC, abstractmethod


class PaymentMethod():
    def __init__(self, is_card, is_apple_pay, is_bitcoin):
        self.is_card = is_card
        self.is_apple_pay = is_apple_pay
        self.is_bitcoin = is_bitcoin


class PaymentHandler(ABC):

    def __init__(self, successor=None):
        self.successor = successor

    @abstractmethod
    def handle(self, payment_option):
        pass


class CardPaymentHandler(PaymentHandler):

    def handle(self, payment_options):
        if payment_options.is_card:
            print("Заказ был оплачен бакновской картой")

            return True

        elif self.successor is not None:
            self.successor.handle(payment_options)

            return False


class ApplePaymentHandler(PaymentHandler):

    def handle(self, payment_options):
        if payment_options.is_apple_pay:
            print("Заказ был оплачен через Apple Pay")

            return True

        elif self.successor is not None:
            self.successor.handle(payment_options)

            return False


class BitcoinPaymentHandler(PaymentHandler):

    def handle(self, payment_options):
        if payment_options.is_bitcoin:
            print("Заказ был оплачен через bitcoin")

            return True

        elif self.successor is not None:
            self.successor.handle(payment_options)

            return False


