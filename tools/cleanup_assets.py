#!/usr/bin/env python3
"""清理未使用的美术素材并重新组织文件夹结构"""

import os
import shutil
from pathlib import Path

# 未使用的资源列表（从 analyze_assets.py 输出复制）
UNUSED_ASSETS = [
    'assets/boss-激光/boss_laser_atlas.png',
    'assets/boss-激光/boss_laser_atlas_compressed.png',
    'assets/boss-激光/boss_laser_atlas_compressed.webp',
    'assets/boss-激光/boss_laser_atlas_optimized.webp',
    'assets/btn_start_disabled.png',
    'assets/btn_start_enabled.png',
    'assets/figma_image/screenshot_198_304.png',
    'assets/figma_image/screenshot_198_313.png',
    'assets/figma_image/screenshot_202_60.png',
    'assets/figma_image/screenshot_211_477_compressed.png',
    'assets/figma_image/screenshot_211_477_compressed.webp',
    'assets/figma_image/screenshot_211_704_compressed.webp',
    'assets/figma_image/screenshot_226_1243.png',
    'assets/figma_image/screenshot_226_1260.png',
    'assets/figma_image/screenshot_254_1370_compressed.png',
    'assets/figma_image/screenshot_254_1370_compressed.webp',
    'assets/figma_image/screenshot_254_1433_compressed.png',
    'assets/figma_image/screenshot_254_1433_compressed.webp',
    'assets/figma_image/screenshot_259_1523_compressed.png',
    'assets/figma_image/screenshot_259_1523_compressed.webp',
    'assets/figma_image/screenshot_259_1523_optimized.webp',
    'assets/figma_image/screenshot_261_1545_compressed.png',
    'assets/figma_image/screenshot_261_1545_compressed.webp',
    'assets/figma_image/screenshot_331_247.png',
    'assets/figma_image/screenshot_331_247_compressed.png',
    'assets/figma_image/screenshot_331_247_compressed.webp',
    'assets/figma_image/screenshot_331_247_optimized.webp',
    'assets/figma_image/screenshot_470_11_compressed.png',
    'assets/figma_image/screenshot_470_11_compressed.webp',
    'assets/figma_image/screenshot_470_11_optimized.webp',
    'assets/figma_image/screenshot_470_25_compressed.png',
    'assets/figma_image/screenshot_470_25_compressed.webp',
    'assets/figma_image/screenshot_470_25_optimized.webp',
    'assets/figma_image/screenshot_470_6_compressed.png',
    'assets/figma_image/screenshot_470_6_compressed.webp',
    'assets/figma_image/screenshot_470_6_optimized.webp',
    'assets/figma_image/screenshot_472_104.png',
    'assets/figma_image/screenshot_473_205_compressed.webp',
    'assets/figma_image/screenshot_474_216_compressed.png',
    'assets/figma_image/screenshot_474_216_compressed.webp',
    'assets/figma_image/screenshot_508_118_compressed.png',
    'assets/figma_image/screenshot_508_118_compressed.webp',
    'assets/figma_image/screenshot_509_220.png',
    'assets/figma_image/screenshot_512_165_compressed.png',
    'assets/figma_image/screenshot_512_165_compressed.webp',
    'assets/figma_image/screenshot_513_177_compressed.png',
    'assets/figma_image/screenshot_513_177_compressed.webp',
    'assets/figma_image/screenshot_514_221.png',
    'assets/figma_image/screenshot_571_3_compressed.png',
    'assets/figma_image/screenshot_571_3_compressed.webp',
    'assets/figma_image/screenshot_571_3_optimized.webp',
    'assets/figma_image/screenshot_572_374.png',
    'assets/figma_image/screenshot_605_123_compressed.png',
    'assets/figma_image/screenshot_605_123_compressed.webp',
    'assets/figma_image/screenshot_605_374.png',
    'assets/figma_image/screenshot_605_401.png',
    'assets/figma_image/screenshot_605_410.png',
    'assets/figma_image/screenshot_605_428.png',
    'assets/figma_image/screenshot_605_456.png',
    'assets/figma_image/screenshot_605_456_compressed.webp',
    'assets/figma_image/screenshot_618_158_compressed.png',
    'assets/figma_image/screenshot_618_158_compressed.webp',
    'assets/figma_image/screenshot_619_533_compressed.webp',
    'assets/figma_image/screenshot_619_622.png',
    'assets/logo_compressed.webp',
    'assets/player_ship_large.png',
    'assets/player_ship_large_compressed.webp',
    'assets/player_ship_turbo_compressed.webp',
    'assets/skill_bg_compressed.png',
    'assets/skill_bg_compressed.webp',
    'assets/skill_bg_optimized.webp',
    'assets/skill_dot_active.png',
    'assets/skill_panel_bg.png',
    'assets/导弹发射-序列帧/missile_bubble_atlas_resized.png',
    'assets/导弹尾焰动画/精灵图测试/atlas (1).png',
    'assets/导弹尾焰动画/精灵图测试/atlas (1)_compressed.png',
    'assets/导弹尾焰动画/精灵图测试/atlas_optimized.webp',
    'assets/海面浪花特效-夜晚/water_splash_night_atlas.png',
    'assets/海面浪花特效-夜晚/water_splash_night_atlas_resized.png',
    'assets/海面浪花特效/water_splash_atlas.png',
    'assets/海面浪花特效/water_splash_atlas_resized.png',
    'assets/潜艇爆炸素材/explosion_atlas.png',
    'assets/潜艇爆炸素材/explosion_atlas_resized.png',
    'assets/超级武器动态皮肤/super_weapon_atlas.png',
    'assets/超级武器动态皮肤/super_weapon_atlas_compressed.png',
    'assets/超级武器动态皮肤/super_weapon_atlas_compressed.webp',
    'assets/超级武器动态皮肤/super_weapon_atlas_optimized.webp',
]

