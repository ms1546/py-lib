import asyncio
import random
from datetime import datetime, timedelta

async def data_source(source_id: int, data_queue: asyncio.Queue):
    """非同期データソースからデータを生成"""
    while True:
        await asyncio.sleep(random.randint(1, 5))
        data = {
            'source_id': source_id,
            'timestamp': datetime.now(),
            'value': random.randint(1, 100)
        }
        await data_queue.put(data)

async def data_processor(data_queue: asyncio.Queue, processed_queue: asyncio.Queue):
    """データのフィルタリングと変換"""
    while True:
        data = await data_queue.get()
        if data['value'] > 50:
            data['value'] = data['value'] * 2  # 変換例
            await processed_queue.put(data)

async def data_aggregator(processed_queue: asyncio.Queue, aggregation_interval: int):
    """データ集約と統計分析"""
    aggregation_data = []
    start_time = datetime.now()
    while True:
        data = await processed_queue.get()
        aggregation_data.append(data['value'])

        if (datetime.now() - start_time) >= timedelta(seconds=aggregation_interval):
            if aggregation_data:
                avg_value = sum(aggregation_data) / len(aggregation_data)
                max_value = max(aggregation_data)
                print(f"Aggregated Data - Avg: {avg_value}, Max: {max_value}")
                aggregation_data = []  # リセット
            start_time = datetime.now()

async def database_writer(processed_queue: asyncio.Queue):
    """データベースへの非同期書き込み"""
    while True:
        data = await processed_queue.get()
        print(f"Writing to database: {data}")

async def alert_system(processed_queue: asyncio.Queue, threshold: int):
    """アラート生成システム"""
    while True:
        data = await processed_queue.get()
        if data['value'] > threshold:
            print(f"Alert! Value exceeded threshold: {data}")

async def main():
    data_queue = asyncio.Queue()
    processed_queue = asyncio.Queue()

    data_sources = [asyncio.create_task(data_source(i, data_queue)) for i in range(3)]

    processor_task = asyncio.create_task(data_processor(data_queue, processed_queue))

    aggregator_task = asyncio.create_task(data_aggregator(processed_queue, 10))

    db_writer_task = asyncio.create_task(database_writer(processed_queue))

    alert_task = asyncio.create_task(alert_system(processed_queue, 150))

    await asyncio.gather(*data_sources, processor_task, aggregator_task, db_writer_task, alert_task)

asyncio.run(main())
