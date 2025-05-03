from typing import Tuple
from uuid import UUID
from sqlmodel.ext.asyncio.session import AsyncSession

class BaseOperations:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def _create_one(
        self, obj, message: str = "Объект создан"
    ) -> Tuple[bool, str, UUID]:
        """
        Создание объекта в базе данных

        :param obj: класс объекта с данными
        :param message: сообщение о создании

        :return: статус, сообщение о создании
        """
        self.session.add(obj)
        await self.session.commit()
        await self.session.refresh(obj)

        return True, message, obj.uuid
    
    async def _create_all(
        self, objs, message: str = "Объекты созданы"
    ) -> Tuple[bool, str]:
        """
        Создание объектов в базе данных

        :param objs: список объектов с данными
        :param message: сообщение о создании

        :return: статус, сообщение о создании
        """
        for obj in objs:
            self.session.add(obj)
        await self.session.commit()

        return True, message 