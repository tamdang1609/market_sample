import json

def read_market():
    # open data
    with open("market-data.json") as j:
        data = j.read()
    data = json.loads(data)
    for ladders in data['payload']['market_data']:  # the payload include all the market data ladder
        if ladders[0]['type'] == 'future':
            # print future data
            print("Future info")
            """
                    {
                        "exchange": "deribit",
                        "payoff": "base",
                        "expiry": "2021-06-18T08:00:00.000000Z",
                        "ccypair": {
                            "base": "BTC",
                            "term": "USD"
                        },
                        "type": "future"
                    }
            """
            print(ladders[0]['exchange'])
            print(ladders[0]['payoff'])
            print(ladders[0]['expiry'])
            print(ladders[0]['ccypair'])
            print(ladders[0]['type'])
            # bid ask ladder in second index
            print(ladders[1]['payload']['bids'])
            print(ladders[1]['payload']['asks'])
        elif ladders[0]['type'] == 'option':
            # print options data
            """
                    {
                        "exchange": "deribit",
                        "callput": "call",
                        "option_type": "vanilla",
                        "exercise_type": "european",
                        "payoff": "base",
                        "expiry": "2021-06-15T08:00:00.000000Z",
                        "ccypair": {
                            "base": "BTC",
                            "term": "USD"
                        },
                        "strike": 30000.0,
                        "type": "option"
                    }
            """
            # product info in the first index
            print("option info")
            print(ladders[0]['exchange'])
            print(ladders[0]['callput'])
            print(ladders[0]['option_type'])
            print(ladders[0]['exercise_type'])
            print(ladders[0]['payoff'])
            print(ladders[0]['expiry'])
            print(ladders[0]['ccypair'])
            print(ladders[0]['strike'])
            print(ladders[0]['type'])
            # bid ask ladder in second index
            print(ladders[1]['payload']['bids'])
            print(ladders[1]['payload']['asks'])
        elif ladders[0]['type'] == 'perpetual':
            # print pepertual data
            print("perpetual info")
            """
                    {
                        "exchange": "deribit",
                        "ccypair": {
                            "base": "BTC",
                            "term": "USD"
                        },
                        "type": "perpetual"
                    }
            """
            print("perpetual info")
            print(ladders[0]['exchange'])
            print(ladders[0]['ccypair'])
            print(ladders[0]['type'])
            # pepertual bid ask ladder
            print(ladders[1]['payload']['bids'])
            print(ladders[1]['payload']['asks'])
        elif ladders[0]['type'] == 'spot':
            # print pepertual data
            print(ladders[0])  # product info
            print(ladders[1]['payload'])  # spot bid ask ladder
        else:
            print("unsupported type")


"""
stream data from pricer endpoint 

/api/market-data/:exchange/:base/:term

example:

/api/market-data/deribit/btc/usd

"""
import websocket  # need to install websocket pip install websocket


def on_message(wsapp, message):
    msg = json.loads(message)
    if msg['condition']['status'] == 'good':
        with open("temp.json", "w") as f:
            f.write(json.dumps(msg))


def streaming_dat():
    """
    replace the ws endpoint to the pricer url.
    """
    wsapp = websocket.WebSocketApp("ws://localhost:3030/api/market-data/deribit/btc/usd",
                                   cookie="chocolate", on_message=on_message)
    wsapp.run_forever(origin="localhost", host="localhost")


if __name__ == "__main__":
    read_market()