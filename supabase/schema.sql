-- 创建排行榜表
CREATE TABLE leaderboard (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    time INTEGER NOT NULL, -- 通关时间（毫秒）
    combo INTEGER NOT NULL DEFAULT 0, -- 连击次数
    speed_level INTEGER NOT NULL DEFAULT 0, -- 速度技能等级
    hp_level INTEGER NOT NULL DEFAULT 0, -- 血量技能等级
    ammo_level INTEGER NOT NULL DEFAULT 0, -- 弹药技能等级
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- 创建索引以优化查询性能
CREATE INDEX idx_leaderboard_time ON leaderboard(time ASC);
CREATE INDEX idx_leaderboard_combo ON leaderboard(combo DESC);

-- 启用 RLS (Row Level Security)
ALTER TABLE leaderboard ENABLE ROW LEVEL SECURITY;

-- 创建策略：允许匿名用户读取排行榜
CREATE POLICY "Allow anonymous read access" ON leaderboard
    FOR SELECT TO anon USING (true);

-- 创建策略：允许认证用户读取排行榜
CREATE POLICY "Allow authenticated read access" ON leaderboard
    FOR SELECT TO authenticated USING (true);

-- 创建策略：允许匿名用户插入数据
CREATE POLICY "Allow anonymous insert" ON leaderboard
    FOR INSERT TO anon WITH CHECK (true);

-- 创建策略：允许认证用户插入数据
CREATE POLICY "Allow authenticated insert" ON leaderboard
    FOR INSERT TO authenticated WITH CHECK (true);

-- 授予权限
GRANT SELECT, INSERT ON leaderboard TO anon;
GRANT SELECT, INSERT ON leaderboard TO authenticated;
GRANT USAGE, SELECT ON SEQUENCE leaderboard_id_seq TO anon;
GRANT USAGE, SELECT ON SEQUENCE leaderboard_id_seq TO authenticated;
