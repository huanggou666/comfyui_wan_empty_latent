import torch

class wanEmptyLatent:
    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "resolution": ([
                    "720x720 (1:1)",
                    "960x960 (1:1)",
                    "544x960 (9:16)",
                    "960x544 (16:9)",
                    "624x832 (3:4)",
                    "832x624 (4:3)",
                    "720x1280 (9:16)",
                    "1280x720 (16:9)",
                    "832x1104 (3:4)",
                    "1104x832 (4:3)"
                ],),
            },
        }

    RETURN_TYPES = ("INT", "INT", "IMAGE")  # 返回宽度、高度、空白图片
    RETURN_NAMES = ("width", "height", "image")
    FUNCTION = "get_resolution"
    CATEGORY = "wanNodes"

    def get_resolution(self, resolution):
        resolution_map = {
            "720x720 (1:1)": (720, 720),
            "960x960 (1:1)": (960, 960),
            "544x960 (9:16)": (544, 960),
            "960x544 (16:9)": (960, 544),
            "624x832 (3:4)": (624, 832),
            "832x624 (4:3)": (832, 624),
            "720x1280 (9:16)": (720, 1280),
            "1280x720 (16:9)": (1280, 720),
            "832x1104 (3:4)": (832, 1104),
            "1104x832 (4:3)": (1104, 832),
        }
        
        width, height = resolution_map.get(resolution, (720, 720))  # 默认 720x720

        # 创建一张空白图片（黑色）
        image_tensor = torch.zeros(1, height, width, 3, dtype=torch.float32, device=self.device)  

        return width, height, image_tensor
