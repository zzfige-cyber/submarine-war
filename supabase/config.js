// Supabase 配置
// 请替换为你自己的 Supabase 项目 URL 和匿名密钥
const SUPABASE_CONFIG = {
    url: 'YOUR_SUPABASE_URL', // 例如: https://abcdefgh12345678.supabase.co
    anonKey: 'YOUR_SUPABASE_ANON_KEY' // 例如: eyJhbGciOiJIUzI1NiIs...
};

// 导出配置（用于 ES 模块）
if (typeof module !== 'undefined' && module.exports) {
    module.exports = SUPABASE_CONFIG;
}