# 需要保留并移动到 sprites/ 的精灵图
SPRITE_ASSETS = {
    'assets/boss-激光/boss_laser_atlas_resized.webp': 'sprites/boss_laser.webp',
    'assets/导弹尾焰动画/精灵图测试/atlas (1)_compressed.webp': 'sprites/missile_tail.webp',
    'assets/潜艇爆炸素材/explosion_atlas_compressed.webp': 'sprites/explosion.webp',
    'assets/超级武器动态皮肤/super_weapon_atlas_resized.webp': 'sprites/super_weapon.webp',
    'assets/导弹发射-序列帧/missile_bubble_atlas.png': 'sprites/missile_bubble.png',
    'assets/海面浪花特效/water_splash_atlas_compressed.webp': 'sprites/water_splash.webp',
    'assets/海面浪花特效-夜晚/water_splash_night_atlas_compressed.webp': 'sprites/water_splash_night.webp',
}

def delete_unused_assets(base_path):
    """删除未使用的资源"""
    deleted_count = 0
    saved_space = 0
    
    for rel_path in UNUSED_ASSETS:
        full_path = base_path / rel_path
        if full_path.exists():
            size = full_path.stat().st_size
            full_path.unlink()
            saved_space += size
            deleted_count += 1
            print(f"  删除: {rel_path}")
    
    print(f"\n已删除 {deleted_count} 个文件，节省 {saved_space / (1024*1024):.2f} MB")
    return deleted_count, saved_space

def move_sprite_assets(base_path):
    """移动精灵图到 sprites/ 文件夹"""
    sprites_dir = base_path / 'assets' / 'sprites'
    sprites_dir.mkdir(exist_ok=True)
    
    moved_count = 0
    for old_path, new_path in SPRITE_ASSETS.items():
        old_full = base_path / old_path
        new_full = base_path / 'assets' / new_path
        
        if old_full.exists():
            shutil.move(str(old_full), str(new_full))
            print(f"  移动: {old_path} -> {new_path}")
            moved_count += 1
    
    print(f"\n已移动 {moved_count} 个精灵图文件")
    return moved_count

def cleanup_empty_dirs(base_path):
    """清理空文件夹"""
    assets_dir = base_path / 'assets'
    
    # 删除已知的空文件夹
    empty_dirs = [
        'boss-激光',
        '导弹发射-序列帧',
        '导弹尾焰动画',
        '导弹尾焰动画/精灵图测试',
        '海面浪花特效',
        '海面浪花特效-夜晚',
        '潜艇爆炸素材',
        '超级武器动态皮肤',
    ]
    
    for dir_name in empty_dirs:
        dir_path = assets_dir / dir_name
        if dir_path.exists():
            try:
                dir_path.rmdir()
                print(f"  删除空文件夹: {dir_name}")
            except OSError:
                # 文件夹不为空，跳过
                pass

def main():
    base_path = Path('/Users/bytedance/Desktop/vibe coding/submarine-war')
    
    print("=" * 80)
    print("步骤 1: 删除未使用的资源")
    print("=" * 80)
    delete_unused_assets(base_path)
    
    print("\n" + "=" * 80)
    print("步骤 2: 移动精灵图到 sprites/ 文件夹")
    print("=" * 80)
    move_sprite_assets(base_path)
    
    print("\n" + "=" * 80)
    print("步骤 3: 清理空文件夹")
    print("=" * 80)
    cleanup_empty_dirs(base_path)
    
    print("\n" + "=" * 80)
    print("清理完成！")
    print("=" * 80)

if __name__ == '__main__':
    main()
