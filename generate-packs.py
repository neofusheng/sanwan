import json, os

# 6 role-based packs
packs = [
    {
        "id": "assistant",
        "icon": "💼",
        "name": "超级助理",
        "tagline": "你的全能私人助理——邮件、日程、搜索、文档，动动嘴就搞定",
        "desc": "适合：白领、管理者、创业者",
        "color": "#2874a6",
        "skills": ["email", "feishu-cal", "feishu-doc", "web-search", "weather", "intelligence"],
        "highlight": "三万每天帮老板处理邮件、管理日程、监控信息——摔伤躺床上也没漏过一件事。"
    },
    {
        "id": "creator",
        "icon": "✍️",
        "name": "内容创作者",
        "tagline": "公众号、小红书、视频、音乐——全平台内容一条龙",
        "desc": "适合：自媒体人、品牌运营、个人IP",
        "color": "#c0392b",
        "skills": ["wechat", "xiaohongshu", "blog-writer", "image-gen", "video-gen", "music-gen", "humanizer", "social-engine"],
        "highlight": "三万14天日更6篇公众号，AI自选选题阅读量1.8万创历史最佳。一篇文章自动改写成多平台版本。"
    },
    {
        "id": "trader",
        "icon": "📈",
        "name": "股票分析师",
        "tagline": "实时行情、技术分析、买卖信号——7×24帮你盯盘",
        "desc": "适合：股民、投资者、量化爱好者",
        "color": "#27ae60",
        "skills": ["web-search", "deep-research", "coding", "intelligence"],
        "highlight": "三万每天监控A股、港股、美股，多维信号分析，交易时段实时推送买卖提醒。",
        "extra_skills": [
            {"icon": "📊", "name": "量化信号监控", "desc": "RSI/MACD/布林带多指标融合，自动生成买卖信号"},
            {"icon": "🔔", "name": "实时推送", "desc": "交易时段内有信号立即推送到聊天工具，不在交易时段自动静默"},
            {"icon": "📉", "name": "持仓追踪", "desc": "自动跟踪持仓股票涨跌幅，异常波动即时预警"}
        ]
    },
    {
        "id": "overseas",
        "icon": "🌏",
        "name": "出海运营官",
        "tagline": "多语言内容、海外社媒、跨境运营——搞定语言和时差",
        "desc": "适合：出海企业、跨境电商、海外市场",
        "color": "#8e44ad",
        "skills": ["twitter", "linkedin", "seo-writer", "web-search", "deep-research", "intelligence"],
        "highlight": "三万发的Twitter Thread，凌晨自动发布，100万+阅读——比团队精心运营的还火。北京深夜=美国白天，龙虾不睡觉。"
    },
    {
        "id": "ecommerce",
        "icon": "🛒",
        "name": "电商运营",
        "tagline": "商品文案、竞品分析、数据监控——用AI代替重复劳动",
        "desc": "适合：电商卖家、品牌方、运营团队",
        "color": "#e67e22",
        "skills": ["xiaohongshu", "xhs-analytics", "image-gen", "seo-writer", "web-search", "deep-research"],
        "highlight": "AI自动生成商品文案和主图，竞品动态实时监控，小红书种草笔记批量产出。"
    },
    {
        "id": "sanwan",
        "icon": "🦞",
        "name": "三万同款团队",
        "tagline": "8个Agent各司其职——这不是一只龙虾，这是一支团队",
        "desc": "⭐ 傅盛亲自验证的完整配置",
        "color": "#c0392b",
        "skills": ["all-in-one", "email", "feishu-cal", "feishu-doc", "wechat", "twitter", "xiaohongshu", "image-gen", "video-gen", "deep-research", "web-search", "coding", "humanizer", "weather", "clawhub"],
        "highlight": "14天，从1只龙虾裂变成8个Agent团队。总指挥+笔杆子+参谋+运营官+社区官+进化官，7×24自动运转。1157条消息，22万字对话，40+ Skill，100万+全网阅读。",
        "agents": [
            {"icon": "🎯", "name": "总指挥（三万）", "desc": "接收指令→分解任务→派发角色→汇总结果→向老板汇报"},
            {"icon": "✍️", "name": "笔杆子", "desc": "公众号、Thread、短视频脚本——内容创作主力"},
            {"icon": "🔬", "name": "参谋", "desc": "深度研究、竞品分析、素材收集——决策支撑"},
            {"icon": "📋", "name": "运营官", "desc": "邮件、日历、审批、Twitter运营、Discord社区"},
            {"icon": "🧬", "name": "进化官", "desc": "写代码、部署、系统优化——技术能力持续进化"},
            {"icon": "💬", "name": "社区官", "desc": "Discord、Twitter互动、用户反馈收集"}
        ]
    }
]

