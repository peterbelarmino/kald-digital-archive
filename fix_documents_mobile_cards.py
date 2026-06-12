from pathlib import Path

p = Path("documents.html")
text = p.read_text(encoding="utf-8", errors="ignore")

mobile_doc_css = """
<style id="documents-mobile-cards">
@media(max-width:768px){
  .section{padding:14px!important;margin:18px auto!important}
  .stats{grid-template-columns:1fr 1fr!important;gap:10px!important}
  .card{padding:14px!important}
  .card h2{font-size:28px!important}
  table, thead, tbody, th, td, tr{display:block!important}
  thead{display:none!important}
  table{box-shadow:none!important;background:transparent!important;white-space:normal!important;overflow:visible!important}
  tbody tr{
    background:white!important;
    margin:12px 0!important;
    padding:14px!important;
    border-radius:16px!important;
    box-shadow:0 5px 14px #0002!important;
  }
  tbody td{
    border:0!important;
    padding:6px 0!important;
    white-space:normal!important;
    word-break:break-word!important;
    font-size:14px!important;
  }
  tbody td:nth-child(1){
    font-weight:800!important;
    color:#0b4f8a!important;
    font-size:15px!important;
  }
  tbody td:nth-child(2)::before{content:"Type: ";font-weight:800;color:#526173}
  tbody td:nth-child(3)::before{content:"Size: ";font-weight:800;color:#526173}
  tbody td:nth-child(4){
    display:flex!important;
    gap:8px!important;
    flex-wrap:wrap!important;
    margin-top:8px!important;
  }
  tbody td:nth-child(4) .btn{
    flex:1!important;
    text-align:center!important;
    min-width:110px!important;
  }
}
</style>
"""

if 'id="documents-mobile-cards"' not in text:
    text = text.replace("</head>", mobile_doc_css + "\n</head>")

# remove desktop.ini row if present
text = "\n".join([line for line in text.splitlines() if "desktop.ini" not in line])

p.write_text(text, encoding="utf-8")
print("documents.html mobile card layout applied and desktop.ini removed")
