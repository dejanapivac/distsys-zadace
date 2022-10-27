import asyncio
import os

async def afun1(file_list):
    await asyncio.sleep(0.2)
    return [{"naziv": file, "velicina": os.path.getsize(file)} for file in file_list]


def fun2(file_list):
    for file in file_list:
        with open(file, "w") as inputfile:
            for i in range(1, 10001):
                inputfile.write(str(i))
                inputfile.write(" ")


async def main():
    file_list = []
    for file_number in range(1, 4):
        file_name = "datoteka{}".format(file_number)
        file_handler = open(file_name, "w")
        file_list.append(file_name)
    file_handler.close()
    fun1 = asyncio.create_task(afun1(file_list))
    fun2(file_list)
    result = await asyncio.gather(fun1)
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
