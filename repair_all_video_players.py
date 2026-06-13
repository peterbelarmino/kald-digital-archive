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
        "drive_id": "1xHpprkMk03LaI1vGkbKDOg0qMYbJ5knh",
        "caption": "Play the CD122V archive video inside the KALD portal."
    },
    {
        "title": "CD113V Video Archive",
        "drive_id": "1Vwbk_XBpQz4oIN35z2yhYdXDuhsQCUwl",
        "caption": "Play the CD113V archive video inside the KALD portal."
    },
    {
        "title": "CD118V Video Archive",
        "drive_id": "1F0KG5F1-GmCGHX9vDXTIUF2cMLgPzyIM",
        "caption": "Play the CD118V archive video inside the KALD portal."
    }
]

def repair_video_card(document, title, drive_id, caption):
    title_pos = document.find(title)

    if title_pos == -1:
        print(f"ERROR: Card not found: {title}")
        return document, False

    card_start = document.rfind(
        '<div class="card video-card',
        0,
        title_pos
    )

    if card_start == -1:
        print(f"ERROR: Card start not found: {title}")
        return document, False

    next_card = document.find(
        '<div class="card video-card',
        title_pos + len(title)
    )

    next_heading = document.find(
        "<h2>",
        title_pos + len(title)
    )

    possible_ends = [
        position for position in (next_card, next_heading)
        if position != -1
    ]

    if not possible_ends:
        print(f"ERROR: Card end not found: {title}")
        return document, False

    card_end = min(possible_ends)
    card = document[card_start:card_end]

    # Remove old pending link
    card = re.sub(
        r'<p>\s*<b>Video Link:</b>.*?</p>',
        '',
        card,
        flags=re.I | re.S
    )

    # Remove old details players
    card = re.sub(
        r'<details\b.*?</details>',
        '',
        card,
        flags=re.I | re.S
    )

    # Remove previous embedded player blocks
    card = re.sub(
        r'<div[^>]*class=["\'][^"\']*kald-inline-video[^"\']*["\'][^>]*>.*?</div>\s*</div>',
        '',
        card,
        flags=re.I | re.S
    )

    # Remove orphaned streaming captions
    card = re.sub(
        r'<p[^>]*class=["\'][^"\']*(?:inline-video-note|kald-video-caption|video-stream-note)[^"\']*["\'][^>]*>.*?</p>',
        '',
        card,
        flags=re.I | re.S
    )

    preview_url = (
        f"https://drive.google.com/file/d/{drive_id}/preview"
    )

    player = f'''
<div class="kald-inline-video">
  <div class="kald-inline-player-heading">
    ▶ {title}
  </div>

  <div class="kald-video-ratio">
    <iframe
      src="{preview_url}"
      title="{title}"
      allow="autoplay; fullscreen"
      allowfullscreen
      loading="lazy">
    </iframe>
  </div>

  <p class="kald-video-caption">
    {caption}
  </p>
</div>
'''

    last_closing_div = card.rfind("</div>")

    if last_closing_div == -1:
        print(f"ERROR: Closing card tag missing: {title}")
        return document, False

    card = (
        card[:last_closing_div]
        + player
        + "\n"
        + card[last_closing_div:]
    )

    document = (
        document[:card_start]
        + card
        + document[card_end:]
    )

    print(f"PLAYER REPAIRED: {title}")
    return document, True


success = True

for video in videos:
    html, repaired = repair_video_card(
        html,
        video["title"],
        video["drive_id"],
        video["caption"]
    )

    if not repaired:
        success = False

# Replace/add reliable styling
if "KALD_REPAIRED_VIDEO_PLAYER_STYLE" not in html:
    css = '''
<style>
/* KALD_REPAIRED_VIDEO_PLAYER_STYLE */
.kald-inline-video {
  margin-top: 16px;
  padding: 12px;
  border-radius: 12px;
  background: #101820;
}

.kald-inline-player-heading {
  padding: 2px 2px 11px;
  color: #ffffff;
  font-size: 15px;
  font-weight: 700;
}

.kald-video-ratio {
  position: relative;
  width: 100%;
  padding-top: 56.25%;
  overflow: hidden;
  border-radius: 9px;
  background: #000000;
}

.kald-video-ratio iframe {
  position: absolute;
  inset: 0;
  display: block;
  width: 100%;
  height: 100%;
  border: 0;
}

.kald-video-caption {
  margin: 10px 2px 2px;
  color: #e3ebf2;
  font-size: 13px;
  text-align: center;
}
</style>
'''

    html = html.replace(
        "</head>",
        css + "\n</head>",
        1
    )

# Ensure the counters are correct
html = re.sub(
    r'(<h2>\s*)\d+(\s*</h2>\s*<p>\s*Converted Videos\s*</p>)',
    r'\g<1>3\g<2>',
    html,
    count=1,
    flags=re.I
)

html = re.sub(
    r'(<h2>\s*)\d+(\s*</h2>\s*<p>\s*Pending Video ISOs\s*</p>)',
    r'\g<1>9\g<2>',
    html,
    count=1,
    flags=re.I
)

# Restore missing CD06V and CD09V pending cards
missing_pending_cards = ""

if "CD06V / VIDEO.iso" not in html:
    missing_pending_cards += '''
<div class="card video-card" data-status="Pending">
  <span class="badge pending">Pending</span>
  <h3>CD06V / VIDEO.iso</h3>
  <p>Size: 4.19 GB</p>
</div>
'''

if "CD09V / LG_COMBI_RECORDER.iso" not in html:
    missing_pending_cards += '''
<div class="card video-card" data-status="Pending">
  <span class="badge pending">Pending</span>
  <h3>CD09V / LG_COMBI_RECORDER.iso</h3>
  <p>Size: 1.56 GB</p>
</div>
'''

if missing_pending_cards:
    heading = "<h2>Pending Video ISO Review</h2>"

    if heading in html:
        html = html.replace(
            heading,
            heading + "\n" + missing_pending_cards,
            1
        )
        print("RESTORED: CD06V and/or CD09V pending cards.")
    else:
        print("WARNING: Pending Video ISO Review heading not found.")

path.write_text(html, encoding="utf-8")

if success:
    print("\nSUCCESS: All three video players repaired.")
else:
    print("\nWARNING: One or more video cards were not repaired.")
    sys.exit(1)
