from typing import TypedDict

from httpx import Response

from clients.http.client import HTTPClient, QueryParams


class GetOperationQueryDict(TypedDict):
    """
    Структура данных для получения списка операций.
    """
    accountId: str

class MakeOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции по счету.
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


class OperationsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/operations сервиса http-gateway.
    """

    def get_operation_api(self, operation_id: str) -> Response:
        """
        Получение информации об операции по operation_id.

        :param operation_id: Идентификатор операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/operations/{operation_id}")
    

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Получение чека по операции по operation_id

        :param operation_id: Идентификатор операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/operations/operation-receipt/{operation_id}")
    
    def get_operation__api(self, query: GetOperationQueryDict) -> Response:
        """
        Получение чека по операции по аккаунту

        :param operation_id: Идентификатор операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/operations", params=QueryParams(**query))
    
    def get_operation_receipt_api(self, query:GetOperationQueryDict) -> Response:
        """
        Получение статистики по операциям для определенного счета.

        :param operation_id: Идентификатор операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/operations/operations-summary", params=QueryParams(**query))
    
    def make_fee_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создание операции комиссии.

        :param request: Словарь с accountId, cardId, суммой операции и статусом.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-fee-operation", json=request)
    
    def make_top_up_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создание операции пополнения.

        :param request: Словарь с accountId, cardId, суммой операции и статусом.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-top-up-operation", json=request)
    
    def make_cashback_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создание операции кэшбека.

        :param request: Словарь с accountId, cardId, суммой операции и статусом.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-cashback-operation", json=request)
    
    def make_transfer_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создание операции перевода.

        :param request: Словарь с accountId, cardId, суммой операции и статусом.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-transfer-operation", json=request)
    
    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создание операции покупки.

        :param request: Словарь с accountId, cardId, суммой операции, категории и статусом.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-purchase-operation", json=request)
    
    def make_bill_payment_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создание операции оплаты по счету.

        :param request: Словарь с accountId, cardId, суммой операции и статусом.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request)
    
    def make_cash_withdrawal_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создание операции снятия наличных денег.

        :param request: Словарь с accountId, cardId, суммой операции и статусом.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-cash-withdrawal-operation", json=request)