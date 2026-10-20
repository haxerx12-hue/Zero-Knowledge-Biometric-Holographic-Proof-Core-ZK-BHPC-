class MeshNodeManager:
    def __init__(self):
        self.nodes = ["cranial_master", "hand_left", "hand_right", "thoracic_core", "lower_extremity"]

    def get_status(self) -> dict:
        return {node: "ACTIVE_SECURE" for node in self.nodes}
