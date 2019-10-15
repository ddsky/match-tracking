import asyncio, evdev

team1Defense = evdev.InputDevice('/dev/input/event3')
team1Offense = evdev.InputDevice('/dev/input/event5')
#team2Defense = evdev.InputDevice('/dev/input/event7')
#team2Offense = evdev.InputDevice('/dev/input/event9')

async def print_events(device):
    async for event in device.async_read_loop():
        if device.path == '/dev/input/event3':      
            print('team 1 offense goal')
        if device.path == '/dev/input/event5':      
            print('team 1 defense goal')

for device in team1Defense, team1Offense:
    asyncio.ensure_future(print_events(device))

loop = asyncio.get_event_loop()
loop.run_forever()
