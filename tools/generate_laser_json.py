#!/usr/bin/env python3
"""
生成压缩版的 Boss 激光 JSON 数据
"""

import json

# 生成简化版的帧数据（只包含必要的 frame 信息）
frames = {}
for i in range(41):
    frame_name = f"4月28日_1_{i:05d}"
    col = i % 6
    row = i // 6
    frames[frame_name] = {
        "frame": {
            "x": col * 608,
            "y": row * 1080,
            "w": 608,
            "h": 1080
        }
    }

json_data = {
    "frames": frames,
    "meta": {
        "image": "boss_laser_atlas.png",
        "size": {"w": 3648, "h": 7560}
    }
}

# 输出为单行 JSON（适合嵌入代码）
compact_json = json.dumps(json_data, ensure_ascii=False, separators=(',', ':'))
print(f"JSON 长度: {len(compact_json)} 字符")
print("\n嵌入代码用的 JSON 数据:")
print(compact_json[:500] + "..." if len(compact_json) > 500 else compact_json)

# 保存完整版本
with open('/Users/bytedance/Desktop/vibe coding/submarine-war/assets/boss-激光/boss_laser_atlas_compact.json', 'w', encoding='utf-8') as f:
    f.write(compact_json)
print("\n✓ 已保存到 boss_laser_atlas_compact.json")
