import logging
from . import bankaccount

logger = logging.getLogger(__name__)


def initialize(registrar):
    logger.info("register package %s", __name__)
    constructors = (
        bankaccount.manage_AddBankAccountForm,
        bankaccount.manage_AddBankAccount,
    )
    registrar.registerClass(bankaccount.BankAccount, constructors=constructors)
