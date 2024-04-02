import asyncio
import aiohttp
import aiofiles
import os


async def get_pic(num, directory_path, session):
    url = "https://source.unsplash.com/random"
    async with session.get(url) as response:
        if response.status == 200:
            async with aiofiles.open(f"{directory_path}/image{num}.jpg", "wb") as f:
                await f.write(await response.read())


async def download(num, directory_path):
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*(get_pic(i + 1, directory_path, session) for i in range(num)))


if __name__ == "__main__":
    num_of_pics = int(input("Number of pics to download:"))
    # output_directory = int(input("Path to directory:"))
    output_directory = "downloaded_images_Ex5_1"
    os.mkdir(output_directory)

    asyncio.run(download(num_of_pics, output_directory))
