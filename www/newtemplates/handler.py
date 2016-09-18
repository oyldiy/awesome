#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re, time, json, logging, hashlib, base64, asyncio

from coroweb import get, post

def check_admin(request):
    if request.__user__ is None or not request.__user__.admin:
        raise APIPermissionError()


@get('/')
async def index(*, page='1'):

    return {
        '__template__': 'blogs.html',
        'page': page,
        'blogs': blogs
    }
