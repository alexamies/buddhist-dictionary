"""Module to read configration data. ==========================================

Only a minimal version of YAML is supported
"""

CONFIG_FILE_NAME = 'config.yaml'


class ConfigurationManager:
    """Reads the config.yaml file into a dictionary.

    """

    def LoadConfig(self, filename = CONFIG_FILE_NAME):
        """Loads the configuration file.

        Args:
          filename: the name of the configuration file

        Return:
          A dictionary with the configuration information

        Raises:
            BDictException: For a non-existent or badly formatted config file.
        """
        self.config = {}
        with open(filename, 'r') as f:
            for line in f:
                if len(line.strip()) == 0:
                    continue
                tokens = line.split(':')
                if len(tokens) < 2:
                    raise BDictException('Badly formatted line %s' % line)
                key = tokens[0].strip()
                value = tokens[1].strip()
                self.config[key] = value
        return self.config

