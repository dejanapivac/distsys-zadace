import asyncio
import numpy as numpy
import psutil as psutil


async def afun1():
    for i in range(10):
        numpy.random.normal(0.0, 1.0, 1000000)
        await asyncio.sleep(0.9)


async def afun2():
    return psutil.cpu_percent(10)


async def main():
    await afun1()
    result = await afun2()
    print("Iskoristenost CPU-a u 10 sekundi iznosi: ", result)


if __name__ == "__main__":
    asyncio.run(main())
