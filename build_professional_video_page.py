from pathlib import Path
from datetime import datetime
import re
import shutil
import sys

page = Path("videos.html")

if not page.exists():
    print("ERROR: videos.html not found.")
    sys.exit(1)

# Backup before changing the page
backup_dir = Path("backups")
backup_dir.mkdir(exist_ok=True)

stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
backup = backup_dir / f"videos_before_pro_layout_{stamp}.html"
shutil.copy2(page, backup)

html = page.read_text(encoding="utf-8", errors="ignore")

new_main = r'''
<main class="kva-page" id="videoArchive">

  <section class="kva-hero">
    <div>
      <span class="kva-eyebrow">KALD DIGITAL ARCHIVE CENTER</span>
      <h1>Video Archive</h1>
      <p>
        Recovered DVD and ISO recordings, enhanced web copies,
        duplicate assessments, and pending preservation work.
      </p>
    </div>

    <div class="kva-hero-badge">
      <strong>3</strong>
      <span>Videos preserved</span>
    </div>
  </section>

  <section class="kva-stats" aria-label="Video archive statistics">
    <article class="kva-stat">
      <span class="kva-stat-icon">▶</span>
      <div>
        <strong>3</strong>
        <span>Converted Videos</span>
      </div>
    </article>

    <article class="kva-stat">
      <span class="kva-stat-icon">◷</span>
      <div>
        <strong>9</strong>
        <span>Pending Video ISOs</span>
      </div>
    </article>

    <article class="kva-stat">
      <span class="kva-stat-icon">⧉</span>
      <div>
        <strong>1</strong>
        <span>Duplicate Video</span>
      </div>
    </article>

    <article class="kva-stat">
      <span class="kva-stat-icon">⚠</span>
      <div>
        <strong>1</strong>
        <span>Damaged Media</span>
      </div>
    </article>
  </section>

  <section class="kva-toolbar" aria-label="Video search and filters">
    <label class="kva-search">
      <span>⌕</span>
      <input
        type="search"
        id="kvaVideoSearch"
        placeholder="Search title, source, year, or status..."
        autocomplete="off">
    </label>

    <label class="kva-filter">
      <span>Status</span>
      <select id="kvaStatusFilter">
        <option value="all">All records</option>
        <option value="converted">Converted</option>
        <option value="pending">Pending ISO</option>
        <option value="duplicate">Duplicate</option>
        <option value="damaged">Damaged</option>
      </select>
    </label>

    <div class="kva-result" id="kvaResultCount">
      Showing 13 archive records
    </div>
  </section>

  <section class="kva-section">
    <header class="kva-section-header">
      <div>
        <span class="kva-section-label">Preserved collection</span>
        <h2>Converted Videos</h2>
      </div>
      <span class="kva-section-count">3 records</span>
    </header>

    <div class="kva-video-grid">

      <article
        class="kva-video-card kva-searchable"
        data-status="converted"
        data-search="cd122v kald 2019 video archive converted google drive 2019">

        <div class="kva-cover">
          <img
            src="assets/video-thumbnails/kald2019_cd122v.jpg?v=20260613"
            alt="KALD 2019 Video Archive thumbnail"
            loading="lazy">

          <span class="kva-status kva-status-converted">Converted</span>
          <span class="kva-duration">01:11:33</span>

          <div class="kva-cover-overlay">
            <span>▶ Play archive video</span>
          </div>
        </div>

        <div class="kva-card-body">
          <div class="kva-card-heading">
            <div>
              <span class="kva-record-code">CD122V</span>
              <h3>KALD 2019 Video Archive</h3>
            </div>
          </div>

          <p class="kva-description">
            Recovered KALD 2019 DVD recording converted to a
            web-compatible preservation copy.
          </p>

          <dl class="kva-metadata">
            <div>
              <dt>Source</dt>
              <dd>KALD2019.iso</dd>
            </div>
            <div>
              <dt>Web copy</dt>
              <dd>542 MB</dd>
            </div>
            <div>
              <dt>Format</dt>
              <dd>MP4 · H.264 · 720p</dd>
            </div>
            <div>
              <dt>Storage</dt>
              <dd>Google Drive Archive</dd>
            </div>
          </dl>

          <div class="kva-tags">
            <span>Recovered</span>
            <span>2019</span>
            <span>DVD Archive</span>
          </div>

          <details
            class="kva-player"
            data-player="https://drive.google.com/file/d/1xHpprkMk03LaI1vGkbKDOg0qMYbJ5knh/preview">

            <summary>
              <span class="kva-play-icon">▶</span>
              <span>Play Video</span>
              <span class="kva-expand-icon">⌄</span>
            </summary>

            <div class="kva-player-shell">
              <iframe
                src="about:blank"
                data-src="https://drive.google.com/file/d/1xHpprkMk03LaI1vGkbKDOg0qMYbJ5knh/preview"
                title="KALD 2019 Video Archive"
                allow="autoplay; fullscreen"
                allowfullscreen>
              </iframe>
            </div>
          </details>
        </div>
      </article>

      <article
        class="kva-video-card kva-searchable"
        data-status="converted"
        data-search="cd113v pp dvd2 ntsc recovered title converted">

        <div class="kva-cover">
          <img
            src="assets/video-thumbnails/cd113v.jpg?v=20260613"
            alt="CD113V recovered DVD title thumbnail"
            loading="lazy">

          <span class="kva-status kva-status-converted">Converted</span>
          <span class="kva-duration">00:14:59</span>

          <div class="kva-cover-overlay">
            <span>▶ Play archive video</span>
          </div>
        </div>

        <div class="kva-card-body">
          <div class="kva-card-heading">
            <div>
              <span class="kva-record-code">CD113V</span>
              <h3>CD113V Recovered DVD Title</h3>
            </div>
          </div>

          <p class="kva-description">
            Selected title recovered from a multi-title authored DVD.
            The original ISO remains preserved for further title recovery.
          </p>

          <dl class="kva-metadata">
            <div>
              <dt>Source</dt>
              <dd>PP_DVD2_NTSC.iso</dd>
            </div>
            <div>
              <dt>Web copy</dt>
              <dd>391.51 MB</dd>
            </div>
            <div>
              <dt>Format</dt>
              <dd>MP4 · H.264 · 720p</dd>
            </div>
            <div>
              <dt>Storage</dt>
              <dd>Google Drive Archive</dd>
            </div>
          </dl>

          <div class="kva-tags">
            <span>Recovered Title</span>
            <span>Multi-title DVD</span>
            <span>Enhanced</span>
          </div>

          <details
            class="kva-player"
            data-player="https://drive.google.com/file/d/1Vwbk_XBpQz4oIN35z2yhYdXDuhsQCUwl/preview">

            <summary>
              <span class="kva-play-icon">▶</span>
              <span>Play Video</span>
              <span class="kva-expand-icon">⌄</span>
            </summary>

            <div class="kva-player-shell">
              <iframe
                src="about:blank"
                data-src="https://drive.google.com/file/d/1Vwbk_XBpQz4oIN35z2yhYdXDuhsQCUwl/preview"
                title="CD113V Recovered DVD Title"
                allow="autoplay; fullscreen"
                allowfullscreen>
              </iframe>
            </div>
          </details>
        </div>
      </article>

      <article
        class="kva-video-card kva-searchable"
        data-status="converted"
        data-search="cd118v video iso converted enhanced verified 1 hour 48 minutes">

        <div class="kva-cover">
          <img
            src="assets/video-thumbnails/cd118v.jpg?v=20260613"
            alt="CD118V Video Archive thumbnail"
            loading="lazy">

          <span class="kva-status kva-status-converted">Converted</span>
          <span class="kva-duration">01:48:04</span>

          <div class="kva-cover-overlay">
            <span>▶ Play archive video</span>
          </div>
        </div>

        <div class="kva-card-body">
          <div class="kva-card-heading">
            <div>
              <span class="kva-record-code">CD118V</span>
              <h3>CD118V Video Archive</h3>
            </div>
          </div>

          <p class="kva-description">
            Complete five-part DVD title joined, restored, enhanced,
            verified, and preserved as a web-compatible master copy.
          </p>

          <dl class="kva-metadata">
            <div>
              <dt>Source</dt>
              <dd>VIDEO.iso</dd>
            </div>
            <div>
              <dt>Web copy</dt>
              <dd>3.51 GB</dd>
            </div>
            <div>
              <dt>Format</dt>
              <dd>MP4 · H.264 · 720p</dd>
            </div>
            <div>
              <dt>Storage</dt>
              <dd>Google Drive Archive</dd>
            </div>
          </dl>

          <div class="kva-tags">
            <span>Complete DVD</span>
            <span>Enhanced</span>
            <span>Verified</span>
          </div>

          <details
            class="kva-player"
            data-player="https://drive.google.com/file/d/1F0KG5F1-GmCGHX9vDXTIUF2cMLgPzyIM/preview">

            <summary>
              <span class="kva-play-icon">▶</span>
              <span>Play Video</span>
              <span class="kva-expand-icon">⌄</span>
            </summary>

            <div class="kva-player-shell">
              <iframe
                src="about:blank"
                data-src="https://drive.google.com/file/d/1F0KG5F1-GmCGHX9vDXTIUF2cMLgPzyIM/preview"
                title="CD118V Video Archive"
                allow="autoplay; fullscreen"
                allowfullscreen>
              </iframe>
            </div>
          </details>
        </div>
      </article>

    </div>
  </section>

  <section class="kva-section">
    <header class="kva-section-header">
      <div>
        <span class="kva-section-label">Quality control</span>
        <h2>Duplicate Assessment</h2>
      </div>
      <span class="kva-section-count">1 record</span>
    </header>

    <article
      class="kva-notice-card kva-searchable"
      data-status="duplicate"
      data-search="cd71v duplicate kald2019 cd122v skipped">

      <div class="kva-notice-icon kva-duplicate-icon">⧉</div>

      <div class="kva-notice-content">
        <div class="kva-notice-title">
          <div>
            <span class="kva-record-code">CD71V</span>
            <h3>KALD2019.iso</h3>
          </div>
          <span class="kva-status kva-status-duplicate">Duplicate</span>
        </div>

        <p>
          Identical VOB structure and matching file sizes were found
          against CD122V. Conversion was skipped to prevent unnecessary
          duplicate storage.
        </p>

        <div class="kva-action-note">
          Action completed: retained as an audited duplicate reference.
        </div>
      </div>
    </article>
  </section>

  <section class="kva-section">
    <header class="kva-section-header">
      <div>
        <span class="kva-section-label">Preservation queue</span>
        <h2>Pending Video ISO Review</h2>
      </div>
      <span class="kva-section-count">9 records</span>
    </header>

    <div class="kva-pending-grid">

      <article class="kva-pending-card kva-searchable" data-status="pending" data-search="cd06v video iso pending 4.19 gb">
        <div>
          <span class="kva-record-code">CD06V</span>
          <h3>VIDEO.iso</h3>
        </div>
        <span class="kva-file-size">4.19 GB</span>
        <span class="kva-status kva-status-pending">Pending review</span>
      </article>

      <article class="kva-pending-card kva-searchable" data-status="pending" data-search="cd09v lg combi recorder iso pending 1.56 gb">
        <div>
          <span class="kva-record-code">CD09V</span>
          <h3>LG_COMBI_RECORDER.iso</h3>
        </div>
        <span class="kva-file-size">1.56 GB</span>
        <span class="kva-status kva-status-pending">Pending review</span>
      </article>

      <article class="kva-pending-card kva-searchable" data-status="pending" data-search="cd119v dvd iso pending 3.75 gb">
        <div>
          <span class="kva-record-code">CD119V</span>
          <h3>DVD.iso</h3>
        </div>
        <span class="kva-file-size">3.75 GB</span>
        <span class="kva-status kva-status-pending">Pending review</span>
      </article>

      <article class="kva-pending-card kva-searchable" data-status="pending" data-search="cd123v video iso pending 4.16 gb">
        <div>
          <span class="kva-record-code">CD123V</span>
          <h3>VIDEO.iso</h3>
        </div>
        <span class="kva-file-size">4.16 GB</span>
        <span class="kva-status kva-status-pending">Pending review</span>
      </article>

      <article class="kva-pending-card kva-searchable" data-status="pending" data-search="cd124v video iso pending 4.01 gb">
        <div>
          <span class="kva-record-code">CD124V</span>
          <h3>VIDEO.iso</h3>
        </div>
        <span class="kva-file-size">4.01 GB</span>
        <span class="kva-status kva-status-pending">Pending review</span>
      </article>

      <article class="kva-pending-card kva-searchable" data-status="pending" data-search="cd125v video iso pending 3.99 gb">
        <div>
          <span class="kva-record-code">CD125V</span>
          <h3>VIDEO.iso</h3>
        </div>
        <span class="kva-file-size">3.99 GB</span>
        <span class="kva-status kva-status-pending">Pending review</span>
      </article>

      <article class="kva-pending-card kva-searchable" data-status="pending" data-search="cd126v video iso pending 3.39 gb">
        <div>
          <span class="kva-record-code">CD126V</span>
          <h3>VIDEO.iso</h3>
        </div>
        <span class="kva-file-size">3.39 GB</span>
        <span class="kva-status kva-status-pending">Pending review</span>
      </article>

      <article class="kva-pending-card kva-searchable" data-status="pending" data-search="cd127v video iso pending 4.16 gb">
        <div>
          <span class="kva-record-code">CD127V</span>
          <h3>VIDEO.iso</h3>
        </div>
        <span class="kva-file-size">4.16 GB</span>
        <span class="kva-status kva-status-pending">Pending review</span>
      </article>

      <article class="kva-pending-card kva-searchable" data-status="pending" data-search="cd136v my disc iso pending 2.75 gb">
        <div>
          <span class="kva-record-code">CD136V</span>
          <h3>My Disc.iso</h3>
        </div>
        <span class="kva-file-size">2.75 GB</span>
        <span class="kva-status kva-status-pending">Pending review</span>
      </article>

    </div>
  </section>

  <section class="kva-section">
    <header class="kva-section-header">
      <div>
        <span class="kva-section-label">Manual recovery</span>
        <h2>Damaged / Special Review</h2>
      </div>
      <span class="kva-section-count">1 record</span>
    </header>

    <article
      class="kva-notice-card kva-searchable kva-damaged-card"
      data-status="damaged"
      data-search="cd69v damaged manual inspection recovery">

      <div class="kva-notice-icon kva-damaged-icon">⚠</div>

      <div class="kva-notice-content">
        <div class="kva-notice-title">
          <div>
            <span class="kva-record-code">CD69V</span>
            <h3>Damaged Video Media</h3>
          </div>
          <span class="kva-status kva-status-damaged">Special review</span>
        </div>

        <p>
          This disc is marked damaged and requires manual inspection,
          recovery testing, and validation before any conversion attempt.
        </p>
      </div>
    </article>
  </section>

  <div class="kva-empty-state" id="kvaEmptyState" hidden>
    <strong>No matching video records</strong>
    <span>Try a different search term or status filter.</span>
  </div>

</main>
'''

