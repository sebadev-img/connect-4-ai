import sys
import time
import random
import json
import asyncio
import websockets

import connect4
import simple_ai
import minimax_ai

async def send(websocket, action, data):
    message = json.dumps(
        {
            'action': action,
            'data': data,
        }
    )
    await websocket.send(message)


async def start(auth_token,ai_name):
    uri = "ws://codechallenge-server-f4118f8ea054.herokuapp.com/ws?token={}".format(auth_token)
    while True:
        try:
            print('connection to {}'.format(uri))
            async with websockets.connect(uri) as websocket:
                print('connection READY!')
                await play(websocket,ai_name)
        except KeyboardInterrupt:
            print('Exiting...')
            break
        except Exception:
            print('connection error!')
            time.sleep(3)

async def play(websocket,ai_name):
    while True:
        try:
            response = await websocket.recv()
            print(f"< {response}")
            response_data = json.loads(response)
            print(f"response data: {response_data}")
            if response_data['event'] == 'update_user_list':
                pass
            if response_data['event'] == 'game_over':
                board = response_data['data']['board']
                print(board)
            if response_data['event'] == 'challenge':
                await send(
                    websocket,
                    'accept_challenge',
                    {
                        'challenge_id': response_data['data']['challenge_id'],
                    },
                )
            if response_data['event'] == 'your_turn':
                #await process_your_turn(websocket, response_data)
                asyncio.create_task(process_your_turn(websocket,ai_name,response_data))
        except KeyboardInterrupt:
            print('Exiting...')
            break
        except Exception as e:
            print('error {}'.format(str(e)))
            break  # force login again

async def process_your_turn(websocket,ai_name,response_data):
    side = response_data['data']['side']
    piece = connect4.get_piece_from_side(side)
    string_board = response_data['data']['board']
    board = connect4.create_board_from_string(string_board)
    drop_col,kill_row,kill_col = get_ai_move(ai_name,board,piece)
    print(string_board)
    if drop_col is not None: 
        drop_col = int(drop_col)   
        await process_move(websocket,response_data,drop_col)
    elif kill_row is not None:
        kill_row = connect4.get_reverse_row(board,kill_row)
        await process_kill_row(websocket,response_data,kill_row)
    elif kill_col is not None:
        kill_col = int(kill_col)
        await process_kill_col(websocket,response_data,kill_col)


def get_ai_move(ai_name,board,piece):
    if ai_name == "simple":
        return simple_ai.get_move(board,piece)
    elif ai_name == "alphabeta":
        drop_col = minimax_ai.get_move(board,piece)
        return drop_col,None,None
    pass


async def process_move(websocket,response_data,col):     
    await send(
        websocket,
        'move',
        {
            'game_id': response_data['data']['game_id'],
            'turn_token': response_data['data']['turn_token'],
            'col': col,
        },
    )

async def process_kill_col(websocket, request_data,col):
    await send(
        websocket,
        'kill',
        {
            'game_id': request_data['data']['game_id'],
            'turn_token': request_data['data']['turn_token'],
            'col': col
        },
    )

async def process_kill_row(websocket, request_data,row):
    await send(
        websocket,
        'kill',
        {
            'game_id': request_data['data']['game_id'],
            'turn_token': request_data['data']['turn_token'],
            'row': row
        },
    )
 


if __name__ == '__main__':
    if len(sys.argv) >= 2:
        auth_token = sys.argv[1]
        ai_name = sys.argv[2]
        print(f"AI {ai_name} started with token id: {auth_token}")
        asyncio.run(start(auth_token,ai_name))       
    else:
        print('please provide your auth_token')