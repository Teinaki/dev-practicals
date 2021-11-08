import asyncio
import aiofiles


async def reads():
    async with aiofiles.open('README.md', mode='r') as f:
        contents = await f.read()
    return contents

async def writes(contents):
    async with aiofiles.open('reversed.txt', mode='w') as f:
        await f.write(contents[::-1])
    return

async def main():
    files = await reads()
    await writes(files)
    

if __name__ == "__main__":
    asyncio.run(main())


#### Practical  23: Async IO
#To perform today's lab it will be necesary to `pip install sqlalchemy`.
#
#1. Write a program that reads in this README file to a list of lines and 
#then prints the text with the order of the lines reversed and the text
#in each line reversed. Use the `aiofiles` library to read and write the 
#files. The basic structure of your program should include
#  - a coroutine that reads in this README file
#  - a coroutine that writes the reversed output to a new file
#  - a coroutine that calls the ones above, chaining them together
#  - a main section that invokes `asyncio.run()`.
###