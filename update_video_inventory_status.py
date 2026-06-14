from pathlib import Path

# DASHBOARD
p = Path("dashboard.html")
text = p.read_text(encoding="utf-8", errors="ignore")

text = text.replace("1</h2><p>Converted Web Video", "3</h2><p>Web Ready Videos")
text = text.replace("11+</h2><p>Pending Video ISOs", "11</h2><p>Archived Master Videos")
text = text.replace("video ISO extraction/conversion, full CD/DVD review", "remaining ISO verification, video catalog completion, full CD/DVD review")

if "48.27 GB Video Masters" not in text:
    text = text.replace(
        "<div class=\"card\"><h2>11</h2><p>Archived Master Videos</p></div>",
        "<div class=\"card\"><h2>11</h2><p>Archived Master Videos</p></div><div class=\"card\"><h2>48.27 GB</h2><p>Video Masters Storage</p></div>"
    )

p.write_text(text, encoding="utf-8")
print("dashboard video numbers updated")

# ARCHIVE STATUS
p = Path("archive-status.html")
text = p.read_text(encoding="utf-8", errors="ignore")

text = text.replace(
    "1 video converted for web. Many DVD/ISO video archives remain pending review and GPU conversion.",
    "11 archived master videos and 3 web-ready videos have been created. Remaining work: ISO verification, thumbnails, and final video catalog completion."
)

text = text.replace(
    "Videos are the largest remaining task.",
    "Videos are now partially processed, with 11 master videos and 3 web-ready videos completed. Remaining task: final verification and catalog completion."
)

p.write_text(text, encoding="utf-8")
print("archive-status video numbers updated")

# VIDEOS PAGE small correction
p = Path("videos.html")
text = p.read_text(encoding="utf-8", errors="ignore")

if "Archived Master Videos" not in text:
    insert = """
<h2>Archived Master Videos</h2>
<div class="grid">
<div class="card video-card" data-status="Converted"><span class="badge done">Archived Master</span><h3>KALD 2008 Event</h3><p>File: KALD_2008_Event_1080p.mp4</p><p>Size: 8.06 GB</p></div>
<div class="card video-card" data-status="Converted"><span class="badge done">Archived Master</span><h3>KALD 2014 Event</h3><p>File: KALD_2014_Event_1080p.mp4</p><p>Size: 3.35 GB</p></div>
<div class="card video-card" data-status="Converted"><span class="badge done">Archived Master</span><h3>CD113V</h3><p>File: KALD_CD113V_1080p.mp4</p><p>Size: 0.03 GB</p></div>
<div class="card video-card" data-status="Converted"><span class="badge done">Archived Master</span><h3>CD118V</h3><p>File: KALD_CD118V_1080p.mp4</p><p>Size: 9.24 GB</p></div>
<div class="card video-card" data-status="Converted"><span class="badge done">Archived Master</span><h3>CD119V</h3><p>File: KALD_CD119V_1080p.mp4</p><p>Size: 1.47 GB</p></div>
<div class="card video-card" data-status="Converted"><span class="badge done">Archived Master</span><h3>CD122V 2019</h3><p>File: KALD_CD122V_2019_1080p.mp4</p><p>Size: 4.02 GB</p></div>
<div class="card video-card" data-status="Converted"><span class="badge done">Archived Master</span><h3>CD123V</h3><p>File: KALD_CD123V_1080p.mp4</p><p>Size: 3.98 GB</p></div>
<div class="card video-card" data-status="Converted"><span class="badge done">Archived Master</span><h3>CD124V</h3><p>File: KALD_CD124V_1080p.mp4</p><p>Size: 4.21 GB</p></div>
<div class="card video-card" data-status="Converted"><span class="badge done">Archived Master</span><h3>CD125V</h3><p>File: KALD_CD125V_1080p.mp4</p><p>Size: 4.73 GB</p></div>
<div class="card video-card" data-status="Converted"><span class="badge done">Archived Master</span><h3>CD136V</h3><p>File: KALD_CD136V_1080p_v2.mp4</p><p>Size: 1.58 GB</p></div>
<div class="card video-card" data-status="Converted"><span class="badge done">Archived Master</span><h3>CD139 2014</h3><p>File: KALD_CD139_2014_1080p.mp4</p><p>Size: 7.60 GB</p></div>
</div>

<h2>Web Ready Videos</h2>
<div class="grid">
<div class="card video-card" data-status="Converted"><span class="badge done">Web Ready</span><h3>CD113V Web 720p</h3><p>File: CD113V_Web_720p.mp4</p><p>Size: 0.38 GB</p></div>
<div class="card video-card" data-status="Converted"><span class="badge done">Web Ready</span><h3>CD118V Web 720p</h3><p>File: CD118V_Web_720p.mp4</p><p>Size: 3.51 GB</p></div>
<div class="card video-card" data-status="Converted"><span class="badge done">Web Ready</span><h3>CD122V Web 720p</h3><p>File: KALD_2019_Video_Archive_CD122V_720p.mp4</p><p>Size: 0.53 GB</p></div>
</div>
"""
    text = text.replace("<h2>Converted Videos</h2>", insert + "\n<h2>Converted Videos</h2>")

p.write_text(text, encoding="utf-8")
print("videos page inventory added")
