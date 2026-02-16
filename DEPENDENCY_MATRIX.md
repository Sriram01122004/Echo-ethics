# Dependency Compatibility Matrix

This document explains why specific versions are required for EchoEthics-ML.

## Critical Dependencies

### NumPy: 1.26.4 (Must be <2.0)
- **Why**: `openai-whisper` uses `numba` which requires NumPy <2.0
- **Conflict**: NumPy 2.3.4 breaks whisper/numba
- **Solution**: Pin to 1.26.4

### PyTorch Ecosystem: 2.2.2 / 0.17.1 / 2.2.2
- **torch**: 2.2.2
- **torchvision**: 0.17.1 (must match torch)
- **torchaudio**: 2.2.2 (must match torch)
- **Why**: `pyannote.audio` 3.1 requires compatible torch versions
- **Conflict**: torch 2.9.0 is incompatible with torchvision 0.17.1
- **Solution**: Use matching versions 2.2.2/0.17.1

### tokenizers: >=0.21,<0.22
- **Why**: `transformers` 4.40.1 requires tokenizers in this range
- **Conflict**: tokenizers 0.19.1 is too old
- **Solution**: Upgrade to 0.21.x

### pyannote.audio: 3.1
- **Why**: Speaker diarization functionality
- **Requires**: 
  - Compatible PyTorch versions
  - Hugging Face authentication token
  - Model license acceptance

## Installation Order Matters

1. **NumPy first** (many packages depend on it)
2. **PyTorch ecosystem** (torch, torchvision, torchaudio together)
3. **tokenizers** (before transformers)
4. **Everything else**

## Version Conflicts to Avoid

| Package | Bad Version | Good Version | Reason |
|---------|-------------|--------------|--------|
| numpy | 2.3.4 | 1.26.4 | Breaks numba/whisper |
| torch | 2.9.0 | 2.2.2 | Incompatible with torchvision |
| torchvision | Missing | 0.17.1 | Required for pyannote.audio |
| tokenizers | 0.19.1 | 0.21.x | Too old for transformers |

## Testing Compatibility

After installation, verify with:

```python
import numpy
assert numpy.__version__ == "1.26.4", "NumPy must be 1.26.4"

import torch
assert torch.__version__ == "2.2.2", "PyTorch must be 2.2.2"

import transformers
from transformers import pipeline
# Should work without errors
```

