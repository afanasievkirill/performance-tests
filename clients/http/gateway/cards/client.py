from typing import TypedDict

from httpx import Response

from clients.http.client import HTTPClient

class CreateCardRequestDict:
    """
    Структура данных для создания новой карты.
    """
    userId: str
    accountId: str

class CardsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/cards сервиса http-gateway.
    """

    def issue_virtual_card_api(self, request: CreateCardRequestDict) -> Response:
        """
        Создание новой виртуальной карты.
        Args:
            request (CreateCardRequestDict): словарь с данными о айди пользователя и айди аккаунта

        Returns:
            Response: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/cards/issue-virtual-card", json=request)
    
    def issue_physical_card_api(self, request: CreateCardRequestDict) -> Response:
        """
        Создание новой физической карты.
        Args:
            request (CreateCardRequestDict): словарь с данными о айди пользователя и айди аккаунта

        Returns:
            Response: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/cards/issue-physical-card", json=request)