from typing import Optional

from pydantic import BaseModel, EmailStr, validator


class UserBaseSchema(BaseModel):
    id: Optional[int] = None
    name: Optional[str]
    email: EmailStr

    class Config:
        orm_mode = True

    @validator("name")
    def full_name_must_have_3_characters(cls, value):
        if len(value) < 3:
            raise ValueError("Nome completo deve ter no mínimo 3 caracteres")
        return value.capitalize()

    @validator("email")
    def email_should_be_valid(cls, value):
        if "@" not in value:
            raise ValueError("E-mail inválido")
        return value


class UserSchemaCreate(UserBaseSchema):
    password: str