pro_style = r'''
<!-- KALD_VIDEO_PRO_STYLE_START -->
<style>
.kva-page {
  --kva-blue: #075da8;
  --kva-blue-dark: #063e72;
  --kva-blue-soft: #eaf4fc;
  --kva-border: #d9e4ed;
  --kva-text: #17324a;
  --kva-muted: #65798a;
  --kva-surface: #ffffff;
  --kva-background: #f4f7fa;

  width: min(1320px, calc(100% - 32px));
  margin: 0 auto;
  padding: 30px 0 64px;
  color: var(--kva-text);
}

.kva-page *,
.kva-page *::before,
.kva-page *::after {
  box-sizing: border-box;
}

.kva-hero {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 30px;
  min-height: 220px;
  padding: 38px 42px;
  border-radius: 24px;
  background:
    radial-gradient(circle at 90% 20%, rgba(255,255,255,.20), transparent 30%),
    linear-gradient(135deg, #063e72, #0874c9);
  color: #ffffff;
  box-shadow: 0 18px 48px rgba(6, 62, 114, .22);
}

.kva-eyebrow,
.kva-section-label {
  display: block;
  margin-bottom: 7px;
  font-size: 12px;
  font-weight: 800;
  letter-spacing: .13em;
  text-transform: uppercase;
}

.kva-hero h1 {
  margin: 0;
  font-size: clamp(34px, 5vw, 54px);
  line-height: 1.05;
}

.kva-hero p {
  max-width: 720px;
  margin: 16px 0 0;
  color: rgba(255,255,255,.86);
  font-size: 16px;
  line-height: 1.7;
}

.kva-hero-badge {
  min-width: 165px;
  padding: 22px;
  border: 1px solid rgba(255,255,255,.22);
  border-radius: 18px;
  background: rgba(255,255,255,.12);
  text-align: center;
  backdrop-filter: blur(8px);
}

.kva-hero-badge strong {
  display: block;
  font-size: 38px;
}

.kva-hero-badge span {
  font-size: 13px;
  color: rgba(255,255,255,.84);
}

.kva-stats {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 16px;
  margin: 22px 0;
}

.kva-stat {
  display: flex;
  align-items: center;
  gap: 14px;
  min-height: 98px;
  padding: 20px;
  border: 1px solid var(--kva-border);
  border-radius: 17px;
  background: var(--kva-surface);
  box-shadow: 0 8px 24px rgba(22, 55, 82, .06);
}

.kva-stat-icon {
  display: grid;
  width: 46px;
  height: 46px;
  flex: 0 0 46px;
  place-items: center;
  border-radius: 13px;
  background: var(--kva-blue-soft);
  color: var(--kva-blue);
  font-size: 21px;
  font-weight: 800;
}

.kva-stat strong {
  display: block;
  font-size: 25px;
  line-height: 1;
}

.kva-stat span:last-child {
  display: block;
  margin-top: 6px;
  color: var(--kva-muted);
  font-size: 13px;
}

.kva-toolbar {
  display: grid;
  grid-template-columns: minmax(260px, 1fr) 210px auto;
  align-items: center;
  gap: 14px;
  margin-bottom: 38px;
  padding: 15px;
  border: 1px solid var(--kva-border);
  border-radius: 17px;
  background: var(--kva-surface);
}

.kva-search {
  display: flex;
  align-items: center;
  gap: 10px;
  min-height: 46px;
  padding: 0 14px;
  border: 1px solid var(--kva-border);
  border-radius: 11px;
  background: #f8fafc;
}

.kva-search input {
  width: 100%;
  border: 0;
  outline: 0;
  background: transparent;
  color: var(--kva-text);
  font: inherit;
}

.kva-filter {
  display: flex;
  flex-direction: column;
  gap: 3px;
}

.kva-filter > span {
  color: var(--kva-muted);
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
}

.kva-filter select {
  min-height: 46px;
  padding: 0 12px;
  border: 1px solid var(--kva-border);
  border-radius: 11px;
  background: #ffffff;
  color: var(--kva-text);
  font: inherit;
}

.kva-result {
  color: var(--kva-muted);
  font-size: 13px;
  white-space: nowrap;
}

.kva-section {
  margin-top: 42px;
}

.kva-section-header {
  display: flex;
  align-items: end;
  justify-content: space-between;
  gap: 20px;
  margin-bottom: 18px;
}

.kva-section-label {
  color: var(--kva-blue);
}

.kva-section-header h2 {
  margin: 0;
  font-size: 26px;
}

.kva-section-count {
  padding: 7px 11px;
  border-radius: 999px;
  background: var(--kva-blue-soft);
  color: var(--kva-blue-dark);
  font-size: 12px;
  font-weight: 700;
}

.kva-video-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 22px;
  align-items: start;
}

.kva-video-card {
  overflow: hidden;
  border: 1px solid var(--kva-border);
  border-radius: 20px;
  background: var(--kva-surface);
  box-shadow: 0 12px 34px rgba(20, 52, 78, .09);
  transition: transform .22s ease, box-shadow .22s ease;
}

.kva-video-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 18px 42px rgba(20, 52, 78, .14);
}

.kva-cover {
  position: relative;
  aspect-ratio: 16 / 9;
  overflow: hidden;
  background: #101820;
}

.kva-cover img {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.kva-cover-overlay {
  position: absolute;
  inset: auto 0 0;
  padding: 38px 16px 14px;
  background: linear-gradient(transparent, rgba(0,0,0,.76));
  color: #ffffff;
  font-size: 13px;
  font-weight: 700;
  opacity: 0;
  transition: opacity .2s ease;
}

.kva-video-card:hover .kva-cover-overlay {
  opacity: 1;
}

.kva-status {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 6px 9px;
  border-radius: 999px;
  font-size: 11px;
  font-weight: 800;
  line-height: 1;
  white-space: nowrap;
}

.kva-cover > .kva-status {
  position: absolute;
  top: 13px;
  left: 13px;
}

.kva-status-converted {
  background: #dff7e8;
  color: #116431;
}

.kva-status-pending {
  background: #fff3cc;
  color: #795b00;
}

.kva-status-duplicate {
  background: #e8eaf8;
  color: #424c8d;
}

.kva-status-damaged {
  background: #ffe2e1;
  color: #9a2421;
}

.kva-duration {
  position: absolute;
  right: 13px;
  bottom: 13px;
  padding: 5px 8px;
  border-radius: 7px;
  background: rgba(0,0,0,.78);
  color: #ffffff;
  font-size: 12px;
  font-weight: 700;
}

.kva-card-body {
  padding: 21px;
}

.kva-card-heading h3 {
  margin: 5px 0 0;
  font-size: 20px;
  line-height: 1.3;
}

.kva-record-code {
  color: var(--kva-blue);
  font-size: 11px;
  font-weight: 900;
  letter-spacing: .11em;
  text-transform: uppercase;
}

.kva-description {
  min-height: 68px;
  margin: 13px 0 17px;
  color: var(--kva-muted);
  font-size: 13px;
  line-height: 1.65;
}

.kva-metadata {
  display: grid;
  grid-template-columns: 1fr 1fr;
  margin: 0;
  border-top: 1px solid #edf1f4;
  border-left: 1px solid #edf1f4;
}

.kva-metadata > div {
  min-width: 0;
  padding: 11px;
  border-right: 1px solid #edf1f4;
  border-bottom: 1px solid #edf1f4;
}

.kva-metadata dt {
  margin-bottom: 4px;
  color: var(--kva-muted);
  font-size: 10px;
  font-weight: 800;
  text-transform: uppercase;
}

.kva-metadata dd {
  margin: 0;
  overflow-wrap: anywhere;
  font-size: 12px;
  font-weight: 700;
}

.kva-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 7px;
  margin: 15px 0;
}

.kva-tags span {
  padding: 5px 8px;
  border-radius: 7px;
  background: #f0f5f8;
  color: #456277;
  font-size: 10px;
  font-weight: 700;
}

.kva-player {
  border: 1px solid #cdddea;
  border-radius: 11px;
  overflow: hidden;
  background: #f8fbfd;
}

.kva-player summary {
  display: grid;
  grid-template-columns: auto 1fr auto;
  align-items: center;
  gap: 9px;
  min-height: 48px;
  padding: 0 14px;
  background: var(--kva-blue);
  color: #ffffff;
  cursor: pointer;
  font-size: 13px;
  font-weight: 800;
  list-style: none;
}

.kva-player summary::-webkit-details-marker {
  display: none;
}

.kva-player[open] summary {
  background: var(--kva-blue-dark);
}

.kva-expand-icon {
  font-size: 19px;
  transition: transform .2s ease;
}

.kva-player[open] .kva-expand-icon {
  transform: rotate(180deg);
}

.kva-player-shell {
  position: relative;
  aspect-ratio: 16 / 9;
  background: #000000;
}

.kva-player-shell iframe {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  border: 0;
}

.kva-pending-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 13px;
}

.kva-pending-card {
  display: grid;
  grid-template-columns: minmax(0, 1fr) auto;
  gap: 8px 14px;
  align-items: center;
  padding: 17px;
  border: 1px solid var(--kva-border);
  border-radius: 14px;
  background: var(--kva-surface);
}

.kva-pending-card h3 {
  margin: 4px 0 0;
  overflow-wrap: anywhere;
  font-size: 14px;
}

.kva-file-size {
  color: var(--kva-muted);
  font-size: 12px;
  font-weight: 700;
}

.kva-pending-card .kva-status {
  grid-column: 1 / -1;
  justify-self: start;
}

.kva-notice-card {
  display: flex;
  align-items: flex-start;
  gap: 18px;
  padding: 22px;
  border: 1px solid var(--kva-border);
  border-radius: 17px;
  background: var(--kva-surface);
}

.kva-notice-icon {
  display: grid;
  width: 51px;
  height: 51px;
  flex: 0 0 51px;
  place-items: center;
  border-radius: 14px;
  font-size: 22px;
  font-weight: 800;
}

.kva-duplicate-icon {
  background: #eceefa;
  color: #465192;
}

.kva-damaged-icon {
  background: #ffe5e3;
  color: #a52d28;
}

.kva-notice-content {
  flex: 1;
}

.kva-notice-title {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 15px;
}

.kva-notice-title h3 {
  margin: 4px 0 0;
}

.kva-notice-content p {
  margin: 12px 0;
  color: var(--kva-muted);
  line-height: 1.6;
}

.kva-action-note {
  padding: 10px 12px;
  border-radius: 9px;
  background: #f3f6f9;
  font-size: 12px;
  font-weight: 700;
}

.kva-empty-state {
  margin-top: 35px;
  padding: 45px 20px;
  border: 1px dashed #bfcfdb;
  border-radius: 16px;
  text-align: center;
  background: #ffffff;
}

.kva-empty-state strong,
.kva-empty-state span {
  display: block;
}

.kva-empty-state span {
  margin-top: 7px;
  color: var(--kva-muted);
}

.kva-searchable[hidden] {
  display: none !important;
}

@media (max-width: 1050px) {
  .kva-video-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }

  .kva-stats {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }

  .kva-pending-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

@media (max-width: 720px) {
  .kva-page {
    width: min(100% - 20px, 1320px);
    padding-top: 18px;
  }

  .kva-hero {
    display: block;
    min-height: 0;
    padding: 28px 22px;
    border-radius: 18px;
  }

  .kva-hero-badge {
    width: 100%;
    margin-top: 22px;
  }

  .kva-toolbar {
    grid-template-columns: 1fr;
  }

  .kva-result {
    white-space: normal;
  }

  .kva-video-grid,
  .kva-pending-grid {
    grid-template-columns: 1fr;
  }

  .kva-section-header {
    align-items: flex-start;
  }

  .kva-description {
    min-height: 0;
  }
}

@media (max-width: 480px) {
  .kva-stats {
    grid-template-columns: 1fr;
  }

  .kva-metadata {
    grid-template-columns: 1fr;
  }

  .kva-notice-card {
    display: block;
  }

  .kva-notice-icon {
    margin-bottom: 14px;
  }

  .kva-notice-title {
    align-items: flex-start;
  }
}
</style>
<!-- KALD_VIDEO_PRO_STYLE_END -->
'''

