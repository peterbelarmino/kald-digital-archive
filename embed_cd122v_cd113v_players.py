from pathlib import Path
import re
import sys

path = Path("videos.html")

if not path.exists():
    print("ERROR: videos.html not found.")
    sys.exit(1)

html = path.read_text(encoding="utf-8", errors="ignore")

videos = [
    {
        "title": "KALD 2019 Video Archive",
        "id": "cd122v-player",
        "drive_id": "1xHpprkMk03LaI1vGkbKDOg0qMYbJ5knh"
    },
    {
        "title": "CD113V Video Archive",
        "id": "cd113v-player",
        "drive_id": "1Vwbk_XBpQz4oIN35z2yhYdXDuhsQCUwl"
    }
]

def update_card(document, title, player_id, drive_id):
    title_position = document.find(title)

    if title_position == -1:
        print(f"ERROR: Card not found: {title}")
        return document, False

    card_start = document.rfind(
        '<div class="card video-card',
        0,
        title_position
    )

    next_card = document.find(
        '<div class="card video-card',
        title_position + len(title)
    )

    next_heading = document.find("<h2>", title_position + len(title))

    possible_ends = [
        value for value in (next_card, next_heading)
        if value != -1
    ]

    if card_start == -1 or not possible_ends:
        print(f"ERROR: Unable to locate full card: {title}")
        return document, False

    card_end = min(possible_ends)
    card = document[card_start:card_end]

    # Remove previous pending link or old player for safe re-run
    card = re.sub(
        r'<p>\s*<b>Video Link:</b>.*?</p>',
        '',
        card,
        flags=re.I | re.S
    )

    card = re.sub(
        r'<details[^>]*class=["\'][^"\']*inline-video-details[^"\']*["\'][^>]*>.*?</details>',
        '',
        card,
        flags=re.I | re.S
    )

    card = re.sub(
        r'<div[^>]*class=["\'][^"\']*(?:video-actions|kald-inline-video)[^"\']*["\'][^>]*>.*?</div>',
        '',
        card,
        flags=re.I | re.S
    )

    preview_url = f"https://drive.google.com/file/d/{drive_id}/preview"

    player = f'''
<details class="inline-video-details" id="{player_id}">
  <summary>▶ Play Video</summary>

  <div class="inline-video-frame">
    <iframe
      src="{preview_url}"
      title="{title}"
      allow="autoplay; fullscreen"
      allowfullscreen
      loading="lazy">
    </iframe>
  </div>

  <p class="inline-video-note">
    Streaming inside the KALD Digital Archive portal.
  </p>
</details>
'''

    last_div = card.rfind("</div>")

    if last_div == -1:
        print(f"ERROR: Closing tag not found: {title}")
        return document, False

    card = card[:last_div] + player + "\n" + card[last_div:]

    updated_document = (
        document[:card_start] +
        card +
        document[card_end:]
    )

    print(f"UPDATED: {title}")
    return updated_document, True


all_success = True

for video in videos:
    html, success = update_card(
        html,
        video["title"],
        video["id"],
        video["drive_id"]
    )

    if not success:
        all_success = False

# Add reusable responsive styling
if "INLINE_VIDEO_DETAILS_STYLE" not in html:
    css = '''
<style>
/* INLINE_VIDEO_DETAILS_STYLE */
.inline-video-details {
  margin-top: 16px;
  border: 1px solid #cbd8e3;
  border-radius: 11px;
  overflow: hidden;
  background: #f7fafc;
}

.inline-video-details summary {
  padding: 13px 17px;
  background: #0969c7;
  color: #ffffff;
  font-weight: 700;
  cursor: pointer;
  list-style: none;
  user-select: none;
}

.inline-video-details summary::-webkit-details-marker {
  display: none;
}

.inline-video-details[open] summary {
  background: #0758a8;
}

.inline-video-frame {
  position: relative;
  width: 100%;
  padding-top: 56.25%;
  background: #000000;
}

.inline-video-frame iframe {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  border: 0;
}

.inline-video-note {
  margin: 0;
  padding: 9px 12px;
  text-align: center;
  font-size: 13px;
  color: #526577;
}
</style>
'''

    html = html.replace("</head>", css + "\n</head>", 1)

path.write_text(html, encoding="utf-8")

if all_success:
    print("\nSUCCESS: CD122V and CD113V players added.")
else:
    print("\nWARNING: One or more cards were not updated.")
    sys.exit(1)
