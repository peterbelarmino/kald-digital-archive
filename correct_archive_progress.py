from pathlib import Path
import re

# DASHBOARD UPDATE
p = Path("dashboard.html")
text = p.read_text(encoding="utf-8", errors="ignore")

text = re.sub(r'Overall Completion:</b>\s*\d+%', 'Overall Archive Content Recovery:</b> 68%', text)
text = re.sub(r'width:\d+%;background:#0b6fae', 'width:68%;background:#0b6fae', text)
text = re.sub(r'>\d+%</div>', '>68%</div>', text, count=1)

text = text.replace(
    'Photos and documents are mostly complete. Remaining major work: video conversion and final turnover package.',
    'Photos and documents are mostly complete. Remaining major work: video ISO extraction/conversion, full CD/DVD review, and final turnover package.'
)

if 'full CD/DVD/ISO content recovery is still in progress' not in text:
    text = text.replace(
        '<h2>Archive Recovery Progress</h2>',
        '<h2>Archive Recovery Progress</h2><div style="background:#fff3cd;color:#5c4700;padding:14px;border-radius:12px;font-weight:700;margin-bottom:14px">Important: The website portal is mostly built, but full CD/DVD/ISO content recovery is still in progress. Many video ISO files remain pending review and conversion.</div>'
    )

p.write_text(text, encoding="utf-8")
print("dashboard.html corrected")

# ARCHIVE STATUS UPDATE
p = Path("archive-status.html")
text = p.read_text(encoding="utf-8", errors="ignore")

text = text.replace(
    '<section class="section">',
    '<section class="section"><div class="card"><h3>Overall Archive Content Recovery</h3><p class="pending">Approximately 68%</p><p>The portal interface is mostly complete, but full CD/DVD/ISO recovery is still in progress. Videos are the largest remaining task.</p></div>',
    1
)

text = text.replace(
    '3,467 organized photos recovered and arranged by year/event.',
    '3,467 photos organized in the portal. Photo recovery is mostly complete based on current identified photo folders.'
)

text = text.replace(
    '74 office documents recovered: Word, Excel, PDF, and PowerPoint.',
    '75 office documents recovered and cataloged: Word, Excel, PDF, and PowerPoint.'
)

text = text.replace(
    '1 video converted for web. Remaining video ISOs pending review and conversion.',
    '1 video converted for web. Many DVD/ISO video archives remain pending review and GPU conversion.'
)

p.write_text(text, encoding="utf-8")
print("archive-status.html corrected")
