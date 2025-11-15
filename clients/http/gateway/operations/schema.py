from datetime import date
from enum import StrEnum
from typing import List

from pydantic import BaseModel, ConfigDict, Field

from tools.fakers import fake


class OperationType(StrEnum):
    FEE = "FEE"
    TOP_UP = "TOP_UP"
    PURCHASE = "PURCHASE"
    CASHBACK = "CASHBACK"
    TRANSFER = "TRANSFER"
    BILL_PAYMENT = "BILL_PAYMENT"
    CASH_WITHDRAWAL = "CASH_WITHDRAWAL"


class OperationStatus(StrEnum):
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"
    IN_PROGRESS = "IN_PROGRESS"
    UNSPECIFIED = "UNSPECIFIED"


class OperationSchema(BaseModel):
    """
    Структура данных операции
    """

    model_config = ConfigDict(populate_by_name=True)

    id: str
    type: OperationType
    status: OperationStatus
    amount: float
    card_id: str = Field(alias="cardId")
    category: str
    created_at: str = Field(alias="createdAt")
    account_id: str = Field(alias="accountId")


class OperationReceiptSchema(BaseModel):
    """
    Структура данных получения документа по операции
    """

    url: str
    document: str


class OperationsSummarySchema(BaseModel):
    """
    Структура данных по балансу операции
    """

    model_config = ConfigDict(populate_by_name=True)

    spent_amount: float = Field(alias="spentAmount")
    received_amount: float = Field(alias="receivedAmount")
    cashback_amount: float = Field(alias="cashbackAmount")


class GetOperationQuerySchema(BaseModel):
    """
    Структура данных для получения списка операций.
    """

    model_config = ConfigDict(populate_by_name=True)
    account_id: str = Field(alias="accountId")


class GetOperationsResponseSchema(BaseModel):
    """
    Структура ответа на получение списка операции
    """

    operations: List[OperationSchema]


class GetOperationResponseSchema(BaseModel):
    """
    Структура ответа на получение списка операции
    """

    operations: OperationSchema


class GetOperationReceiptResponseSchema(BaseModel):
    """
    Структура ответа на получение чека
    """

    operations: OperationReceiptSchema


class GetOperationSummaryResponseSchema(BaseModel):
    """
    Структура ответа на получение баланса по операциям
    """

    summary: OperationsSummarySchema


class MakeFeeOperationRequestSchema(BaseModel):
    """
    Структура данных для создания операции платежа по счету.
    """

    model_config = ConfigDict(populate_by_name=True)
    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.float)
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeFeeOperationResponseSchema(BaseModel):
    """
    Структура ответа на пополнении баланса
    """

    operation: OperationSchema


class MakeTopUpOperationRequestSchema(BaseModel):
    """
    Структура данных для создания операции платежа по счету.
    """

    model_config = ConfigDict(populate_by_name=True)
    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.float)
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeTopUpOperationResponseSchema(BaseModel):
    """
    Структура ответа на пополнении баланса
    """

    operation: OperationSchema


class MakeCashbackOperationRequestSchema(BaseModel):
    """
    Структура данных для создания операции кэшбека по счету.
    """

    model_config = ConfigDict(populate_by_name=True)
    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.float)
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeCashbackOperationResponseSchema(BaseModel):
    """
    Структура ответа операции кэшбека по счету
    """

    operation: OperationSchema


class MakeTransferOperationRequestSchema(BaseModel):
    """
    Структура данных для создания перевода между счетами.
    """

    model_config = ConfigDict(populate_by_name=True)
    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.float)
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeTransferOperationResponseSchema(BaseModel):
    """
    Структура ответа операции перевода денежных средств между счетами.
    """

    operation: OperationSchema


class MakePurchaseOperationRequestSchema(BaseModel):
    """
    Структура данных для совершения покупки.
    """

    model_config = ConfigDict(populate_by_name=True)
    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.float)
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")
    category: str = Field(default_factory=fake.category)


class MakePurchaseOperationResponseSchema(BaseModel):
    """
    Структура ответа на покупку
    """

    operation: OperationSchema


class MakeBillPaymentOperationRequestSchema(BaseModel):
    """
    Структура данных для орлаты счета.
    """

    model_config = ConfigDict(populate_by_name=True)
    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.float)
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeBillPaymentOperationResponseSchema(BaseModel):
    """
    Структура ответа на оплату счетаю
    """

    operation: OperationSchema


class MakeCashWithdrawalOperationRequestSchema(BaseModel):
    """
    Структура данных для создания операции кэшбека по счету.
    """

    model_config = ConfigDict(populate_by_name=True)
    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.float)
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeCashWithdrawalOperationResponseSchema(BaseModel):
    """
    Структура ответа на операции кэшбека по счету.
    """

    operation: OperationSchema
