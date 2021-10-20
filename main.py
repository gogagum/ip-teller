from src.bot import Bot
import logging
import time

if __name__ == "__main__":
    while True:
        try:
            bot = Bot()
            bot.infinity_polling()
        except Exception as e:
            # In case of internet error try starting again
            logging.debug(e)
            print(e)
            time.sleep(5)
