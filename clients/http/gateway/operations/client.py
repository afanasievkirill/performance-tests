from typing import TypedDict, List

from httpx import Response

from clients.http.client import HTTPClient, QueryParams
from clients.http.gateway.client import build_gateway_http_client


class OperationDict(TypedDict):
    """
    Структура данных операции
    """

    id: str
    type: str
    status: str
    amount: float
    cardId: str
    category: str
    createdAt: str
    accountId: str


class OperationReceiptDict(TypedDict):
    """
    Структура данных получения документа по операции
    """

    url: str
    document: str


class GetOperationQueryDict(TypedDict):
    """
    Структура данных для получения списка операций.
    """

    accountId: str


class OperationsSummaryDict(TypedDict):
    """
    Структура данных по балансу операции
    """

    spentAmount: float
    receivedAmount: float
    cashbackAmount: float


class MakeOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции по счету.
    """

    status: str
    amount: float
    cardId: str
    accountId: str

class MakeFeeOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции платежа по счету.
    """

    status: str
    amount: float
    cardId: str
    accountId: str


class MakeTopUpOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции платежа по счету.
    """

    status: str
    amount: float
    cardId: str
    accountId: str

class MakeCashbackOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции кэшбека по счету.
    """

    status: str
    amount: float
    cardId: str
    accountId: str


class MakeTransferOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции кэшбека по счету.
    """

    status: str
    amount: float
    cardId: str
    accountId: str

class MakeBillPaymentOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции кэшбека по счету.
    """

    status: str
    amount: float
    cardId: str
    accountId: str


class MakeCashWithdrawalOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции кэшбека по счету.
    """

    status: str
    amount: float
    cardId: str
    accountId: str


class MakePurchaseOperationRequestDict(MakeOperationRequestDict):
    """
    Структура данных для совершения покупки.
    """

    category: str


class GetOperationsResponseDict(TypedDict):
    """
    Структура ответа на получение списка операции
    """

    operations: List[OperationDict]


class GetOperationResponseDict(TypedDict):
    """
    Структура ответа на получение операции
    """

    operations: OperationDict


class GetOperationReceiptResponseDict(TypedDict):
    """
    Структура ответа на получение чека
    """

    receipt: OperationReceiptDict


class GetOperationSummaryResponseDict(TypedDict):
    """
    Структура ответа на получение баланса по операциям
    """

    summary: OperationsSummaryDict


class MakeFeeOperationResponseDict(TypedDict):
    """
    Структура ответа на пополнении баланса
    """

    operation: OperationDict

class MakeTopUpOperationResponseDict(TypedDict):
    """
    Структура ответа на  пополнении баланса
    """

    operation: OperationDict


class MakeCashbackOperationResponseDict(TypedDict):
    """
    Структура ответа на  пополнении баланса
    """

    operation: OperationDict


class MakeTransferOperationResponseDict(TypedDict):
    """
    Структура ответа на первод
    """

    operation: OperationDict


class MakePurchaseOperationResponseDict(TypedDict):
    """
    Структура ответа на покупку
    """

    operation: OperationDict

class MakeBillPaymentOperationResponseDict(TypedDict):
    """
    Структура ответа на оплату счета
    """

    operation: OperationDict


class MakeCashWithdrawalOperationResponseDict(TypedDict):
    """
    Структура ответа на оплату счета
    """

    operation: OperationDict

class OperationsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/operations сервиса http-gateway.
    """

    def get_operations_api(self, query: GetOperationQueryDict) -> Response:
        """
        Выполняет GET-запрос на получение списка операций пользователя.

        :param query: Словарь с параметрами запроса, например: {'accountId': '123'}.
        :return: Объект httpx.Response с данными о счетах.
        """
        return self.get("/api/v1/operations", params=QueryParams(**query))

    def get_operations(self, account_id: str) -> GetOperationsResponseDict:
        response = self.get_operations_api(account_id)
        return response.json()

    def get_operation_api(self, operation_id: str) -> Response:
        """
        Получение информации об операции по operation_id.

        :param operation_id: Идентификатор операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/operations/{operation_id}")

    def get_operation(self, operation_id: str) -> GetOperationResponseDict:
        response = self.get_operation_api(operation_id)
        return response.json()

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Получение чека по операции по operation_id

        :param operation_id: Идентификатор операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/operations/operation-receipt/{operation_id}")

    def get_operation_receipt(
        self, operation_id: str
    ) -> GetOperationReceiptResponseDict:
        response = self.get_operation_receipt_api(operation_id)
        return response.json()

    def get_operation_summary_api(self, query: GetOperationQueryDict) -> Response:
        """
        Получение статистики по операциям для определенного счета.

        :param operation_id: Идентификатор операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(
            f"/api/v1/operations/operations-summary", params=QueryParams(**query)
        )

    def get_operation_summary(self, account_id: str) -> GetOperationSummaryResponseDict:
        response = self.get_operation_summary_api(account_id)
        return response.json()

    def make_fee_operation_api(self, request: MakeFeeOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создание операции комиссии.

        :param request: Словарь с accountId, cardId, суммой операции и статусом.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-fee-operation", json=request)
    
    def make_fee_operation(self, account_id: str, card_id: str) -> MakeFeeOperationResponseDict:
        request = MakeFeeOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )  
        response = self.make_fee_operation_api(request)
        return response.json()

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создание операции пополнения.

        :param request: Словарь с accountId, cardId, суммой операции и статусом.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-top-up-operation", json=request)
    
    def make_top_up_operation(self, account_id: str, card_id: str) -> MakeTopUpOperationResponseDict:
        request = MakeTopUpOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )  
        response = self.make_top_up_operation_api(request)
        return response.json()

    def make_cashback_operation_api(
        self, request: MakeCashbackOperationRequestDict
    ) -> Response:
        """
        Выполняет POST-запрос для создание операции кэшбека.

        :param request: Словарь с accountId, cardId, суммой операции и статусом.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-cashback-operation", json=request)
    
    def make_cashback_operation(self, account_id: str, card_id: str) -> MakeCashbackOperationResponseDict:
        request = MakeCashbackOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )  
        response = self.make_cashback_operation_api(request)
        return response.json()

    def make_transfer_operation_api(
        self, request: MakeTransferOperationRequestDict
    ) -> Response:
        """
        Выполняет POST-запрос для создание операции перевода.

        :param request: Словарь с accountId, cardId, суммой операции и статусом.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-transfer-operation", json=request)
    
    def make_transfer_operation(self, account_id: str, card_id: str) -> MakeTransferOperationResponseDict:
        request = MakeTransferOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )  
        response = self.make_transfer_operation_api(request)
        return response.json()

    def make_purchase_operation_api(
        self, request: MakePurchaseOperationRequestDict
    ) -> Response:
        """
        Выполняет POST-запрос для создание операции покупки.

        :param request: Словарь с accountId, cardId, суммой операции, категории и статусом.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-purchase-operation", json=request)


    def make_purchase_operation(self, account_id: str, card_id: str) -> MakePurchaseOperationResponseDict:
        request = MakePurchaseOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id,
            category="Taxi"
        )  
        response = self.make_purchase_operation_api(request)
        return response.json()
    
    def make_bill_payment_operation_api(
        self, request: MakeBillPaymentOperationRequestDict
    ) -> Response:
        """
        Выполняет POST-запрос для создание операции оплаты по счету.

        :param request: Словарь с accountId, cardId, суммой операции и статусом.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request)
    

    def make_bill_payment_operation(self, account_id: str, card_id: str) -> MakeBillPaymentOperationResponseDict:
        request = MakeBillPaymentOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )  
        response = self.make_bill_payment_operation_api(request)
        return response.json()

    def make_cash_withdrawal_operation_api(
        self, request: MakeCashWithdrawalOperationRequestDict
    ) -> Response:
        """
        Выполняет POST-запрос для создание операции снятия наличных денег.

        :param request: Словарь с accountId, cardId, суммой операции и статусом.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post(
            "/api/v1/operations/make-cash-withdrawal-operation", json=request
        )
    
    def make_cash_withdrawal_operation(self, account_id: str, card_id: str) -> MakeCashWithdrawalOperationResponseDict:
        request = MakeCashWithdrawalOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )  
        response = self.make_cash_withdrawal_operation_api(request)
        return response.json()


def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Функция создаёт экземпляр UsersGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию UsersGatewayHTTPClient.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())
