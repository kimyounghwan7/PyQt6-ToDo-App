from app.gui.main_view import main_view
from loguru import logger

logger.add("app.log", rotation="10 MB")

def main():
	try:
		logger.info("Starting the application...")
		main_view()
		logger.info("Application exited successfully.")
	except Exception as e:
		logger.error(f"An error occurred: {e}")
		logger.exception("msg")
		exit(1)

if __name__ == "__main__":
	main()
