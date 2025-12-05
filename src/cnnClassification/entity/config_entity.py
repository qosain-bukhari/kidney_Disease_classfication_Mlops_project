from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConstants:
    root_dir: Path
    tumor_dir: Path
    normal_dir: Path
    train_dir: Path
    test_dir: Path
    test_size: float
    
