import os,re,json,hashlib
from pathlib import Path
from datetime import datetime,timezone
from openai import OpenAI
ROOT=Path(__file__).resolve().parents[1]; D=ROOT/"content/posts/drafts"; DATA=ROOT/"data"
D.mkdir(parents=True,exist_ok=True)
limit=max(1,min(int(os.getenv("BLOG_DAILY_LIMIT","50")),50))
client=OpenAI(api_key=os.environ["OPENAI_API_KEY"])
topics=json.loads((DATA/"topics.json").read_text())
idx=json.loads((DATA/"article_index.json").read_text()) if (DATA/"article_index.json").exists() else []
used={x.get("title","").lower() for x in idx}|{x.get("slug","").lower() for x in idx}
def slug(s): return re.sub(r"-+","-",re.sub(r"[^a-z0-9]+","-",s.lower())).strip("-")[:90]
for topic in topics:
    if limit<=0: break
    prompt=f"""Write one original, useful educational article for a cryptocurrency fraud-awareness website about: {topic}.
Return JSON with title, slug, excerpt, meta_description, tags, article_html.
Make it 900-1400 words. Use only article HTML tags h2,h3,p,ul,ol,li,strong,em,blockquote.
Do not fabricate statistics, sources, victims, testimonials, or legal outcomes. Never guarantee recovery.
Do not provide hacking, credential theft, bypassing authentication, or private-key instructions.
Tell readers never to share passwords, seed phrases, private keys, or authentication codes.
Include practical warning signs, safe evidence-preservation steps, and a short victim-help section."""
    try:
        r=client.chat.completions.create(model="gpt-4o-mini",response_format={"type":"json_object"},
          messages=[{"role":"system","content":"Return valid JSON only."},{"role":"user","content":prompt}],temperature=.5)
        a=json.loads(r.choices[0].message.content); title=a["title"].strip(); sl=slug(a.get("slug") or title)
        if title.lower() in used or sl in used or len(re.sub("<[^>]+>"," ",a["article_html"]))<3000: continue
        stamp=hashlib.sha256((title+sl).encode()).hexdigest()[:8]; fn=f"{sl}-{stamp}.md"
        front={"title":title,"slug":sl,"status":"draft","created_at":datetime.now(timezone.utc).isoformat(),
               "excerpt":a["excerpt"],"meta_description":a["meta_description"][:160],"tags":a.get("tags",[])}
        text="---\n"+ "\n".join(f"{k}: {json.dumps(v,ensure_ascii=False)}" for k,v in front.items())+"\n---\n\n"+a["article_html"]
        text+="\n<h2>If you may be a victim</h2><p>Preserve transaction IDs, wallet addresses, screenshots, messages, payment records, and website information. Do not send additional funds to anyone promising guaranteed recovery.</p><p><strong>Disclaimer:</strong> This article is educational. Cryptocurrency recovery is never guaranteed.</p>"
        (D/fn).write_text(text,encoding="utf-8"); idx.append({**front,"path":f"content/posts/drafts/{fn}"}); used|={title.lower(),sl}; limit-=1
    except Exception as e: print("Skipped:",e)
(DATA/"article_index.json").write_text(json.dumps(idx,indent=2,ensure_ascii=False))
print("Generation complete.")
