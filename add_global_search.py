from pathlib import Path

f=Path("dashboard.html")

html=f.read_text(encoding="utf-8")

if "globalSearch" not in html:

    searchbox='''
<section style="max-width:1100px;margin:auto;padding:20px">
<h2>Global Archive Search</h2>

<input id="globalSearch"
placeholder="Search photos, documents, videos..."
style="width:100%;padding:14px;border:1px solid #ccc;border-radius:12px;font-size:16px">

<div id="searchResults"
style="margin-top:15px"></div>
</section>
'''

    html=html.replace("</body>",searchbox + """

<script src="search-data.js"></script>

<script>

const input=document.getElementById("globalSearch");
const results=document.getElementById("searchResults");

input.addEventListener("input",()=>{

const q=input.value.toLowerCase();

if(q.length<2){
results.innerHTML="";
return;
}

const matches=archiveData.filter(item=>
item.title.toLowerCase().includes(q)
);

results.innerHTML=matches.map(item=>`
<div style="background:white;padding:12px;margin:8px 0;border-radius:10px;box-shadow:0 2px 8px #0001">
<a href="${item.url}" style="font-weight:bold">${item.title}</a>
<br>
<small>${item.type}</small>
</div>
`).join("");

});

</script>

</body>
""")

    f.write_text(html,encoding="utf-8")
    print("Dashboard search added")

else:
    print("Search already exists")
