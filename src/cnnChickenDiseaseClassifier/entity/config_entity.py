from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig: # = Entity. a structured object that holds all the config values for the ingestion step:
    root_dir: Path # where artifacts are stored (like artifacts/data_ingestion)
    source_URL: str # dataset link (my S3 URL)
    local_data_file: Path # path to store the downloaded zip
    unzip_dir: Path # path where the zip is extracted

@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int