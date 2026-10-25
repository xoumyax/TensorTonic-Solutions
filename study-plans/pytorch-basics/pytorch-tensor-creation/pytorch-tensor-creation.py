import torch

def create_tensor(method: str, shape: list, value: float = 0.0) -> torch.Tensor:
    """
    Returns a float32 tensor with the requested shape.
    """
    final_tensor = None
    if method == "zeros":
        final_tensor = torch.zeros(shape, dtype=torch.float32)
    elif method == "ones":
        final_tensor = torch.ones(shape, dtype=torch.float32)
    elif method == "full":
        final_tensor = torch.full(shape, value, dtype=torch.float32)

    return final_tensor