# Load skills data
with open('data/skills.json') as f:
    all_skills = {s['id']: s for s in json.load(f)}

def gen_pack_page(pack):
    pid = pack['id']
    
    # Skills list HTML
    skills_html = ""
    for sid in pack['skills']:
        if sid in all_skills:
            s = all_skills[sid]
            skills_html += f'''
    <a href="/skills/{sid}.html" style="text-decoration:none;color:inherit">
      <div style="background:var(--bg);border:1px solid var(--border);border-radius:10px;padding:14px 16px;display:flex;gap:12px;align-items:center;transition:all .15s">
        <div style="font-size:24px;flex-shrink:0">{s['emoji']}</div>
        <div style="flex:1">
          <div style="font-weight:700;font-size:14px">{s['name']}</div>
          <div style="font-size:12px;color:var(--muted);margin-top:2px">{s['desc']}</div>
        </div>
        <div style="color:var(--accent);font-size:12px;font-weight:600">查看 →</div>
      </div>
    </a>'''

    # Extra skills (like quant trading specific ones)
    extra_html = ""
    if 'extra_skills' in pack:
        for es in pack['extra_skills']:
            extra_html += f'''
    <div style="background:var(--bg);border:1px solid var(--border);border-radius:10px;padding:14px 16px;display:flex;gap:12px;align-items:center">
      <div style="font-size:24px;flex-shrink:0">{es['icon']}</div>
      <div>
        <div style="font-weight:700;font-size:14px">{es['name']}</div>
        <div style="font-size:12px;color:var(--muted);margin-top:2px">{es['desc']}</div>
      </div>
    </div>'''

    # Agent org chart for sanwan pack
    agents_html = ""
    if 'agents' in pack:
        agents_html = '''
    <div class="section">
      <h2><span class="sec-icon">👥</span> 团队架构</h2>
      <p style="font-size:13px;color:var(--muted);margin-bottom:14px">三万同款 = 6个角色各司其职，自动协作：</p>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">'''
        for a in pack['agents']:
            agents_html += f'''
        <div style="background:var(--bg);border:1px solid var(--border);border-radius:10px;padding:12px 14px">
          <div style="font-size:18px;margin-bottom:4px">{a['icon']}</div>
          <div style="font-weight:700;font-size:13px">{a['name']}</div>
          <div style="font-size:12px;color:var(--muted);margin-top:2px">{a['desc']}</div>
        </div>'''
        agents_html += '''
      </div>
    </div>'''

    # Build the install prompt
    skill_names = [all_skills[sid]['name'] for sid in pack['skills'] if sid in all_skills]
    install_prompt = f"请帮我配置「{pack['name']}」技能包，包含以下技能：\\n" + "\\n".join([f"- {n}" for n in skill_names])
    install_prompt += f"\\n\\n技能包说明页：https://sanwan.ai/skills/pack-{pid}.html\\n\\n请逐个学习每个技能的详情页，然后告诉我你已经准备好了。"

    return f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{pack['name']} 技能包 — 龙虾技能</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Noto+Sans+SC:wght@400;500;700&display=swap" rel="stylesheet">
  <style>
    :root {{ --bg:#f7f5f2; --card:#fff; --border:#e8e4df; --accent:{pack['color']}; --text:#2d2926; --muted:#7a746e; }}
    * {{ box-sizing:border-box; margin:0; padding:0; }}
    body {{ font-family:'Inter','Noto Sans SC',-apple-system,sans-serif; background:var(--bg); color:var(--text); line-height:1.6; }}
    .topbar {{ background:#fff; border-bottom:1px solid var(--border); padding:14px 32px; display:flex; align-items:center; gap:12px; font-size:13px; }}
    .topbar a {{ color:var(--muted); text-decoration:none; }} .topbar a:hover {{ color:var(--accent); }}
    .topbar .sep {{ color:var(--border); }}
    .hero {{ background:#fff; border-bottom:1px solid var(--border); padding:52px 32px 40px; text-align:center; position:relative; overflow:hidden; }}
    .hero::before {{ content:""; position:absolute; top:0; left:0; right:0; bottom:0; opacity:0.12; background-image:radial-gradient(var(--accent) 0.5px,transparent 0.5px); background-size:28px 28px; pointer-events:none; }}
    .hero-badge {{ display:inline-block; background:var(--accent); color:#fff; font-size:11px; font-weight:700; letter-spacing:1px; padding:4px 12px; border-radius:99px; margin-bottom:16px; position:relative; }}
    .hero h1 {{ font-size:clamp(1.8rem,5vw,2.4rem); font-weight:700; margin-bottom:12px; position:relative; }}
    .hero p {{ color:var(--muted); font-size:1rem; max-width:520px; margin:0 auto 6px; position:relative; }}
    .hero .sub {{ font-size:13px; color:var(--muted); margin-bottom:24px; position:relative; }}
    .hero-btns {{ display:flex; gap:12px; justify-content:center; flex-wrap:wrap; position:relative; }}
    .btn {{ display:inline-flex; align-items:center; gap:6px; padding:10px 20px; border-radius:8px; font-size:13px; font-weight:600; text-decoration:none; transition:all .18s; cursor:pointer; border:none; font-family:inherit; }}
    .btn-primary {{ background:var(--accent); color:#fff; }} .btn-primary:hover {{ opacity:0.9; }}
    .btn-ghost {{ background:var(--bg); color:var(--text); border:1px solid var(--border); }} .btn-ghost:hover {{ border-color:var(--accent); color:var(--accent); }}
    .container {{ max-width:820px; margin:0 auto; padding:40px 24px 80px; }}
    .section {{ background:var(--card); border:1px solid var(--border); border-radius:14px; padding:28px; margin-bottom:20px; box-shadow:0 1px 3px rgba(0,0,0,0.05); }}
    .section h2 {{ font-size:17px; font-weight:700; margin-bottom:18px; display:flex; align-items:center; gap:8px; }}
    .sec-icon {{ font-size:18px; }}
    .story {{ background:rgba({",".join([str(int(pack['color'].lstrip('#')[i:i+2],16)) for i in (0,2,4)])},0.06); border:1px solid rgba({",".join([str(int(pack['color'].lstrip('#')[i:i+2],16)) for i in (0,2,4)])},0.2); border-radius:12px; padding:16px 20px; margin-bottom:24px; }}
    .story p {{ font-size:14px; color:var(--text); line-height:1.7; }}
    .skills-list {{ display:grid; gap:10px; }}
    .skills-list a div:hover {{ border-color:var(--accent); transform:translateX(4px); }}
    .skill-count {{ display:inline-block; background:var(--accent); color:#fff; font-size:12px; font-weight:700; padding:2px 10px; border-radius:99px; margin-left:8px; }}
    @media(max-width:600px) {{ .section {{ padding:20px; }} .hero {{ padding:36px 20px 28px; }} .topbar {{ padding:12px 16px; }} }}
  </style>
</head>
<body>
  <div class="topbar">
    <a href="/">🦞 龙虾养成日记</a><span class="sep">›</span>
    <a href="/skills.html">技能商店</a><span class="sep">›</span>
    <span>{pack['name']}包</span>
  </div>

  <div class="hero">
    <div class="hero-badge">技能包</div>
    <h1>{pack['icon']} {pack['name']}</h1>
    <p>{pack['tagline']}</p>
    <div class="sub">{pack['desc']}</div>
    <div class="hero-btns">
      <button class="btn btn-primary" onclick="copyInstall()">📋 一键复制安装提示词</button>
      <a class="btn btn-ghost" href="/skills.html">← 全部技能</a>
    </div>
  </div>

  <div class="container">
    <div class="story">
      <p>💡 <strong>真实故事：</strong>{pack['highlight']}</p>
    </div>

    {agents_html}

    <div class="section">
      <h2><span class="sec-icon">🧩</span> 包含技能 <span class="skill-count">{len(pack['skills'])}个</span></h2>
      <div class="skills-list">{skills_html}{extra_html}
      </div>
    </div>

    <div style="text-align:center;margin-top:32px">
      <button class="btn btn-primary" onclick="copyInstall()" style="font-size:15px;padding:14px 28px">📋 一键安装全部技能</button>
      <p style="font-size:12px;color:var(--muted);margin-top:8px">复制提示词 → 发给你的龙虾 → 自动学会全部技能</p>
    </div>
  </div>

  <script>
    function copyInstall() {{
      const prompt = `{install_prompt}`;
      navigator.clipboard.writeText(prompt).then(() => {{
        document.querySelectorAll('.btn-primary').forEach(btn => {{
          const orig = btn.textContent;
          btn.textContent = '✅ 已复制！发给你的龙虾即可';
          setTimeout(() => btn.textContent = orig, 3000);
        }});
      }});
    }}
  </script>
</body>
</html>'''


# Generate pack pages
os.makedirs('skills', exist_ok=True)
for pack in packs:
    html = gen_pack_page(pack)
    with open(f'skills/pack-{pack["id"]}.html', 'w') as f:
        f.write(html)
    print(f"✅ pack-{pack['id']}.html ({len(pack['skills'])} skills)")

# Save packs data for skills.html
with open('data/packs.json', 'w') as f:
    json.dump([{
        "id": p["id"], "icon": p["icon"], "name": p["name"],
        "tagline": p["tagline"], "desc": p["desc"], "color": p["color"],
        "skillCount": len(p["skills"])
    } for p in packs], f, ensure_ascii=False, indent=2)

print("\n✅ packs.json saved")
print("Done!")
