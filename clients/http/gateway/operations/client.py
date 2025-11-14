from typing import TypedDict, List

from httpx import Response

from clients.http.client import HTTPClient, QueryParams
from clients.http.gateway.client import build_gateway_http_client

from clients.http.gateway.operations.schema import (
    GetOperationQuerySchema,
    GetOperationsResponseSchema,
    GetOperationResponseSchema,
    GetOperationReceiptResponseSchema,
    GetOperationSummaryResponseSchema,
    MakeFeeOperationRequestSchema,
    MakeFeeOperationResponseSchema,
    MakeTopUpOperationRequestSchema,
    MakeTopUpOperationResponseSchema,
    MakeCashbackOperationRequestSchema,
    MakeCashbackOperationResponseSchema,
    MakeTransferOperationRequestSchema,
    MakeTransferOperationResponseSchema,
    MakePurchaseOperationRequestSchema,
    MakePurchaseOperationResponseSchema,
    MakeBillPaymentOperationRequestSchema,
    MakeBillPaymentOperationResponseSchema,
    MakeCashWithdrawalOperationRequestSchema,
    MakeCashWithdrawalOperationResponseSchema,
)


class OperationsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/operations сервиса http-gateway.
    """

    def get_operations_api(self, query: GetOperationQuerySchema) -> Response:
        """
        Выполняет GET-запрос на получение списка операций пользователя.

        :param query: Словарь с параметрами запроса, например: {'accountId': '123'}.
        :return: Объект httpx.Response с данными о счетах.
        """
        return self.get(
            "/api/v1/operations", params=QueryParams(**query.model_dump(by_alias=True))
        )

    def get_operations(self, account_id: str) -> GetOperationsResponseSchema:
        response = self.get_operations_api(account_id)
        return GetOperationsResponseSchema.model_validate_json(response.text)

    def get_operation_api(self, operation_id: str) -> Response:
        """
        Получение информации об операции по operation_id.

        :param operation_id: Идентификатор операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/operations/{operation_id}")

    def get_operation(self, operation_id: str) -> GetOperationResponseSchema:
        response = self.get_operation_api(operation_id)
        return GetOperationResponseSchema.model_validate_json(response.text)

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Получение чека по операции по operation_id

        :param operation_id: Идентификатор операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/operations/operation-receipt/{operation_id}")

    def get_operation_receipt(
        self, operation_id: str
    ) -> GetOperationReceiptResponseSchema:
        response = self.get_operation_receipt_api(operation_id)
        return GetOperationReceiptResponseSchema.model_validate_json(response.text)

    def get_operation_summary_api(self, query: GetOperationQuerySchema) -> Response:
        """
        Получение статистики по операциям для определенного счета.

        :param operation_id: Идентификатор операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(
            f"/api/v1/operations/operations-summary",
            params=QueryParams(**query.model_dump(by_alias=True)),
        )

    def get_operation_summary(
        self, account_id: str
    ) -> GetOperationSummaryResponseSchema:
        response = self.get_operation_summary_api(account_id)
        return GetOperationSummaryResponseSchema.model_validate_json(response.text)

    def make_fee_operation_api(
        self, request: MakeFeeOperationRequestSchema
    ) -> Response:
        """
        Выполняет POST-запрос для создание операции комиссии.

        :param request: Словарь с accountId, cardId, суммой операции и статусом.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post(
            "/api/v1/operations/make-fee-operation",
            json=request.model_dump(by_alias=True),
        )

    def make_fee_operation(
        self, account_id: str, card_id: str
    ) -> MakeFeeOperationResponseSchema:
        request = MakeFeeOperationRequestSchema(cardId=card_id, accountId=account_id)
        response = self.make_fee_operation_api(request)
        return MakeFeeOperationResponseSchema.model_validate_json(response.text)

    def make_top_up_operation_api(
        self, request: MakeTopUpOperationRequestSchema
    ) -> Response:
        """
        Выполняет POST-запрос для создание операции пополнения.

        :param request: Словарь с accountId, cardId, суммой операции и статусом.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post(
            "/api/v1/operations/make-top-up-operation",
            json=request.model_dump(by_alias=True),
        )

    def make_top_up_operation(
        self, account_id: str, card_id: str
    ) -> MakeTopUpOperationResponseSchema:
        request = MakeTopUpOperationRequestSchema(card_id=card_id, account_id=account_id)
        response = self.make_top_up_operation_api(request)
        return MakeTopUpOperationResponseSchema.model_validate_json(response.text)

    def make_cashback_operation_api(
        self, request: MakeCashbackOperationRequestSchema
    ) -> Response:
        """
        Выполняет POST-запрос для создание операции кэшбека.

        :param request: Словарь с accountId, cardId, суммой операции и статусом.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post(
            "/api/v1/operations/make-cashback-operation",
            json=request.model_dump(by_alias=True),
        )

    def make_cashback_operation(
        self, account_id: str, card_id: str
    ) -> MakeCashbackOperationResponseSchema:
        request = MakeCashbackOperationRequestSchema(
            cardId=card_id, accountId=account_id
        )
        response = self.make_cashback_operation_api(request)
        return MakeCashbackOperationResponseSchema.model_validate_json(response.text)

    def make_transfer_operation_api(
        self, request: MakeTransferOperationRequestSchema
    ) -> Response:
        """
        Выполняет POST-запрос для создание операции перевода.

        :param request: Словарь с accountId, cardId, суммой операции и статусом.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post(
            "/api/v1/operations/make-transfer-operation",
            json=request.model_dump(by_alias=True),
        )

    def make_transfer_operation(
        self, account_id: str, card_id: str
    ) -> MakeTransferOperationResponseSchema:
        request = MakeTransferOperationRequestSchema(
            cardId=card_id, accountId=account_id
        )
        response = self.make_transfer_operation_api(request)
        return MakeTransferOperationResponseSchema.model_validate_json(response.text)

    def make_purchase_operation_api(
        self, request: MakePurchaseOperationRequestSchema
    ) -> Response:
        """
        Выполняет POST-запрос для создание операции покупки.

        :param request: Словарь с accountId, cardId, суммой операции, категории и статусом.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post(
            "/api/v1/operations/make-purchase-operation",
            json=request.model_dump(by_alias=True),
        )

    def make_purchase_operation(
        self, account_id: str, card_id: str
    ) -> MakePurchaseOperationResponseSchema:
        request = MakePurchaseOperationRequestSchema(
            cardId=card_id,
            accountId=account_id,
        )
        response = self.make_purchase_operation_api(request)
        return MakePurchaseOperationResponseSchema.model_validate_json(response.text)

    def make_bill_payment_operation_api(
        self, request: MakeBillPaymentOperationRequestSchema
    ) -> Response:
        """
        Выполняет POST-запрос для создание операции оплаты по счету.

        :param request: Словарь с accountId, cardId, суммой операции и статусом.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post(
            "/api/v1/operations/make-bill-payment-operation",
            json=request.model_dump(by_alias=True),
        )

    def make_bill_payment_operation(
        self, account_id: str, card_id: str
    ) -> MakeBillPaymentOperationResponseSchema:
        request = MakeBillPaymentOperationRequestSchema(
            cardId=card_id, accountId=account_id
        )
        response = self.make_bill_payment_operation_api(request)
        return MakeBillPaymentOperationResponseSchema.model_validate_json(response.text)

    def make_cash_withdrawal_operation_api(
        self, request: MakeCashWithdrawalOperationRequestSchema
    ) -> Response:
        """
        Выполняет POST-запрос для создание операции снятия наличных денег.

        :param request: Словарь с accountId, cardId, суммой операции и статусом.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post(
            "/api/v1/operations/make-cash-withdrawal-operation",
            json=request.model_dump(by_alias=True),
        )

    def make_cash_withdrawal_operation(
        self, account_id: str, card_id: str
    ) -> MakeCashWithdrawalOperationResponseSchema:
        request = MakeCashWithdrawalOperationRequestSchema(
            cardId=card_id, accountId=account_id
        )
        response = self.make_cash_withdrawal_operation_api(request)
        return MakeCashWithdrawalOperationResponseSchema.model_validate_json(
            response.text
        )


def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Функция создаёт экземпляр UsersGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию UsersGatewayHTTPClient.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())
