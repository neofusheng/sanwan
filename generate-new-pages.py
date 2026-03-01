import os, json

pages = {
    "video-summary": {
        "icon":"🎬","badge":"研究分析","name":"视频总结",
        "tagline":"YouTube/Bilibili视频自动字幕提取+AI总结",
        "install":"已安装 (vsum skill)",
        "prompt":"请学会视频总结技能。\n\n读取skill文件学习用法：~/.openclaw/workspace-creator/skills/vsum/SKILL.md\n\n功能：给YouTube或Bilibili链接，自动获取字幕，AI总结为结构化markdown。\n\n用法：直接发视频链接，说\"帮我总结这个视频\"",
        "features":["YouTube+Bilibili双平台支持","自动字幕提取+AI总结","输出结构化markdown格式"],
        "examples":["帮我总结这个YouTube视频","这个B站视频讲了什么","提取这个视频的关键观点"]
    },
    "trending": {
        "icon":"🔥","badge":"研究分析","name":"今日热榜",
        "tagline":"微博/知乎/抖音/百度等全平台热搜，一键获取",
        "install":"已安装 (daily-trending skill)",
        "prompt":"请学会今日热榜技能。\n\n读取skill文件：~/.openclaw/workspace-canmou/skills/daily-trending/SKILL.md\n\n从tophub.today抓取各平台热搜：微博/知乎/百度/抖音/头条/B站\n\n用法：说\"今天有什么热搜\"",
        "features":["微博/知乎/抖音/百度/B站多平台","实时热搜榜单抓取","全网热点一目了然"],
        "examples":["今天有什么热搜","微博热搜是什么","最近什么话题比较火"]
    },
    "hn-digest": {
        "icon":"📰","badge":"研究分析","name":"Hacker News",
        "tagline":"HN前页热帖抓取，支持按主题过滤",
        "install":"已安装 (hn-digest skill)",
        "prompt":"请学会Hacker News技能。\n\n读取skill文件：~/.openclaw/workspace-canmou/skills/hn-digest/SKILL.md\n\n抓取HN前页热帖，支持按主题过滤(tech/health/AI)。\n\n用法：说 hn、pull HN、hn 10、hn AI",
        "features":["HN前页实时热帖","按主题过滤(tech/health/AI)","标题+链接+分数完整信息"],
        "examples":["HN上有什么新鲜事","hn AI","拉10条HN帖子看看"]
    },
    "stock-analysis": {
        "icon":"📊","badge":"投资工具","name":"股票深度分析",
        "tagline":"Yahoo Finance数据+8维评分+持仓管理+热门扫描",
        "install":"已安装 (stock-analysis skill)",
        "prompt":"请学会股票深度分析技能。\n\n读取skill文件：~/.openclaw/workspace-jiaoyi/skills/stock-analysis/SKILL.md\n\n功能：Yahoo Finance数据、8维评分、持仓管理、Hot Scanner、传闻捕捉、股息分析\n\n支持：美股/港股/加密货币",
        "features":["8维度综合评分体系","持仓管理+智能预警","Hot Scanner热门股+传闻捕捉"],
        "examples":["分析一下AAPL这只股票","我的持仓收益怎么样","最近有什么热门股票"]
    },
    "hk-stock": {
        "icon":"🇭🇰","badge":"投资工具","name":"港股AI投研",
        "tagline":"港股AI概念板块专属——南向资金博弈+产业基本面",
        "install":"已安装 (hk-ai-stock-expert skill)",
        "prompt":"请学会港股AI投研技能。\n\n读取skill文件：~/.openclaw/workspace-jiaoyi/skills/hk-ai-stock-expert/SKILL.md\n\n功能：港股AI概念板块深度分析、南向资金流向、AI产业链基本面、个股挖掘+风控",
        "features":["港股AI概念板块专属分析","南向资金流向+博弈判断","产业链基本面+个股挖掘"],
        "examples":["港股AI板块今天怎么样","南向资金今天流入多少","推荐几只港股AI标的"]
    },
    "project-manager": {
        "icon":"📋","badge":"办公效率","name":"项目管理",
        "tagline":"飞书多维表格驱动——任务创建/跟踪/日报/通知",
        "install":"已安装 (project-manager skill)",
        "prompt":"请学会项目管理技能。\n\n读取skill文件：~/.openclaw/workspace-yunying/skills/project-manager/SKILL.md\n\n功能：飞书多维表格项目管理、任务分配/跟踪、自动日报、到期提醒",
        "features":["飞书多维表格驱动","任务创建/分配/跟踪全流程","自动日报+到期提醒"],
        "examples":["创建一个新项目","这个任务完成了更新一下","生成今天的项目日报"]
    },
    "fusheng-voice": {
        "icon":"🗣️","badge":"创作工具","name":"傅盛语音克隆",
        "tagline":"用傅盛老板的声音说话——AI语音克隆",
        "install":"已安装 (fusheng-voice skill)",
        "prompt":"请学会傅盛语音克隆技能。\n\n读取skill文件：~/.openclaw/skills/fusheng-voice/SKILL.md\n\n触发方式：说\"用傅盛语音说 [内容]\"\n\n注意：仅限内部使用",
        "features":["AI语音克隆技术","飞书原生语音条发送","说什么就用老板声音说"],
        "examples":["用傅盛语音说：大家好","用老板声音说今天辛苦了","傅盛语音念这段话"]
    },
    "n8n-automation": {
        "icon":"⚡","badge":"开发工具","name":"自动化工作流",
        "tagline":"n8n工作流设计——触发器/重试/错误处理",
        "install":"已安装 (n8n-workflow-automation)",
        "prompt":"请学会自动化工作流技能。\n\n读取skill文件：~/.openclaw/workspace/skills/n8n-workflow-automation/SKILL.md\n\n功能：设计n8n工作流JSON，含触发器/重试/错误处理/人工审核",
        "features":["可视化工作流设计","内置错误处理+重试机制","人工审核队列(human-in-the-loop)"],
        "examples":["帮我设计一个定时发报告的流程","建一个n8n工作流","当邮件到达时自动处理"]
    },
    "distil-web": {
        "icon":"🧊","badge":"研究分析","name":"网页净化提取",
        "tagline":"通过distil.net代理获取干净Markdown",
        "install":"已安装 (distil skill)",
        "prompt":"请学会网页净化提取技能。\n\n读取skill文件：~/.openclaw/workspace-creator/skills/distil/SKILL.md\n\n功能：通过distil.net代理净化网页，输出干净Markdown。web_fetch效果不好时的备选方案。",
        "features":["distil.net代理净化网页","自动去广告去干扰","输出干净Markdown"],
        "examples":["用distil抓取这个网页","这个页面太乱了帮我提取正文","净化这个URL的内容"]
    },
    "self-evolution": {
        "icon":"🧬","badge":"系统能力","name":"自我进化引擎",
        "tagline":"分析运行历史——自动发现改进点并进化能力",
        "install":"已安装 (capability-evolver)",
        "prompt":"请学会自我进化引擎技能。\n\n读取skill文件：~/.openclaw/workspace-jinhua/skills/capability-evolver/SKILL.md\n\n功能：分析agent运行历史，自动识别能力短板，在协议约束下安全进化。",
        "features":["运行历史自动分析","能力短板识别+改进","协议约束下安全进化"],
        "examples":["分析最近的运行效率","有什么能力需要提升","自动优化工作流程"]
    },
    "security-audit": {
        "icon":"🛡️","badge":"系统能力","name":"安全审计",
        "tagline":"Skill安全扫描+系统加固+风险评估",
        "install":"已安装 (mayguard + healthcheck)",
        "prompt":"请学会安全审计技能。\n\n读取skill文件：\n- ~/.openclaw/skills/mayguard/SKILL.md（Skill扫描）\n- /usr/lib/node_modules/openclaw/skills/healthcheck/SKILL.md（系统加固）\n\n功能：Skill恶意代码扫描、系统安全加固、SSH/防火墙/更新检查",
        "features":["Skill恶意代码扫描","系统安全加固检查","SSH/防火墙/更新评估"],
        "examples":["扫描一下这个skill是否安全","系统安全检查","评估当前安全风险"]
    },
    "summary-report": {
        "icon":"📊","badge":"办公效率","name":"工作汇报生成",
        "tagline":"从Session历史自动生成工作总结PDF",
        "install":"已安装 (summary-report skill)",
        "prompt":"请学会工作汇报生成技能。\n\n读取skill文件：~/.openclaw/workspace/skills/summary-report/SKILL.md\n\n功能：从Session历史生成工作总结，支持日报/周报，输出PDF。",
        "features":["Session历史自动提取","日报/周报/月报模板","PDF精美输出"],
        "examples":["总结今天的工作","生成本周工作报告","帮我看看团队这周做了什么"]
    },
    "competitor-research": {
        "icon":"🕵️","badge":"研究分析","name":"竞品研究",
        "tagline":"竞品信息收集、对比分析、市场定位研究",
        "install":"已安装 (competitor-research skill)",
        "prompt":"请学会竞品研究技能。\n\n读取skill文件：~/.openclaw/workspace-canmou/skills/competitor-research/SKILL.md\n\n功能：竞品产品信息收集、功能对比矩阵、市场定位分析、用户评价汇总",
        "features":["产品信息自动收集","功能对比矩阵生成","用户评价+市场定位分析"],
        "examples":["帮我调研一下XX的竞品","对比XX和YY的功能差异","分析这个市场的主要玩家"]
    }
}

template = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{name} — 龙虾技能</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Noto+Sans+SC:wght@400;500;700&display=swap" rel="stylesheet">
<style>
:root{{--bg:#f7f5f2;--card:#fff;--border:#e8e4df;--accent:#c0392b;--text:#2d2926;--muted:#7a746e}}
*{{box-sizing:border-box;margin:0;padding:0}}body{{font-family:'Inter','Noto Sans SC',-apple-system,sans-serif;background:var(--bg);color:var(--text);line-height:1.6}}
.topbar{{background:#fff;border-bottom:1px solid var(--border);padding:14px 32px;display:flex;align-items:center;gap:12px;font-size:13px}}.topbar a{{color:var(--muted);text-decoration:none}}.topbar .sep{{color:var(--border)}}
.hero{{background:#fff;border-bottom:1px solid var(--border);padding:52px 32px 40px;text-align:center;position:relative;overflow:hidden}}
.hero::before{{content:"";position:absolute;top:0;left:0;right:0;bottom:0;opacity:0.15;background-image:radial-gradient(var(--accent) 0.5px,transparent 0.5px);background-size:28px 28px;pointer-events:none}}
.hero-badge{{display:inline-block;background:var(--accent);color:#fff;font-size:11px;font-weight:700;padding:4px 12px;border-radius:99px;margin-bottom:16px;position:relative}}
.hero h1{{font-size:clamp(1.8rem,5vw,2.4rem);font-weight:700;margin-bottom:12px;position:relative}}
.hero p{{color:var(--muted);font-size:1rem;max-width:520px;margin:0 auto 24px;position:relative}}
.hero-btns{{display:flex;gap:12px;justify-content:center;flex-wrap:wrap;position:relative}}
.btn{{display:inline-flex;align-items:center;gap:6px;padding:10px 20px;border-radius:8px;font-size:13px;font-weight:600;text-decoration:none;transition:all .18s;cursor:pointer;border:none;font-family:inherit}}
.btn-primary{{background:var(--accent);color:#fff}}.btn-ghost{{background:var(--bg);color:var(--text);border:1px solid var(--border)}}
.container{{max-width:820px;margin:0 auto;padding:40px 24px 80px}}
.section{{background:var(--card);border:1px solid var(--border);border-radius:14px;padding:28px;margin-bottom:20px}}
.section h2{{font-size:17px;font-weight:700;margin-bottom:18px}}
.feat{{background:var(--bg);border:1px solid var(--border);border-radius:10px;padding:14px;font-size:13px;margin-bottom:8px}}
pre{{background:#1e1e1e;color:#d4d4d4;border-radius:10px;padding:14px 18px;overflow-x:auto;font-size:13px;line-height:1.65;font-family:monospace;margin:8px 0}}
.install-banner{{background:#fffdf9;border:1px solid #fde8c8;border-radius:12px;padding:16px 20px;margin-bottom:24px}}
.install-banner code{{background:rgba(192,57,43,0.1);color:var(--accent);padding:2px 6px;border-radius:4px;font-size:12px}}
@media(max-width:600px){{.section{{padding:20px}}.hero{{padding:36px 20px 28px}}}}
</style></head><body>
<div class="topbar"><a href="/">🦞 龙虾养成日记</a><span class="sep">›</span><a href="/skills.html">技能商店</a><span class="sep">›</span><span>{name}</span></div>
<div class="hero"><div class="hero-badge">{badge}</div><h1>{icon} {name}</h1><p>{tagline}</p>
<div class="hero-btns"><button class="btn btn-primary" onclick="copyInstall()">📋 复制安装提示词</button><a class="btn btn-ghost" href="/skills.html">← 全部技能</a></div></div>
<div class="container">
<div class="install-banner"><p style="font-size:13px;color:#5a4a3a"><strong>⚙️ 安装方式：</strong> <code>{install}</code></p></div>
<div class="section"><h2>⚡ 核心能力</h2>{features_html}</div>
<div class="section"><h2>💬 你可以这样说</h2>{examples_html}</div>
<div style="text-align:center;margin-top:32px"><button class="btn btn-primary" onclick="copyInstall()" style="font-size:15px;padding:14px 28px">📋 复制提示词，发给龙虾即可学会</button></div>
</div>
<script>function copyInstall(){{const p={prompt_json};navigator.clipboard.writeText(p).then(()=>{{document.querySelectorAll('.btn-primary').forEach(b=>{{b.textContent='✅ 已复制！';setTimeout(()=>b.textContent='📋 复制安装提示词',3000)}})}})}};</script>
</body></html>'''

for sid, d in pages.items():
    fhtml = "\n".join([f'<div class="feat">✅ {f}</div>' for f in d['features']])
    ehtml = "\n".join([f'<pre><code>{e}</code></pre>' for e in d['examples']])
    pjson = json.dumps(d['prompt'], ensure_ascii=False)
    
    html = template.format(
        name=d['name'], icon=d['icon'], badge=d['badge'],
        tagline=d['tagline'], install=d['install'],
        features_html=fhtml, examples_html=ehtml, prompt_json=pjson
    )
    with open(f'skills/{sid}.html','w') as f:
        f.write(html)
    print(f"✅ {sid}.html")

print(f"\nDone! {len(pages)} pages generated")
