import logging
import simplejson
import os

logger = logging.getLogger('dw')

class plugin(object):

    author = 'wit0k'
    description = ''
    config_file = ''
    plugin_type = ''
    vendor_name = ''
    required_params = ['debug_proxies', 'submission_comments', 'requests_debug']
    config_data = {}

    def __init__(self):

            self.debug_proxies = {
                'http': 'http://127.0.0.1:8080',
                'https': 'http://127.0.0.1:8080'
            }

            self.submission_comments = ""
            self.requests_debug = False

    def load_config(self):

        if self.config_file == "":
            logger.debug('This plugin does not require config file')
            return True

        if self.config_file:
            logger.debug('Attempt to load_config(%s)' % self.config_file)

            if os.path.isfile(self.config_file):

                with open(self.config_file, 'r') as file:
                    try:
                        vendor_config = simplejson.load(file)
                        if vendor_config:
                            logger.debug('Successfully loaded JSON data')
                            self.config_data = vendor_config
                            return True
                        else:
                            logger.error('Failed to load config data. Contact plugin developer ')
                            return False
                    except Exception as msg:
                        logger.error('Failed to load config data. Contact plugin developer. Error: %s ' % str(msg))
                        return False

            else:
                logger.error('Config file not found!')
                return False

    def call(self, function_name, params=()):

        if function_name in self.plugin_functions.keys():
            self.plugin_functions[function_name](self,  *params)