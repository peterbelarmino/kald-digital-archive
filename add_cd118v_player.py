from pathlib import Path
import re
import sys

path = Path("videos.html")

if not path.exists():
    print("ERROR: videos.html not found.")
    sys.exit(1)

html = path.read_text(encoding="utf-8", errors="ignore")

drive_id = "1F0KG5F1-GmCGHX9vDXTIUF2cMLgPzyIM"
preview_url = f"https://drive.google.com/file/d/{drive_id}/preview"
view_url = f"https://drive.google.com/file/d/{drive_id}/view?usp=sharing"

marker = "CD118V Video Archive"
marker_pos = html.find(marker)

if marker_pos == -1:
    print("ERROR: CD118V card was not found in videos.html.")
    sys.exit(1)

card_start = html.rfind('<div class="card video-card', 0, marker_pos)
card_end = html.find("</div>", marker_pos)

if card_start == -1 or card_end == -1:
    print("ERROR: Could not locate the complete CD118V card.")
    sys.exit(1)

card_end += len("</div>")
card = html[card_start:card_end]

player_controls = f'''
<div class="video-actions">
  <button type="button"
          class="play-video-btn"
          onclick="openKaldDriveVideo('{preview_url}', 'CD118V Video Archive')">
    ▶ Play Video
  </button>

  <a class="drive-video-link"
     href="{view_url}"
     target="_blank"
     rel="noopener">
    Open in Google Drive
  </a>
</div>

<p class="video-stream-note">
  Streaming securely from Google Drive.
</p>
'''

pending_patterns = [
    r'<p><b>Video Link:</b>\s*Pending authorized shared-drive setup</p>',
    r'<p><b>Video Link:</b>\s*Pending public/shared-drive setup</p>',
    r'<p><b>Video Link:</b>.*?</p>'
]

updated = False

for pattern in pending_patterns:
    new_card, count = re.subn(
        pattern,
        player_controls,
        card,
        count=1,
        flags=re.I | re.S
    )

    if count:
        card = new_card
        updated = True
        break

if not updated and "openKaldDriveVideo" not in card:
    card = card.replace("</div>", player_controls + "\n</div>", 1)

# Make CD118V thumbnail clickable
card = re.sub(
    r'(<img[^>]+src=["'][^"']*cd118v\.jpg[^"']*["'][^>]*)(>)',
    r'''\1
       role="button"
       tabindex="0"
       title="Play CD118V video"
       onclick="openKaldDriveVideo('https://drive.google.com/file/d/1F0KG5F1-GmCGHX9vDXTIUF2cMLgPzyIM/preview', 'CD118V Video Archive')"
       onkeydown="if(event.key==='Enter'){this.click();}"\2''',
    card,
    count=1,
    flags=re.I
)

html = html[:card_start] + card + html[card_end:]

# Add player styling
if ".kald-video-modal" not in html:
    css = '''
<style>
.video-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: 14px;
}

.play-video-btn,
.drive-video-link {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 44px;
  padding: 10px 18px;
  border: 0;
  border-radius: 9px;
  font-size: 15px;
  font-weight: 700;
  text-decoration: none;
  cursor: pointer;
}

.play-video-btn {
  background: #0b67c2;
  color: white;
}

.drive-video-link {
  background: #edf3f8;
  color: #17324d;
  border: 1px solid #cbd8e3;
}

.video-stream-note {
  margin-top: 8px;
  font-size: 13px;
  color: #687786;
}

.video-card img[src*="cd118v.jpg"] {
  cursor: pointer;
}

.kald-video-modal {
  display: none;
  position: fixed;
  inset: 0;
  z-index: 99999;
  padding: 20px;
  background: rgba(0, 0, 0, 0.86);
  align-items: center;
  justify-content: center;
}

.kald-video-modal.active {
  display: flex;
}

.kald-video-dialog {
  position: relative;
  width: min(1000px, 96vw);
  background: #111820;
  border-radius: 14px;
  padding: 18px;
  box-shadow: 0 22px 70px rgba(0, 0, 0, 0.55);
}

.kald-video-dialog h3 {
  margin: 0 45px 14px 0;
  color: white;
}

.kald-video-close {
  position: absolute;
  top: 8px;
  right: 12px;
  border: 0;
  background: transparent;
  color: white;
  font-size: 34px;
  cursor: pointer;
}

.kald-video-frame {
  position: relative;
  width: 100%;
  padding-top: 56.25%;
  overflow: hidden;
  border-radius: 10px;
  background: black;
}

.kald-video-frame iframe {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  border: 0;
}

@media (max-width: 600px) {
  .kald-video-modal {
    padding: 8px;
  }

  .kald-video-dialog {
    width: 100%;
    padding: 12px;
  }

  .play-video-btn,
  .drive-video-link {
    width: 100%;
  }
}
</style>
'''

    html = html.replace("</head>", css + "\n</head>", 1)

# Add modal
if 'id="kaldDriveVideoModal"' not in html:
    modal = '''
<div id="kaldDriveVideoModal"
     class="kald-video-modal"
     aria-hidden="true"
     onclick="if(event.target === this){closeKaldDriveVideo();}">

  <div class="kald-video-dialog"
       role="dialog"
       aria-modal="true"
       aria-labelledby="kaldDriveVideoTitle">

    <button type="button"
            class="kald-video-close"
            aria-label="Close video"
            onclick="closeKaldDriveVideo()">
      &times;
    </button>

    <h3 id="kaldDriveVideoTitle">Video Archive</h3>

    <div class="kald-video-frame">
      <iframe id="kaldDriveVideoFrame"
              src=""
              allow="autoplay; fullscreen"
              allowfullscreen>
      </iframe>
    </div>
  </div>
</div>
'''

    html = html.replace("</body>", modal + "\n</body>", 1)

# Add modal JavaScript
if "function openKaldDriveVideo" not in html:
    javascript = '''
<script>
function openKaldDriveVideo(url, title) {
  const modal = document.getElementById("kaldDriveVideoModal");
  const frame = document.getElementById("kaldDriveVideoFrame");
  const heading = document.getElementById("kaldDriveVideoTitle");

  frame.src = url;
  heading.textContent = title || "Video Archive";
  modal.classList.add("active");
  modal.setAttribute("aria-hidden", "false");
  document.body.style.overflow = "hidden";
}

function closeKaldDriveVideo() {
  const modal = document.getElementById("kaldDriveVideoModal");
  const frame = document.getElementById("kaldDriveVideoFrame");

  frame.src = "";
  modal.classList.remove("active");
  modal.setAttribute("aria-hidden", "true");
  document.body.style.overflow = "";
}

document.addEventListener("keydown", function(event) {
  if (event.key === "Escape") {
    closeKaldDriveVideo();
  }
});
</script>
'''

    html = html.replace("</body>", javascript + "\n</body>", 1)

path.write_text(html, encoding="utf-8")

print("SUCCESS: CD118V Google Drive player added.")
print("Preview URL:", preview_url)
