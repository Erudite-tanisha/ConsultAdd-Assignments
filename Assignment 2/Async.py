import asyncio

async def say_hello_async():
    await asyncio.sleep(2)  
    print("Hello, Async World!")

async def do_something_else():
    print("Starting another task...")
    await asyncio.sleep(1)
    print("Finished another task!")

async def main():
    
    await asyncio.gather(
        say_hello_async(),
        do_something_else(),
    )

asyncio.run(main())