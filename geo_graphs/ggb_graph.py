import zipfile, io

# Create simple GeoGebra XML
xml = """<?xml version="1.0" encoding="utf-8"?>
<geogebra format="5.0">
 <construction>
  <element type="point" label="1">
   <coords x="0" y="1" z="1"/>
  </element>
  <element type="point" label="2">
   <coords x="0.951" y="0.309" z="1"/>
  </element>
  <element type="point" label="3">
   <coords x="0.588" y="-0.809" z="1"/>
  </element>
  <element type="point" label="4">
   <coords x="-0.588" y="-0.809" z="1"/>
  </element>
  <element type="point" label="5">
   <coords x="-0.951" y="0.309" z="1"/>
  </element>
"""

# Add all segments between all pairs
points = ["1","2","3","4","5"]
for i in range(5):
    for j in range(i+1,5):
        xml += f"""
  <element type="segment" label="s{points[i]}{points[j]}">
    <pointRef label="{points[i]}"/>
    <pointRef label="{points[j]}"/>
  </element>
"""
xml += "\n </construction>\n</geogebra>"

# Create zip (.ggb)
buffer = io.BytesIO()
with zipfile.ZipFile(buffer, 'w', zipfile.ZIP_DEFLATED) as z:
    z.writestr("geogebra.xml", xml)

with open('K5.ggb','wb') as f:
    f.write(buffer.getvalue())

'K5.ggb'
