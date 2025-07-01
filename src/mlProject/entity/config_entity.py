from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path

    # def __post_init__(self):
    #     # Ensure that the paths are absolute
    #     self.root_dir = Path(self.root_dir).resolve()
    #     self.local_data_file = Path(self.local_data_file).resolve()
    #     self.unzip_dir = Path(self.unzip_dir).resolve()

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict