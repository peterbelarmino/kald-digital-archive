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

marker = "CD118V Video Archive"
marker_position = html.find(marker)

if marker_position == -1:
    print("ERROR: CD118V card not found.")
    sys.exit(1)

card_start = html.rfind('<div class="card video-card', 0, marker_position)
next_card = html.find('<div class="card video-card', marker_position + len(marker))
next_heading = html.find("<h2>Duplicate Videos</h2>", marker_position)

possible_ends = [x for x in [next_card, next_heading] if x != -1]

if card_start == -1 or not possible_ends:
    print("ERROR: Unable to locate the complete CD118V card.")
    sys.exit(1)

card_end = min(possible_ends)
card = html[card_start:card_end]

# Remove direct Google Drive buttons and previous player controls
card = re.sub(
    r'<div[^>]*class=["\'][^"\']*(?:video-actions|cd118-direct-actions)[^"\']*["\'][^>]*>.*?</div>',
    '',
    card,
    flags=re.I | re.S
)

card = re.sub(
    r'<p[^>]*class=["\'][^"\']*video-stream-note[^"\']*["\'][^>]*>.*?</p>',
    '',
    card,
    flags=re.I | re.S
)

card = re.sub(
    r'<p>\s*<b>Video Link:</b>.*?</p>',
    '',
    card,
    flags=re.I | re.S
)

# Remove broken thumbnail click functions
card = re.sub(
    r'\s+onclick=["\'][^"\']*["\']',
    '',
    card,
    flags=re.I
)

card = re.sub(
    r'\s+onkeydown=["\'][^"\']*["\']',
    '',
    card,
    flags=re.I
)

player = f'''
<div class="kald-inline-video">
  <div class="kald-video-ratio">
    <iframe
      src="{preview_url}"
      title="CD118V Video Archive"
      allow="autoplay; fullscreen"
      allowfullscreen
      loading="lazy">
    </iframe>
  </div>

  <p class="kald-video-caption">
    Play the CD118V archive video securely inside the KALD portal.
  </p>
</div>
'''

# Insert player before the final closing div of the card
last_div = card.rfind("</div>")

if last_div == -1:
    print("ERROR: CD118V card closing tag not found.")
    sys.exit(1)

card = card[:last_div] + player + "\n" + card[last_div:]
html = html[:card_start] + card + html[card_end:]

# Add responsive video styling
if "KALD_INLINE_VIDEO_STYLE" not in html:
    css = '''
<style>
/* KALD_INLINE_VIDEO_STYLE */
.kald-inline-video {
  margin-top: 16px;
  padding: 12px;
  background: #101820;
  border-radius: 12px;
}

.kald-video-ratio {
  position: relative;
  width: 100%;
  padding-top: 56.25%;
  overflow: hidden;
  border-radius: 9px;
  background: #000;
}

.kald-video-ratio iframe {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  border: 0;
}

.kald-video-caption {
  margin: 10px 2px 2px;
  color: #e7edf3;
  font-size: 13px;
  text-align: center;
}
</style>
'''

    html = html.replace("</head>", css + "\n</head>", 1)

path.write_text(html, encoding="utf-8")

print("SUCCESS: CD118V now plays inside the KALD webpage.")
print("Direct Google Drive buttons removed.")
