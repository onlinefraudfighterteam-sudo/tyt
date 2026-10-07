import json,re,shutil
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; D=ROOT/"content/posts/drafts"; P=ROOT/"content/posts"; P.mkdir(exist_ok=True)
idx=json.loads((ROOT/"data/article_index.json").read_text()) if (ROOT/"data/article_index.json").exists() else []
for f in D.glob("*.md"):
    t=f.read_text()
    if re.search(r"^status:\s*['\"]?approved['\"]?\s*$",t,re.M): shutil.move(f,P/f.name)
for x in idx:
    if x.get("path","").startswith("content/posts/drafts/") and not (ROOT/x["path"]).exists():
        x["status"]="published"; x["path"]=x["path"].replace("content/posts/drafts/","content/posts/")
(ROOT/"data/article_index.json").write_text(json.dumps(idx,indent=2,ensure_ascii=False))
site="https://YOUR-DOMAIN.example"
urls=[site+"/blog/"+x["slug"]+"/" for x in idx if x.get("status")=="published"]
(ROOT/"sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"\n".join(f"<url><loc>{u}</loc></url>" for u in sorted(set(urls)))+"\n</urlset>\n")
print("Published approved posts:",len(urls))
