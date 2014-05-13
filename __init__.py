# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from .purchase_request import *


def register():
    Pool.register(
        CreatePurchaseRequestStart,
        module='stock_supply_warehouse', type_='model')
    Pool.register(
        CreatePurchaseRequest,
        module='stock_supply_warehouse', type_='wizard')
