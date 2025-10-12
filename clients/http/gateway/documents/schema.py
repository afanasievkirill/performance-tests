from pydantic import BaseModel


# Добавили суффикс Schema вместо Dict
class DocumentSchema(BaseModel):
    """
    Описание структуры документа.
    """

    url: str
    document: str


class GetTariffDocumentResponseSchema(BaseModel):
    """
    Описание структуры ответа получения тарифа.
    """

    tariff: DocumentSchema


class GetContractDocumentResponseSchema(BaseModel):
    """
    Описание структуры ответа получения контракта.
    """

    contract: DocumentSchema
