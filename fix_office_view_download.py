from pathlib import Path
import re, urllib.parse

p = Path("documents.html")
text = p.read_text(encoding="utf-8", errors="ignore")

base = "https://peterbelarmino.github.io/kald-digital-archive/"

def fix_actions(m):
    dtype = m.group(1)
    name = m.group(2)
    size = m.group(4)
    action = m.group(5)

    href = re.search(r'href="([^"]+)"', action)
    if not href:
        return m.group(0)

    file_path = href.group(1)

    # kung may old viewer link, kunin ulit ang original file url
    if "docs.google.com" in file_path and "url=" in file_path:
        file_path = urllib.parse.unquote(file_path.split("url=")[-1])
        file_path = file_path.replace(base, "")

    if "view.officeapps.live.com" in file_path and "src=" in file_path:
        file_path = urllib.parse.unquote(file_path.split("src=")[-1])
        file_path = file_path.replace(base, "")

    file_url = base + file_path.replace(" ", "%20")

    if dtype == "PDF":
        view_url = file_path
        view_label = "View PDF"
    elif dtype in ["Word", "Excel", "PowerPoint"]:
        view_url = "https://view.officeapps.live.com/op/embed.aspx?src=" + urllib.parse.quote(file_url, safe="")
        view_label = "View"
    else:
        view_url = file_path
        view_label = "View"

    buttons = f'<a class="btn" href="{view_url}" target="_blank" rel="noopener">{view_label}</a> <a class="btn" href="{file_path}" download>Download</a>'

    return f'<tr data-type="{dtype}">\n<td>{name}</td>\n<td>{dtype}</td>\n<td>{size}</td>\n<td>{buttons}</td>\n</tr>'

text = re.sub(
    r'<tr data-type="([^"]+)">\s*<td>(.*?)</td>\s*<td>(.*?)</td>\s*<td>(.*?)</td>\s*<td>(.*?)</td>\s*</tr>',
    fix_actions,
    text,
    flags=re.S
)

p.write_text(text, encoding="utf-8")
print("Documents updated: PDF, Word, Excel, PowerPoint now have View + Download.")
