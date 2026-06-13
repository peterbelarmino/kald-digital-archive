from pathlib import Path

p = Path("documents.html")
text = p.read_text(encoding="utf-8", errors="ignore")

css = """
<style id="document-action-fix">
.doc-action-label{font-weight:800;color:#526173;margin-bottom:6px;display:block}
@media(max-width:768px){
  tbody td:nth-child(4)::before{
    content:"Action";
    display:block;
    font-weight:900;
    color:#0b4f8a;
    margin-bottom:8px;
  }
  tbody td:nth-child(4){
    background:#f1f7fc!important;
    padding:12px!important;
    border-radius:12px!important;
  }
  tbody td:nth-child(4) .btn{
    display:block!important;
    width:100%!important;
    margin:6px 0!important;
    padding:12px!important;
    font-size:15px!important;
  }
}
</style>
"""

if 'id="document-action-fix"' not in text:
    text = text.replace("</head>", css + "\n</head>")

p.write_text(text, encoding="utf-8")
print("Document action buttons fixed for mobile.")
