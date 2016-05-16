import logging

import database.game_config as config


# Init Log
logging.basicConfig(level=logging.__dict__[config.Log.Level], 
                    format=config.Log.Format,
                    filename='logbook/main.log',
                    filemode='w')

# Main Thread (Handles View)
handler = logging.FileHandler(config.Log.ViewFilename, mode=config.Log.AccessMode)

view_logger = logging.getLogger('view')
view_logger.addHandler(handler)

# Model Producer (Handles Models and InGame Logic)
handler = logging.FileHandler(config.Log.ModelFilename, mode=config.Log.AccessMode)

model_logger = logging.getLogger('model')
model_logger.addHandler(handler)

# ViewModel Producer (Handles ViewModels and Game Logic)
handler = logging.FileHandler(config.Log.ViewModelFilename, mode=config.Log.AccessMode)

vm_logger = logging.getLogger('viewmodel')
vm_logger.addHandler(handler)
