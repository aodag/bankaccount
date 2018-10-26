import logging

from AccessControl.class_init import InitializeClass
from AccessControl.security import ClassSecurityInfo
from OFS.owner import Owned
from OFS.SimpleItem import SimpleItem
from Products.PageTemplates.PageTemplateFile import PageTemplateFile

from zope.globalrequest import getRequest
from zope.interface import implementer

from .interfaces import IBankAccount

logger = logging.getLogger(__name__)
manage_AddBankAccountForm = PageTemplateFile(
    "browser/manage_AddBankAccountForm.zpt", globals()
)


def manage_AddBankAccount(context, id):
    """ Add BankAccount object"""
    o = BankAccount(id)
    context._setObject(o.getId(), o)
    request = getRequest()
    return request.response.redirect(o.absolute_url())


@implementer(IBankAccount)
class BankAccount(SimpleItem):
    meta_type = "Bank Account"
    security = ClassSecurityInfo()

    manage_options = SimpleItem.manage_options + Owned.manage_options

    def __init__(self, id):
        self.id = id
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, new_balance):
        logger.info("update balance %s", new_balance)
        if new_balance < 0:
            raise ValueError(new_balance)
        self._balance = new_balance

    @security.private
    def deposit(self, amount):
        logger.info("deposit %s", amount)
        self.balance += amount

    @security.private
    def withdraw(self, amount):
        logger.info("withdraw %s", amount)
        self.balance -= amount


InitializeClass(BankAccount)