pro_script = r'''
<!-- KALD_VIDEO_PRO_SCRIPT_START -->
<script>
(function () {
  const search = document.getElementById("kvaVideoSearch");
  const filter = document.getElementById("kvaStatusFilter");
  const records = Array.from(
    document.querySelectorAll(".kva-searchable")
  );
  const result = document.getElementById("kvaResultCount");
  const empty = document.getElementById("kvaEmptyState");

  function updateResults() {
    const query = (search.value || "").trim().toLowerCase();
    const status = filter.value;
    let visible = 0;

    records.forEach(function (record) {
      const searchable = (
        record.dataset.search ||
        record.textContent ||
        ""
      ).toLowerCase();

      const statusMatches =
        status === "all" ||
        record.dataset.status === status;

      const queryMatches =
        !query ||
        searchable.includes(query);

      const show = statusMatches && queryMatches;
      record.hidden = !show;

      if (show) {
        visible += 1;
      }
    });

    result.textContent =
      "Showing " + visible + " of " + records.length + " archive records";

    empty.hidden = visible !== 0;
  }

  search.addEventListener("input", updateResults);
  filter.addEventListener("change", updateResults);

  document
    .querySelectorAll(".kva-player")
    .forEach(function (details) {
      details.addEventListener("toggle", function () {
        const frame = details.querySelector("iframe");

        if (!frame) {
          return;
        }

        if (details.open) {
          if (
            !frame.src ||
            frame.src === "about:blank" ||
            frame.src.endsWith("/about:blank")
          ) {
            frame.src = frame.dataset.src;
          }
        } else {
          frame.src = "about:blank";
        }
      });
    });

  updateResults();
})();
</script>
<!-- KALD_VIDEO_PRO_SCRIPT_END -->
'''

