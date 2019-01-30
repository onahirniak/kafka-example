import logging
import logging.config

def main():
	logging.config.fileConfig(fname='logging.conf', disable_existing_loggers=False)

	# Get the logger specified in the file
	logger = logging.getLogger('Producer')

	logging.debug('Starting producer.')
	logging.debug('Shutdown producer.')

main()


