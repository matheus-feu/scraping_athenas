from fastapi import APIRouter, Depends
from sqlalchemy import select, and_
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from starlette.exceptions import HTTPException
from starlette.responses import JSONResponse

from app.core.deps import get_current_user
from app.db.session import get_session
from app.exceptions.exception_auth import NotAuthenticatedException
from app.helpers.scrappy import scrape_data
from app.models import UserModel
from app.models.products import ProductModel

router = APIRouter()


@router.get("/{category}")
async def get_products(category: str, current_user: UserModel = Depends(get_current_user),
                       db: AsyncSession = Depends(get_session)):
    """GET - Endpoint para receber a categoria do produto para realizar o scraping, enviado os params: phones ou computers
    :param category: str [required] - Categoria do produto
    """

    if not current_user:
        raise NotAuthenticatedException()

    category_mapping = {
        "phones": ["phones/touch"],
        "computers": ["computers/tablets", "computers/laptops"]
    }

    if category not in category_mapping:
        raise HTTPException(status_code=400, detail="Invalid category")

    categories = category_mapping[category]
    products = []

    for cat in categories:
        products += scrape_data(category=cat)

    async with db as session:
        try:
            for product in products:

                query = select(ProductModel).where(
                    and_(
                        ProductModel.name == product["title"],
                        ProductModel.description == product["description"],
                    )
                )
                result = await session.execute(query)
                existing_product = result.scalars().one_or_none()

                if existing_product:
                    existing_product.price = product["price"]
                    existing_product.image = product["image"]
                    existing_product.link = product["link"]
                    existing_product.description = product["description"]
                    existing_product.reviews = product["reviews"]
                else:
                    new_product = ProductModel(
                        name=product["title"],
                        price=product["price"],
                        image=product["image"],
                        link=product["link"],
                        description=product["description"],
                        reviews=product["reviews"],
                    )
                    session.add(new_product)
            await session.commit()
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    return JSONResponse(content=products, status_code=status.HTTP_200_OK)
