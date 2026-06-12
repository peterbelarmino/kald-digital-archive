from pathlib import Path
import re

mobile_css = """
<style id="mobile-fix">
@media (max-width: 768px){
  nav{
    padding:12px 14px !important;
    flex-direction:column !important;
    align-items:flex-start !important;
    gap:10px !important;
  }
  .brand{
    width:100% !important;
    font-size:16px !important;
  }
  .brand img{
    height:42px !important;
  }
  .nav-links{
    width:100% !important;
    display:flex !important;
    flex-wrap:wrap !important;
    gap:8px !important;
    margin-left:0 !important;
  }
  .nav-links a{
    background:#eef6fc !important;
    padding:8px 10px !important;
    border-radius:8px !important;
    font-size:13px !important;
  }
  .hero{
    padding:34px 16px !important;
  }
  .hero h1{
    font-size:26px !important;
    line-height:1.2 !important;
  }
  .hero p{
    font-size:15px !important;
  }
  .section,.actions,.gallery{
    padding:14px !important;
  }
  .grid{
    grid-template-columns:1fr !important;
  }
  .card{
    padding:18px !important;
  }
  table{
    display:block !important;
    overflow-x:auto !important;
    white-space:nowrap !important;
  }
  th,td{
    font-size:13px !important;
    padding:10px !important;
  }
  .gallery{
    grid-template-columns:repeat(2,1fr) !important;
    gap:10px !important;
  }
  .photo img{
    height:130px !important;
  }
  .viewer .topbar{
    top:8px !important;
    left:8px !important;
    right:8px !important;
    flex-direction:column !important;
    gap:8px !important;
    text-align:center !important;
  }
  .viewer button{
    padding:8px 10px !important;
    font-size:12px !important;
  }
  .viewer img{
    max-width:96% !important;
    max-height:68vh !important;
  }
  .viewer .prev{
    left:6px !important;
  }
  .viewer .next{
    right:6px !important;
  }
  .viewer .navbtn{
    font-size:22px !important;
  }
  input,select{
    width:100% !important;
    box-sizing:border-box !important;
  }
}
</style>
"""

for file in Path(".").glob("*.html"):
    text = file.read_text(encoding="utf-8", errors="ignore")
    if 'id="mobile-fix"' not in text:
        text = text.replace("</head>", mobile_css + "\n</head>")
        file.write_text(text, encoding="utf-8")
        print("Mobile fixed:", file.name)

print("Done.")
