import time
import os
import logging
import hvac

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())


def wait_for_vault():
    client = hvac.Client(url=os.getenv('VAULT_URL'))

    logger.info('Waiting vault')
    while client.sys.is_sealed():
        time.sleep(5)
    logger.info('Vault is unsealed')


wait_for_vault()
