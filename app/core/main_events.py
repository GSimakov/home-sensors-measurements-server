from typing import Callable
from fastapi import FastAPI
from loguru import logger



#todo fix api routes
def create_start_app_handler(
    app: FastAPI,
) -> Callable:
    async def start_app() -> None:
        pass
    return start_app


def create_stop_app_handler(
        app: FastAPI
) -> Callable:
    @logger.catch
    async def stop_app() -> None:
        pass
    return stop_app

