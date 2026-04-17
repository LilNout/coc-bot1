import sys
import argparse
from bot.game_bot import GameBot

def main():
    parser = argparse.ArgumentParser(description="Clash of Clans Auto Farm Bot")
    parser.add_argument("--device", help="ADB Device ID")
    args = parser.parse_args()

    bot = GameBot(device_id=args.device)
    bot.run()

if __name__ == "__main__":
    main()
