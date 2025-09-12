import tensorflow as tf
from pathlib import Path
from cnnChickenDiseaseClassifier.entity.config_entity import PrepareBaseModelConfig


class PrepareBaseModel:
    def __init__(self, config: PrepareBaseModelConfig):
        self.config = config  # paths + params (image size, include_top, weights, classes, etc.)

    def get_base_model(self):
        """Load the pretrained backbone and save it (no optimizer)."""
        self.model = tf.keras.applications.vgg16.VGG16(
            input_shape=self.config.params_image_size,
            weights=self.config.params_weights,
            include_top=self.config.params_include_top,
        )
        # Save WITHOUT optimizer state (prevents later optimizer/variable mismatch in Keras 3)
        self.save_model(path=self.config.base_model_path, model=self.model, include_optimizer=False)

    @staticmethod
    def _prepare_full_model(model, classes, freeze_all=True, freeze_till=None):
        """
        Attach a classification head and set trainable flags.
        NOTE: No compile here — training stage will compile freshly.
        """
        # Correct freezing: set per-layer.trainable, not model.trainable
        if freeze_all:
            for layer in model.layers:
                layer.trainable = False
        elif (freeze_till is not None) and (freeze_till > 0):
            for layer in model.layers[:-freeze_till]:
                layer.trainable = False

        # Head: Flatten -> Dense(classes, softmax)
        x = tf.keras.layers.Flatten(name="flatten")(model.output)
        outputs = tf.keras.layers.Dense(classes, activation="softmax", name="predictions")(x)

        full_model = tf.keras.models.Model(inputs=model.input, outputs=outputs, name="vgg16_transfer")

        # we Do NOT compile here; we will compile in the training stage with a fresh optimizer
        # full_model.compile(...)

        full_model.summary()
        return full_model

    def update_base_model(self):
        """Build the full (uncompiled) model with head and save it (no optimizer)."""
        self.full_model = self._prepare_full_model(
            model=self.model,
            classes=self.config.params_classes,
            freeze_all=True,
            freeze_till=None,
        )
        # Save WITHOUT optimizer state (important for Keras 3)
        self.save_model(path=self.config.updated_base_model_path, model=self.full_model, include_optimizer=False)

    @staticmethod
    def save_model(path: Path, model: tf.keras.Model, include_optimizer: bool = False):
        model.save(path, include_optimizer=include_optimizer)  # Keras 3 native saver
