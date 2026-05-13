#!/usr/bin/env python3
"""分析游戏中使用的美术素材，找出未使用的文件"""

import os
import json
from pathlib import Path

# 项目中实际使用的资源列表（从 game.html 中提取）
USED_ASSETS = {
    # 字体
    'assets/fonts/HYQiHeiY3-HEW.woff2',
    
    # 静态图片 - 直接从HTML引用的
    'assets/logo.png',
    'assets/btn_minus_disabled.png',
    'assets/btn_minus_enabled.png',
    'assets/btn_plus_disabled.png',
    'assets/btn_plus_enabled.png',
    'assets/skill_dot_empty.png',
    'assets/skill_bg.png',
    'assets/background.png',
    
    # figma_image - HTML中直接引用的
    'assets/figma_image/screenshot_211_704.png',
    'assets/figma_image/screenshot_218_1099.png',
    'assets/figma_image/screenshot_218_1105.png',
    'assets/figma_image/screenshot_218_1100.png',
    'assets/figma_image/screenshot_332_5.png',
    'assets/figma_image/screenshot_220_190.png',
    'assets/figma_image/screenshot_255_1506.png',
    'assets/figma_image/screenshot_220_176.png',
    'assets/figma_image/screenshot_220_182.png',
    'assets/figma_image/screenshot_222_1203.png',
    'assets/figma_image/screenshot_222_1196.png',
    'assets/figma_image/screenshot_222_1157.png',
    'assets/figma_image/screenshot_222_1158.png',
    'assets/figma_image/screenshot_261_1545.png',
    'assets/figma_image/screenshot_259_1523.png',
    'assets/figma_image/screenshot_259_1508.png',
    'assets/figma_image/screenshot_259_1514.png',
    'assets/figma_image/screenshot_508_118.png',
    'assets/figma_image/screenshot_513_177.png',
    'assets/figma_image/screenshot_618_177.png',
    'assets/figma_image/screenshot_619_533.png',
    'assets/figma_image/screenshot_605_446.png',
    'assets/figma_image/screenshot_605_477.png',
    'assets/figma_image/screenshot_618_158.png',
    'assets/figma_image/screenshot_508_131.png',
    'assets/figma_image/screenshot_605_476.png',
    'assets/figma_image/screenshot_605_530.png',
    'assets/figma_image/screenshot_605_123.png',
    'assets/figma_image/screenshot_571_3.png',
    'assets/figma_image/screenshot_605_132.png',
    'assets/figma_image/screenshot_605_140.png',
    'assets/figma_image/screenshot_605_282.png',
    'assets/figma_image/screenshot_619_765.png',
    'assets/figma_image/screenshot_619_741.png',
    'assets/figma_image/screenshot_513_199.png',
    'assets/figma_image/screenshot_618_408.png',
    
    # figma_image - JavaScript中引用的
    'assets/figma_image/screenshot_470_6.png',
    'assets/figma_image/screenshot_470_11.png',
    'assets/figma_image/screenshot_202_32.png',
    'assets/figma_image/screenshot_534_4.png',
    'assets/figma_image/screenshot_534_2.png',
    'assets/figma_image/screenshot_534_6.png',
    'assets/figma_image/screenshot_534_8.png',
    'assets/figma_image/screenshot_509_221.png',
    'assets/figma_image/screenshot_470_25.png',
    'assets/figma_image/screenshot_325_90.png',
    'assets/figma_image/screenshot_473_205.png',
    'assets/figma_image/screenshot_474_216.png',
    'assets/figma_image/screenshot_350_13.png',
    'assets/figma_image/screenshot_254_1433.png',
    'assets/figma_image/screenshot_254_1370.png',
    'assets/figma_image/screenshot_211_477.png',
    'assets/figma_image/screenshot_329_187.png',
    'assets/figma_image/screenshot_257_282.png',
    'assets/figma_image/screenshot_512_165.png',
    'assets/figma_image/screenshot_517_506.png',
    'assets/figma_image/screenshot_517_484.png',
    'assets/figma_image/screenshot_519_513.png',
    'assets/figma_image/screenshot_577_652.png',
    'assets/figma_image/screenshot_572_364.png',
    'assets/figma_image/screenshot_584_34.png',
    
    # 精灵图（实际使用的压缩版本）
    'assets/boss-激光/boss_laser_atlas_resized.webp',
    'assets/导弹尾焰动画/精灵图测试/atlas (1)_compressed.webp',
    'assets/潜艇爆炸素材/explosion_atlas_compressed.webp',
    'assets/超级武器动态皮肤/super_weapon_atlas_resized.webp',
    'assets/导弹发射-序列帧/missile_bubble_atlas.png',
    'assets/海面浪花特效/water_splash_atlas_compressed.webp',
    'assets/海面浪花特效-夜晚/water_splash_night_atlas_compressed.webp',
}

# 精灵图资源（需要移动到 sprites/ 文件夹）
SPRITE_ASSETS = {
    'assets/boss-激光/boss_laser_atlas_resized.webp',
    'assets/导弹尾焰动画/精灵图测试/atlas (1)_compressed.webp',
    'assets/潜艇爆炸素材/explosion_atlas_compressed.webp',
    'assets/超级武器动态皮肤/super_weapon_atlas_resized.webp',
    'assets/导弹发射-序列帧/missile_bubble_atlas.png',
    'assets/海面浪花特效/water_splash_atlas_compressed.webp',
    'assets/海面浪花特效-夜晚/water_splash_night_atlas_compressed.webp',
}

def get_all_asset_files(base_path):
    """获取所有美术素材文件"""
    asset_files = []
    assets_dir = Path(base_path) / 'assets'
    
    for ext in ['*.png', '*.jpg', '*.jpeg', '*.webp', '*.gif']:
        for file in assets_dir.rglob(ext):
            # 转换为相对路径
            rel_path = str(file.relative_to(base_path))
            asset_files.append(rel_path)
    
    return sorted(asset_files)

def analyze_assets():
    base_path = Path('/Users/bytedance/Desktop/vibe coding/submarine-war')
    
    # 获取所有资源文件
    all_files = get_all_asset_files(base_path)
    
    # 分类
    used_files = []
    unused_files = []
    
    for file in all_files:
        # 标准化路径（统一使用正斜杠）
        normalized = file.replace('\\', '/')
        
        if normalized in USED_ASSETS:
            used_files.append(normalized)
        else:
            unused_files.append(normalized)
    
    print("=" * 80)
    print("分析结果")
    print("=" * 80)
    print(f"\n总共发现 {len(all_files)} 个美术资源文件")
    print(f"已使用的资源: {len(used_files)} 个")
    print(f"未使用的资源: {len(unused_files)} 个")
    
    print("\n" + "=" * 80)
    print("未使用的资源列表（可以删除）")
    print("=" * 80)
    for f in unused_files:
        print(f"  - {f}")
    
    print("\n" + "=" * 80)
    print("精灵图资源（需要移动到 sprites/ 文件夹）")
    print("=" * 80)
    for f in sorted(SPRITE_ASSETS):
        print(f"  - {f}")
    
    # 计算节省空间
    total_unused_size = 0
    for f in unused_files:
        try:
            size = (base_path / f).stat().st_size
            total_unused_size += size
        except:
            pass
    
    print(f"\n删除未使用资源可节省空间: {total_unused_size / (1024*1024):.2f} MB")
    
    return unused_files, SPRITE_ASSETS

if __name__ == '__main__':
    unused, sprites = analyze_assets()
