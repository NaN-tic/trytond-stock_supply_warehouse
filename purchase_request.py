#The COPYRIGHT file at the top level of this repository contains the full
#copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = ['CreatePurchaseRequestStart', 'CreatePurchaseRequest']
__metaclass__ = PoolMeta


class CreatePurchaseRequestStart:
    __name__ = 'purchase.request.create.start'

    warehouses = fields.Many2Many('stock.location', None, None, 'Warehouses',
        domain=[
            ('type', '=', 'warehouse'),
            ])


class CreatePurchaseRequest:
    __name__ = 'purchase.request.create'

    @property
    def _requests_parameters(self):
        res = super(CreatePurchaseRequest, self)._requests_parameters
        if self.start.warehouses:
            res.update({
                    'warehouses': self.start.warehouses
                    })
        return res
