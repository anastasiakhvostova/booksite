from fastapi import APIRouter, Request, Form, HTTPException, status, Depends, Response
from fastapi.templating import Jinja2Templates
from pydantic import EmailStr

from app import catalog_data
# from app.auth.auth_lib import AuthHandler, AuthLibrary
# from app.auth import dependencies


import dao

import settings


router = APIRouter(
    prefix='/web',
    tags=['menu', 'landing'],
)

templates = Jinja2Templates(directory='app\\templates')


@router.get('/menu')
async def get_menu(request: Request):
    context = {
        'request': request,
        'title': 'Наш каталог',
        'menu': catalog_data.menu

    }
    return templates.TemplateResponse(
        'catalog.html',
        context=context
    )
@router.post('/search')
# @router.get('/menu')
async def get_menu(request: Request, dish_name: str = Form(None)):
    filtered_menu = []
    if dish_name:
        for dish in catalog_data.menu:
            if dish_name.lower() in dish['title'].lower():
                filtered_menu.append(dish)

    context = {
        'request': request,
        'title': f'Результати пошуку за {dish_name}' if dish_name else 'Наше меню',
        'menu': filtered_menu if dish_name else catalog_data.menu,
        # 'user': user,
        # 'categories': catalog_data.Categories
    }

    return templates.TemplateResponse(
        'catalog.html',
        context=context,
    )


@router.get('/about-us')
async def about_us(request: Request):
    context = {
        'request': request,
        'title': 'Доставка і оплата',
    }

    return templates.TemplateResponse(
        'about_us.html',
        context=context,
    )


@router.get('/about-contact')
async def about_us(request: Request):
    context = {
        'request': request,
        'title': 'Магазини і контакти',
    }

    return templates.TemplateResponse(
        'about_contact.html',
        context=context,
    )


@router.get('/map')
async def map_drive(request: Request):
    context = {
        'request': request,
        'title': 'Карта проїзду',

    }

    return templates.TemplateResponse(
        'map.html',
        context=context,
    )