# Remove a previous copy of this professional style/script
html = re.sub(
    r'<!-- KALD_VIDEO_PRO_STYLE_START -->.*?<!-- KALD_VIDEO_PRO_STYLE_END -->',
    '',
    html,
    flags=re.S
)

html = re.sub(
    r'<!-- KALD_VIDEO_PRO_SCRIPT_START -->.*?<!-- KALD_VIDEO_PRO_SCRIPT_END -->',
    '',
    html,
    flags=re.S
)

# Replace the complete existing main page content
main_pattern = re.compile(
    r'<main\b[^>]*>.*?</main>',
    flags=re.I | re.S
)

if not main_pattern.search(html):
    print("ERROR: The <main> section was not found in videos.html.")
    print("No changes were saved.")
    sys.exit(1)

html = main_pattern.sub(new_main.strip(), html, count=1)

if "</head>" not in html or "</body>" not in html:
    print("ERROR: Invalid videos.html structure.")
    sys.exit(1)

html = html.replace("</head>", pro_style + "\n</head>", 1)
html = html.replace("</body>", pro_script + "\n</body>", 1)

page.write_text(html, encoding="utf-8")

print("SUCCESS: Professional video archive layout created.")
print("Backup:", backup)
print("Converted videos: 3")
print("Pending ISOs: 9")
print("Embedded players: CD122V, CD113V, CD118V")
