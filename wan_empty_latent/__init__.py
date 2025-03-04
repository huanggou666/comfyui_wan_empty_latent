from .wan_empty_latent import wanEmptyLatent  # 这里要用小写的文件名

NODE_CLASS_MAPPINGS = {
    # 其他节点...
    "wanEmptyLatent": wanEmptyLatent,  # 添加 wanEmptyLatent 节点
}

NODE_DISPLAY_NAME_MAPPINGS = {
    # 其他节点...
    "wanEmptyLatent": "Empty Latent (WAN)",  # UI 里显示的名称
}
