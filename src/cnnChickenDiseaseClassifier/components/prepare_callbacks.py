

import os
import time
import tensorflow as tf
from cnnChickenDiseaseClassifier.entity.config_entity import PrepareCallbacksConfig


class PrepareCallback:
    def __init__(self, config: PrepareCallbacksConfig): # takes a config object that tells it where to save logs and checkpoints
        self.config = config

    
    @property
    def _create_tb_callbacks(self): # Builds a TensorBoard callback.
        timestamp = time.strftime("%Y-%m-%d-%H-%M-%S") 
        tb_running_log_dir = os.path.join(
            self.config.tensorboard_root_log_dir,
            f"tb_logs_at_{timestamp}", # timestamp ensures each training run gets a unique folder (avoids overwriting old logs).
        ) # to view Tensorboard logs on browser, run this in the terminal and visit the website: tensorboard --logdir artifacts/prepare_callbacks/tensorboard_log_dir/
        return tf.keras.callbacks.TensorBoard(log_dir=tb_running_log_dir)
    

    @property
    def _create_ckpt_callbacks(self):
        return tf.keras.callbacks.ModelCheckpoint(
            filepath=self.config.checkpoint_model_filepath,
            save_best_only=True # Saves model weights only when validation metrics improve
        ) # Ensures you always end training with the best model saved.
 

    def get_tb_ckpt_callbacks(self): # returns both callbacks as a list
        return [
            self._create_tb_callbacks,
            self._create_ckpt_callbacks
        ]