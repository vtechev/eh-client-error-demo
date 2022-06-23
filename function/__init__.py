import azure.functions as func
import asyncio
import logging

from azure.identity import DefaultAzureCredential

from azure.eventhub.aio import EventHubConsumerClient


async def main(mytimer: func.TimerRequest, context: str) -> None:
    logging.info(f"Started function.")

