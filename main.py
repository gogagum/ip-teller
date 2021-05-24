from src.bot import bot
import logging

if __name__ == "__main__":
    while True:
        try:
            bot.polling(timeout=200)
        except Exception as err:
            # In case of internet error try starting again
            logging.debug(err)
            time.sleep(5)
