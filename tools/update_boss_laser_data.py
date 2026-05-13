#!/usr/bin/env python3
"""
更新game.html中的Boss激光精灵图数据
"""

import re

BASE_DIR = "/Users/bytedance/Desktop/vibe coding/submarine-war"
GAME_HTML = f"{BASE_DIR}/game.html"

# 新的精灵图数据（50%缩放后的坐标）
NEW_SPRITE_DATA = '''assets.bossLaserSpriteData = {"frames":{"4月28日_1_00000.png":{"frame":{"x":0,"y":0,"w":304,"h":540}},"4月28日_1_00001.png":{"frame":{"x":304,"y":0,"w":304,"h":540}},"4月28日_1_00002.png":{"frame":{"x":608,"y":0,"w":304,"h":540}},"4月28日_1_00003.png":{"frame":{"x":912,"y":0,"w":304,"h":540}},"4月28日_1_00004.png":{"frame":{"x":1216,"y":0,"w":304,"h":540}},"4月28日_1_00005.png":{"frame":{"x":1520,"y":0,"w":304,"h":540}},"4月28日_1_00006.png":{"frame":{"x":0,"y":540,"w":304,"h":540}},"4月28日_1_00007.png":{"frame":{"x":304,"y":540,"w":304,"h":540}},"4月28日_1_00008.png":{"frame":{"x":608,"y":540,"w":304,"h":540}},"4月28日_1_00009.png":{"frame":{"x":912,"y":540,"w":304,"h":540}},"4月28日_1_00010.png":{"frame":{"x":1216,"y":540,"w":304,"h":540}},"4月28日_1_00011.png":{"frame":{"x":1520,"y":540,"w":304,"h":540}},"4月28日_1_00012.png":{"frame":{"x":0,"y":1080,"w":304,"h":540}},"4月28日_1_00013.png":{"frame":{"x":304,"y":1080,"w":304,"h":540}},"4月28日_1_00014.png":{"frame":{"x":608,"y":1080,"w":304,"h":540}},"4月28日_1_00015.png":{"frame":{"x":912,"y":1080,"w":304,"h":540}},"4月28日_1_00016.png":{"frame":{"x":1216,"y":1080,"w":304,"h":540}},"4月28日_1_00017.png":{"frame":{"x":1520,"y":1080,"w":304,"h":540}},"4月28日_1_00018.png":{"frame":{"x":0,"y":1620,"w":304,"h":540}},"4月28日_1_00019.png":{"frame":{"x":304,"y":1620,"w":304,"h":540}},"4月28日_1_00020.png":{"frame":{"x":608,"y":1620,"w":304,"h":540}},"4月28日_1_00021.png":{"frame":{"x":912,"y":1620,"w":304,"h":540}},"4月28日_1_00022.png":{"frame":{"x":1216,"y":1620,"w":304,"h":540}},"4月28日_1_00023.png":{"frame":{"x":1520,"y":1620,"w":304,"h":540}},"4月28日_1_00024.png":{"frame":{"x":0,"y":2160,"w":304,"h":540}},"4月28日_1_00025.png":{"frame":{"x":304,"y":2160,"w":304,"h":540}},"4月28日_1_00026.png":{"frame":{"x":608,"y":2160,"w":304,"h":540}},"4月28日_1_00027.png":{"frame":{"x":912,"y":2160,"w":304,"h":540}},"4月28日_1_00028.png":{"frame":{"x":1216,"y":2160,"w":304,"h":540}},"4月28日_1_00029.png":{"frame":{"x":1520,"y":2160,"w":304,"h":540}},"4月28日_1_00030.png":{"frame":{"x":0,"y":2700,"w":304,"h":540}},"4月28日_1_00031.png":{"frame":{"x":304,"y":2700,"w":304,"h":540}},"4月28日_1_00032.png":{"frame":{"x":608,"y":2700,"w":304,"h":540}},"4月28日_1_00033.png":{"frame":{"x":912,"y":2700,"w":304,"h":540}},"4月28日_1_00034.png":{"frame":{"x":1216,"y":2700,"w":304,"h":540}},"4月28日_1_00035.png":{"frame":{"x":1520,"y":2700,"w":304,"h":540}},"4月28日_1_00036.png":{"frame":{"x":0,"y":3240,"w":304,"h":540}},"4月28日_1_00037.png":{"frame":{"x":304,"y":3240,"w":304,"h":540}},"4月28日_1_00038.png":{"frame":{"x":608,"y":3240,"w":304,"h":540}},"4月28日_1_00039.png":{"frame":{"x":912,"y":3240,"w":304,"h":540}},"4月28日_1_00040.png":{"frame":{"x":1216,"y":3240,"w":304,"h":540}}},"meta":{"image":"boss_laser_atlas_resized.webp","size":{"w":1824,"h":3780}}};'''

def update_game_html():
    with open(GAME_HTML, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 使用正则表达式替换bossLaserSpriteData
    pattern = r'assets\.bossLaserSpriteData = \{[^}]+\}\};'
    
    if re.search(pattern, content):
        content = re.sub(pattern, NEW_SPRITE_DATA, content)
        print("✓ 成功更新 bossLaserSpriteData")
    else:
        print("✗ 未找到 bossLaserSpriteData，尝试其他模式...")
        # 尝试更宽松的匹配
        pattern2 = r'assets\.bossLaserSpriteData = \{[\s\S]*?"size":\{[^}]+\}\}\};'
        if re.search(pattern2, content):
            content = re.sub(pattern2, NEW_SPRITE_DATA, content)
            print("✓ 成功更新 bossLaserSpriteData (使用备用模式)")
        else:
            print("✗ 仍然未找到，请手动检查")
            return False
    
    with open(GAME_HTML, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

if __name__ == '__main__':
    print("=" * 60)
    print("更新Boss激光精灵图数据")
    print("=" * 60)
    
    if update_game_html():
        print("\n✓ 更新完成！")
    else:
        print("\n✗ 更新失败，请手动更新")
