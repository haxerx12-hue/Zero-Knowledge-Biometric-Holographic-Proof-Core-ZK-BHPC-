import numpy as np

def compute_voxel_coordinates(readings: list) -> dict:
    norm = float(np.linalg.norm(readings))
    return {"x": round(norm * 0.5, 3), "y": round(norm * 0.866, 3), "z": round(sum(readings) % 100.0, 3)}
