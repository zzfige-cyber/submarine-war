# Supabase 全球排行榜部署指南

## 概述

本指南将帮助你设置 Supabase 后端，使全球玩家可以通过 GitHub Pages 访问游戏并提交成绩到排行榜。

## 步骤 1：创建 Supabase 项目

1. 访问 [Supabase](https://supabase.com/) 并注册/登录账号
2. 点击 "New Project" 创建新项目
3. 填写项目信息：
   - **Name**: `submarine-war-leaderboard` (或你喜欢的名字)
   - **Database Password**: 设置一个强密码
   - **Region**: 选择离你用户最近的地区 (如 `East Asia`)
4. 点击 "Create new project" 等待项目创建完成（约 1-2 分钟）

## 步骤 2：创建数据库表

1. 进入项目后，点击左侧菜单的 **Table Editor**
2. 点击 **New table** 创建新表
3. 表名填写：`leaderboard`
4. 启用 **Enable Row Level Security (RLS)**
5. 添加以下列：

| 列名 | 类型 | 默认值 | 是否必填 |
|------|------|--------|----------|
| `id` | int8 | 自动生成 | 是 (主键) |
| `name` | text | - | 是 |
| `time` | int4 | - | 是 |
| `combo` | int4 | 0 | 是 |
| `speed_level` | int4 | 0 | 是 |
| `hp_level` | int4 | 0 | 是 |
| `ammo_level` | int4 | 0 | 是 |
| `created_at` | timestamptz | now() | 是 |

6. 点击 **Save** 保存表

## 步骤 3：配置访问权限 (RLS 策略)

1. 点击左侧菜单的 **Authentication** → **Policies**
2. 找到 `leaderboard` 表，点击 **New Policy**
3. 创建以下策略：

### 策略 1: 允许匿名读取
- **Policy name**: `Allow anonymous read access`
- **Allowed operation**: `SELECT`
- **Target roles**: `anon`
- **Using expression**: `true`

### 策略 2: 允许认证用户读取
- **Policy name**: `Allow authenticated read access`
- **Allowed operation**: `SELECT`
- **Target roles**: `authenticated`
- **Using expression**: `true`

### 策略 3: 允许匿名插入
- **Policy name**: `Allow anonymous insert`
- **Allowed operation**: `INSERT`
- **Target roles**: `anon`
- **With check expression**: `true`

### 策略 4: 允许认证用户插入
- **Policy name**: `Allow authenticated insert`
- **Allowed operation**: `INSERT`
- **Target roles**: `authenticated`
- **With check expression**: `true`

## 步骤 4：获取 API 密钥

1. 点击左侧菜单的 **Project Settings** (齿轮图标)
2. 选择 **API** 选项卡
3. 复制以下信息：
   - **URL**: `https://xxxxxxxxxxxxxx.supabase.co`
   - **anon public**: `eyJhbGciOiJIUzI1NiIs...` (以 `eyJ` 开头的长字符串)

## 步骤 5：配置游戏代码

1. 打开 `game.html` 文件
2. 找到第 1513-1514 行的 Supabase 配置：

```javascript
const SUPABASE_URL = 'YOUR_SUPABASE_URL';
const SUPABASE_ANON_KEY = 'YOUR_SUPABASE_ANON_KEY';
```

3. 替换为你在步骤 4 中获取的实际值：

```javascript
const SUPABASE_URL = 'https://你的项目ID.supabase.co';
const SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIs...你的anon密钥...';
```

## 步骤 6：部署到 GitHub Pages

1. 将修改后的代码提交到 GitHub 仓库
2. 进入仓库的 **Settings** → **Pages**
3. **Source** 选择 `Deploy from a branch`
4. **Branch** 选择 `main` (或 `master`)，文件夹选择 `/ (root)`
5. 点击 **Save**
6. 等待几分钟，访问 `https://你的用户名.github.io/仓库名/` 查看部署结果

## 验证是否工作

1. 打开部署后的游戏链接
2. 通关游戏后，尝试上传成绩到排行榜
3. 检查 Supabase 数据库中是否有新记录：
   - 进入 Supabase 项目 → **Table Editor** → `leaderboard` 表
   - 查看是否有新插入的数据

## 故障排除

### 问题：无法上传成绩
- 检查浏览器控制台是否有错误信息
- 确认 SUPABASE_URL 和 SUPABASE_ANON_KEY 是否正确配置
- 检查 RLS 策略是否正确设置

### 问题：排行榜不显示数据
- 检查网络请求是否成功 (浏览器开发者工具 → Network)
- 确认数据库中有数据
- 检查 RLS SELECT 策略是否允许匿名访问

### 问题：跨域错误 (CORS)
- Supabase 默认允许所有来源，无需额外配置
- 如果仍有问题，检查浏览器插件是否拦截了请求

## 安全提示

1. **anon key** 是公开的，可以安全地放在前端代码中
2. 不要暴露 **service_role key**，它具有完全数据库访问权限
3. 定期清理旧数据，避免数据库过大
4. 考虑添加 rate limiting 防止恶意刷榜

## 免费额度

Supabase 免费套餐包含：
- 500MB 数据库空间
- 每月 2GB 带宽
- 每日 50,000 次数据库请求

对于小游戏排行榜来说完全足够！
