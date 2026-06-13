from pathlib import Path
import re

p = Path("dashboard.html")
text = p.read_text(encoding="utf-8", errors="ignore")

analytics = """
<section class="section">
<h2>Archive Analytics</h2>
<div class="grid">
<div class="card"><h2>3,467</h2><p>Organized Photos</p></div>
<div class="card"><h2>75</h2><p>Recovered Documents</p></div>
<div class="card"><h2>1</h2><p>Converted Web Video</p></div>
<div class="card"><h2>11+</h2><p>Pending Video ISOs</p></div>
<div class="card"><h2>2</h2><p>Confirmed Duplicates</p></div>
<div class="card"><h2>1</h2><p>Damaged / Special Review</p></div>
</div>

<h2>Archive Recovery Progress</h2>
<div style="background:white;border-radius:18px;padding:22px;box-shadow:0 6px 20px #0002">
<p><b>Overall Completion:</b> 88%</p>
<div style="background:#e5eaf0;border-radius:30px;overflow:hidden;height:28px">
<div style="width:88%;background:#0b6fae;color:white;height:28px;text-align:center;font-weight:800;line-height:28px">88%</div>
</div>
<p style="margin-top:12px;color:#526173">Photos and documents are mostly complete. Remaining major work: video conversion and final turnover package.</p>
</div>
</section>
"""

# Remove old duplicate analytics if rerun
text = re.sub(r'<section class="section">\s*<h2>Archive Analytics</h2>.*?</section>', '', text, flags=re.S)

# Insert before footer if footer exists, else before body
if "<footer>" in text:
    text = text.replace("<footer>", analytics + "\n<footer>", 1)
else:
    text = text.replace("</body>", analytics + "\n</body>")

p.write_text(text, encoding="utf-8")
print("Dashboard analytics and progress bar added.")
