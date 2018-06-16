#!/usr/bin/env python3

import argparse
import asyncio
from time import gmtime, strftime
import websockets

argparser = argparse.ArgumentParser(description='Listens for events from deCONZ websocket')
argparser.add_argument('-t', '--time', action='store_true', help='Prints the time of each event')
argparser.add_argument('-H', '--host', help='Hostname or IP of gw')
args = argparser.parse_args()

if not args.host:
  argparser.print_help()
  exit(1)

async def wslisten():
  async with websockets.connect('ws://' + args.host + ':443') as websocket:
    async for message in websocket:
      if args.time:
        print(strftime("%Y-%m-%d %H:%M:%S", gmtime()) + ' ' + message) 
      else:
        print(message)

asyncio.get_event_loop().run_until_complete(wslisten())
