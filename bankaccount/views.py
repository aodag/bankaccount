from z3c.form import form, field
from zope.schema import Int
from zope.interface import Interface
from zope.globalrequest import getRequest
from plone.z3cform import layout


class IDepositSchema(Interface):
    amount = Int(min=0)


class IWithhdrawSchema(Interface):
    amount = Int(min=0)


class DepositForm(form.Form):
    fields = field.Fields(IDepositSchema)
    ignoreContext = True

    @form.button.buttonAndHandler("deposit")
    def deposit(self, action):
        data, errors = self.extractData()
        if errors:
            return
        amount = data["amount"]
        self.context.deposit(amount)
        return getRequest().response.redirect(self.context.absolute_url())


class WithdrawForm(form.Form):
    fields = field.Fields(IDepositSchema)
    ignoreContext = True

    @form.button.buttonAndHandler("withdraw")
    def withdraw(self, action):
        data, errors = self.extractData()
        if errors:
            return
        amount = data["amount"]
        self.context.withdraw(amount)
        return getRequest().response.redirect(self.context.absolute_url())


DepositFormView = layout.wrap_form(DepositForm)
WithdrawFormView = layout.wrap_form(WithdrawForm)
