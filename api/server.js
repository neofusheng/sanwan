const express = require('express');
const Database = require('better-sqlite3');
const cors = require('cors');
const path = require('path');

const app = express();
const PORT = 3456;
const HOST = '127.0.0.1';

// 数据库初始化
const db = new Database(path.join(__dirname, 'comments.db'));
db.exec(`
  CREATE TABLE IF NOT EXISTS comments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    page TEXT NOT NULL,
    nickname TEXT NOT NULL DEFAULT '匿名龙虾🦞',
    content TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
  )
`);
db.exec('CREATE INDEX IF NOT EXISTS idx_page ON comments(page)');

// 内存防刷限制（同IP 30秒内只能提交1条）
const rateLimit = new Map();
function checkRateLimit(ip) {
  const now = Date.now();
  const last = rateLimit.get(ip);
  if (last && now - last < 30000) return false;
  rateLimit.set(ip, now);
  return true;
}
// 定期清理过期记录
setInterval(() => {
  const now = Date.now();
  for (const [ip, t] of rateLimit.entries()) {
    if (now - t > 60000) rateLimit.delete(ip);
  }
}, 60000);

app.use(cors());
app.use(express.json());

// 获取留言列表（支持翻页：offset + limit）
app.get('/api/comments', (req, res) => {
  const page = (req.query.page || 'default').slice(0, 50);
  const limit = Math.min(parseInt(req.query.limit) || 10, 50);
  const offset = Math.max(parseInt(req.query.offset) || 0, 0);
  try {
    const total = db.prepare(
      'SELECT COUNT(*) as cnt FROM comments WHERE page=?'
    ).get(page).cnt;
    const rows = db.prepare(
      'SELECT id, nickname, content, created_at FROM comments WHERE page=? ORDER BY id DESC LIMIT ? OFFSET ?'
    ).all(page, limit, offset);
    res.json({ ok: true, data: rows, total, limit, offset });
  } catch (e) {
    console.error('GET /api/comments error:', e);
    res.status(500).json({ ok: false, error: '服务器错误' });
  }
});

// 提交留言
app.post('/api/comments', (req, res) => {
  const ip = (req.headers['x-forwarded-for'] || '').split(',')[0].trim() || req.ip || 'unknown';

  if (!checkRateLimit(ip)) {
    return res.status(429).json({ ok: false, error: '提交太频繁，请30秒后再试' });
  }

  const { page, nickname, content } = req.body || {};

  if (!page || typeof page !== 'string') {
    return res.status(400).json({ ok: false, error: '缺少page参数' });
  }
  if (!content || typeof content !== 'string' || content.trim().length === 0) {
    return res.status(400).json({ ok: false, error: '内容不能为空' });
  }

  const cleanNick = ((nickname || '').trim().slice(0, 20)) || '匿名龙虾🦞';
  const cleanContent = content.trim().slice(0, 500);
  const cleanPage = page.slice(0, 50);

  try {
    const result = db.prepare(
      'INSERT INTO comments (page, nickname, content) VALUES (?, ?, ?)'
    ).run(cleanPage, cleanNick, cleanContent);

    const row = db.prepare(
      'SELECT id, nickname, content, created_at FROM comments WHERE id=?'
    ).get(result.lastInsertRowid);

    res.json({ ok: true, data: row });
  } catch (e) {
    console.error('POST /api/comments error:', e);
    res.status(500).json({ ok: false, error: '服务器错误' });
  }
});

app.listen(PORT, HOST, () => {
  console.log(`sanwan comments API running at http://${HOST}:${PORT}`);
});
