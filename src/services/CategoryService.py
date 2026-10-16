from abc import ABC, abstractmethod
from typing import List

from src.dtos.CategoryDTO import CategoryDTO, CreateCategoryDTO, UpdateCategoryDTO


class CategoryService(ABC):

    @abstractmethod
    def get_all_categories(self) -> List[CategoryDTO]:
        pass

    @abstractmethod
    def create_category(self, dto: CreateCategoryDTO) -> CategoryDTO:
        pass

    @abstractmethod
    def update_category(self, dto: UpdateCategoryDTO) -> CategoryDTO:
        pass

    @abstractmethod
    def delete_category(self, category_id: int) -> None:
        pass
