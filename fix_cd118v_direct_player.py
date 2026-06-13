from pathlib import Path
import re
import sys

path = Path("videos.html")

if not path.exists():
    print("ERROR: videos.html was not found.")
    sys.exit(1)

html = path.read_text(encoding="utf-8", errors="ignore")

marker = "CD118V Video Archive"
start = html.find(marker)

if start == -1:
    print("ERROR: CD118V card was not found.")
    sys.exit(1)

end = html.find("<h2>Duplicate Videos</h2>", start)

if end == -1:
    end = min(len(html), start + 7000)

section = html[start:end]

drive_url = "https://drive.google.com/file/d/1F0KG5F1-GmCGHX9vDXTIUF2cMLgPzyIM/view?usp=sharing"

direct_player = f'''
<div class="video-actions cd118-direct-actions">
  <a class="cd118-play-button"
     href="{drive_url}"
     target="_blank"
     rel="noopener noreferrer">
    ▶ Play CD118V Video
  </a>

  <a class="cd118-drive-button"
     href="{drive_url}"
     target="_blank"
     rel="noopener noreferrer">
    Open in Google Drive
  </a>
</div>

<p class="video-stream-note">
  Video opens securely in Google Drive.
</p>
'''

# Remove existing modal controls inside CD118V card
section = re.sub(
    r'<div[^>]*class=["\'][^"\']*video-actions[^"\']*["\'][^>]*>.*?</div>'
    r'\s*(?:<p[^>]*class=["\'][^"\']*video-stream-note[^"\']*["\'][^>]*>.*?</p>)?',
    direct_player,
    section,
    count=1,
    flags=re.I | re.S
)

# Replace old pending Video Link line when no action block matched
if "cd118-direct-actions" not in section:
    section, replaced = re.subn(
        r'<p>\s*<b>Video Link:</b>.*?</p>',
        direct_player,
        section,
        count=1,
        flags=re.I | re.S
    )

    # Last fallback: insert before closing card
    if replaced == 0:
        closing = section.rfind("</div>")

        if closing != -1:
            section = section[:closing] + direct_player + "\n" + section[closing:]
        else:
            section += direct_player

# Remove broken JavaScript click actions from the CD118V section
section = re.sub(
    r'\s+onclick=["\'][^"\']*openKaldDriveVideo[^"\']*["\']',
    '',
    section,
    flags=re.I
)

section = re.sub(
    r'\s+onkeydown=["\'][^"\']*["\']',
    '',
    section,
    flags=re.I
)

html = html[:start] + section + html[end:]

# Add button styling
if "CD118_DIRECT_PLAYER_STYLE" not in html:
    css = '''
<style>
/* CD118_DIRECT_PLAYER_STYLE */
.cd118-direct-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: 15px;
}

.cd118-play-button,
.cd118-drive-button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 44px;
  padding: 11px 18px;
  border-radius: 9px;
  font-weight: 700;
  text-decoration: none;
}

.cd118-play-button {
  background: #0969c7;
  color: #ffffff;
}

.cd118-drive-button {
  background: #eef3f7;
  color: #17324d;
  border: 1px solid #c7d4df;
}

@media (max-width: 600px) {
  .cd118-play-button,
  .cd118-drive-button {
    width: 100%;
  }
}
</style>
'''

    html = html.replace("</head>", css + "\n</head>", 1)

path.write_text(html, encoding="utf-8")

print("SUCCESS: Direct CD118V Play button added.")
