from pathlib import Path
import re

# dashboard.html
p = Path("dashboard.html")
text = p.read_text(encoding="utf-8", errors="ignore")

text = text.replace("Overall Completion:</b> 88%", "Overall Archive Content Recovery:</b> 68%")
text = text.replace("width:88%;background:#0b6fae", "width:68%;background:#0b6fae")
text = text.replace(">88%</div>", ">68%</div>")
text = text.replace(
    "Photos and documents are mostly complete. Remaining major work: video conversion and final turnover package.",
    "Photos and documents are mostly complete. Remaining major work: video ISO extraction/conversion, full CD/DVD review, and final turnover package."
)

if "full CD/DVD/ISO content recovery is still in progress" not in text:
    text = text.replace(
        "<h2>Archive Recovery Progress</h2>",
        '<h2>Archive Recovery Progress</h2><div style="background:#fff3cd;color:#5c4700;padding:14px;border-radius:12px;font-weight:700;margin-bottom:14px">Important: The website portal is mostly built, but full CD/DVD/ISO content recovery is still in progress. Many video ISO files remain pending review and conversion.</div>'
    )

p.write_text(text, encoding="utf-8")
print("dashboard updated")

# archive-status.html
p = Path("archive-status.html")
text = p.read_text(encoding="utf-8", errors="ignore")

if "Approximately 68%" not in text:
    text = text.replace(
        '<section class="section">',
        '<section class="section"><div class="card"><h3>Overall Archive Content Recovery</h3><p class="pending">Approximately 68%</p><p>The portal interface is mostly complete, but full CD/DVD/ISO recovery is still in progress. Videos are the largest remaining task.</p></div>',
        1
    )

text = text.replace("74 office documents recovered", "75 office documents recovered")
text = text.replace(
    "1 video converted for web. Remaining video ISOs pending review and conversion.",
    "2 videos converted for web. Many DVD/ISO video archives remain pending review and GPU conversion."
)

p.write_text(text, encoding="utf-8")
print("archive-status updated")
