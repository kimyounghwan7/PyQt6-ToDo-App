from app.gui.main_view import app
from loguru import logger

logger.add("app.log", rotation="10 MB")

def main():
	try:
		app.exec()
	except Exception as e:
		logger.error(f"An error occurred: {e}")


if __name__ == "__main__":
	main()
