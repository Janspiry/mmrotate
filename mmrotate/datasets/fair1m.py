# Copyright (c) OpenMMLab. All rights reserved.
from .builder import ROTATED_DATASETS
from .dota import DOTADataset


@ROTATED_DATASETS.register_module()
class FAIR1MDataset(DOTADataset):
    """Fair1M plane dataset for detection."""
    CLASSES = ('Airplane', )
    PALETTE = [(165, 42, 42), ]
