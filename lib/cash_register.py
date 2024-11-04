#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.transactions = []

  @property
  def discount(self):
    return self._discount
  
  @discount.setter
  def discount(self, discount):
    self._discount = discount

  def add_item(self, title, price, quantity=1):
    self.total += price * quantity
    for _ in range(quantity):
      self.items.append(title)
      self.transactions.append([price, quantity])
    return self.total
  
  def apply_discount(self):
    if self.discount == 0:
      print("There is no discount to apply.")
    else:
      self.total -= int(self.total * (self.discount / 100))
      print(f'After the discount, the total comes to ${self.total}.')

  def void_last_transaction(self):
    last_price, last_quantity = self.transactions.pop()
    self.total -= last_price * last_quantity

    return self.total
    