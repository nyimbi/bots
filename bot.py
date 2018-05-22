#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 ft=python
# Date              : 17.03.2018
# Last Modified Date: 17.03.2018

import os
import logging
import importlib
from telegram.ext import Updater
from telegram.ext.dispatcher import run_async
import config as cfg

# updater = Updater(token=os.environ.get('TG_TOKEN') or "")
updater = Updater(token=cfg.BOTKEY)
dp = updater.dispatcher

logging.basicConfig(format='[%(asctime)s][%(name)s][%(levelname)s] %(message)s',
	level=logging.INFO)

logger = logging.getLogger(__name__)

@run_async
def error_callback(bot, update, error):
	pass # p-t-b's logger already logs this to the console

def main():
	# for modname in ["compressor", "help", "ocr"]:
	for modname in ["ocr", "help"]:
		module = getattr(importlib.import_module('modules.{}'.format(modname)), "module") # from modules.modname import module
		logger.info("importing module: %s (handlers: %d)", module.name, len(module.handlers))
		for handler in module.handlers:
			dp.add_handler(handler)

	dp.add_error_handler(error_callback)

	updater.start_polling(clean=True)
	updater.idle()

if __name__ == '__main__':
	main()