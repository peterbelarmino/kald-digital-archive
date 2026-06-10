$files = @("index.html","photos.html","photos-2016.html","photos-2017.html","videos.html","documents.html","reports.html","dashboard.html","about.html")

foreach ($file in $files) {
    $content = Get-Content $file -Raw

    $content = $content -replace '<nav><div class="brand"><img src="assets/logo.jpg"><span>KALD Digital Archive</span></div><div>', '<nav><a class="brand" href="index.html"><img src="assets/logo.jpg"><span>KALD Digital Archive</span></a><div class="nav-links">'

    $content = $content -replace '<nav>\s*<div class="brand"><img src="assets/logo.jpg"><span>KALD Digital Archive</span></div>\s*<div>', '<nav><a class="brand" href="index.html"><img src="assets/logo.jpg"><span>KALD Digital Archive</span></a><div class="nav-links">'

    $content = $content -replace '<div class="brand"><img src="assets/logo.jpg"><span>KALD Digital Archive</span></div>\s*<div>', '<a class="brand" href="index.html"><img src="assets/logo.jpg"><span>KALD Digital Archive</span></a><div class="nav-links">'

    $content = $content -replace 'nav\{[^}]*\}', 'nav{background:white;padding:14px 38px;display:flex;justify-content:space-between;align-items:center;box-shadow:0 2px 12px #0001;position:sticky;top:0;z-index:999}'

    $content = $content -replace 'nav a\{[^}]*\}', 'nav a{text-decoration:none;color:#0b4f8a;font-weight:700}'

    $content = $content -replace '\.brand\{[^}]*\}', '.brand{display:flex;align-items:center;gap:12px;font-weight:800;color:#0b4f8a;text-decoration:none}'

    if ($content -notmatch '\.nav-links') {
        $content = $content -replace '</style>', '.nav-links{display:flex;align-items:center;gap:18px;margin-left:auto}.nav-links a{margin-left:0;text-decoration:none;color:#0b4f8a;font-weight:700}@media(max-width:760px){nav{padding:12px 14px;flex-wrap:wrap}.brand{width:100%;justify-content:center;margin-bottom:8px}.nav-links{width:100%;justify-content:center;flex-wrap:wrap;gap:12px}.nav-links a{font-size:14px}}</style>'
    } else {
        $content = $content -replace '\.nav-links\{[^}]*\}', '.nav-links{display:flex;align-items:center;gap:18px;margin-left:auto}'
    }

    Set-Content $file $content
}

