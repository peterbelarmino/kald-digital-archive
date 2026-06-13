from pathlib import Path
import re

# Add Audit link to all nav menus
for p in Path(".").glob("*.html"):
    text = p.read_text(encoding="utf-8", errors="ignore")
    if 'href="iso-audit.html"' not in text:
        text = text.replace(
            '<a href="archive-status.html">Status</a>',
            '<a href="archive-status.html">Status</a><a href="iso-audit.html">Audit</a>'
        )
    p.write_text(text, encoding="utf-8")
    print("Nav checked:", p.name)

# Fix reports page actions
p = Path("reports.html")
text = p.read_text(encoding="utf-8", errors="ignore")

# remove old report links section style only by replacing target text
text = text.replace('target="_blank">Open Archive Summary</a>', 'target="_blank" rel="noopener">View</a> <a href="assets/reports/ARCHIVE_SUMMARY.txt" download>Download</a>')
text = text.replace('target="_blank">Open Master Inventory</a>', 'target="_blank" rel="noopener">View</a> <a href="assets/reports/MASTER_INVENTORY.csv" download>Download</a>')
text = text.replace('target="_blank">Open Recovery Report</a>', 'target="_blank" rel="noopener">View</a> <a href="assets/reports/RECOVERY_REPORT.txt" download>Download</a>')

# add safety notice if not present
if "Report files open in a new tab" not in text:
    text = text.replace(
        '<section',
        '<p style="max-width:1100px;margin:18px auto;background:#fff3cd;color:#5c4700;padding:12px;border-radius:10px;font-weight:700">Report files open in a new tab. Download is optional and only happens when you press Download.</p>\n<section',
        1
    )

# force button style
style = '''
<style id="reports-action-style">
.reports-actions a, .report-card a, .card a{
  display:inline-block;
  background:#0b4f8a!important;
  color:#fff!important;
  padding:10px 14px!important;
  border-radius:10px!important;
  text-decoration:none!important;
  font-weight:800!important;
  margin:4px!important;
}
@media(max-width:768px){
  .reports-actions a, .report-card a, .card a{
    display:block!important;
    width:100%!important;
    box-sizing:border-box!important;
    text-align:center!important;
    margin:8px 0!important;
  }
}
</style>
'''
if 'id="reports-action-style"' not in text:
    text = text.replace("</head>", style + "\n</head>")

p.write_text(text, encoding="utf-8")
print("Reports view/download fixed.")
