"""
Architecture figure (paper Fig. 2): draw.io diagram -> rendered with the draw.io viewer in headless Edge.

Outputs (run from the repository root):
  figures/fig4_architecture_diagram_io.drawio   editable in diagrams.net
  figures/fig4_architecture.png                 3x screenshot, cropped to the drawing
  figures/fig4_architecture.pdf                 that PNG on a page of the drawing's size

Layout grid (1x px): 306-320-306 px columns with 80 px gaps for the flow labels, two 116 px boxes per column
with a 32 px gap for the vertical arrow, labels placed beside their arrows, canvas cropped to the content.
Labels follow the camera-ready text: delay-critical GBR 5QI 82-85 and the pre-registered miss threshold
z_miss = 2.0.
"""
import html
import json
import os
import subprocess

import fitz

W_PAGE, H_PAGE = 1115, 420
COL_Y, COL_H, HDR = 44, 304, 24
COLS = {"tx": (12, 306), "ran": (398, 320), "rx": (798, 306)}
BOX_X, BOX_H, BOX1_Y, BOX2_Y = 8, 116, 32, 180          # relative to the column
SCALE = 3                                               # raster scale of the rendered figure
FONT = "font-family:Helvetica,Arial,sans-serif;"
_cells = []


def esc(s):
    return html.escape(s, quote=True)


def cell(cid, value, style, x, y, w, h, parent="1", vertex=True):
    kind = 'vertex="1"' if vertex else 'edge="1"'
    _cells.append(f'<mxCell id="{cid}" value="{esc(value)}" style="{style}" {kind} parent="{parent}">'
                  f'<mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry" /></mxCell>')


def text(cid, value, x, y, w, h, align="center", valign="middle"):
    cell(cid, value, f"text;html=1;align={align};verticalAlign={valign};whiteSpace=wrap;strokeColor=none;"
         "fillColor=none;spacing=0;", x, y, w, h)


def arrow(cid, pts, color, width=2.2):
    (x0, y0), (x1, y1), mids = pts[0], pts[-1], pts[1:-1]
    arr = "".join(f'<mxPoint x="{x}" y="{y}" />' for x, y in mids)
    arr = f'<Array as="points">{arr}</Array>' if mids else ""
    _cells.append(f'<mxCell id="{cid}" value="" style="edgeStyle=none;html=1;rounded=0;strokeColor={color};'
                  f'strokeWidth={width};endArrow=block;endFill=1;endSize=5;" edge="1" parent="1">'
                  f'<mxGeometry relative="1" as="geometry"><mxPoint x="{x0}" y="{y0}" as="sourcePoint" />'
                  f'<mxPoint x="{x1}" y="{y1}" as="targetPoint" />{arr}</mxGeometry></mxCell>')


def box_html(w, h, header, hdr_bg, hdr_fg, hdr_line, bullets, footer=None, ft_bg=None, ft_line=None, ft_fg=None,
             ft_size=11, cards=None):
    head = (f'<div style="background:{hdr_bg};color:{hdr_fg};font-weight:bold;font-size:11.5px;text-align:center;'
            f'padding:4px 0;border-bottom:1px solid {hdr_line};border-radius:3px 3px 0 0;">{header}</div>')
    if cards:
        body = "".join(
            f'<div style="margin:5px 8px 0 8px;background:{bg};border:1px solid {line};border-radius:3px;'
            f'padding:2px 7px;text-align:left;line-height:1.3;"><b style="color:{fg};font-size:11px;">{title}</b><br>'
            f'<span style="color:{fg2};font-size:9.5px;">{sub}</span></div>'
            for bg, line, fg, fg2, title, sub in cards)
        tail = '<div style="height:6px;"></div>'
    else:
        body = (f'<div style="padding:5px 12px 0 12px;font-size:11px;line-height:1.5;color:#334155;text-align:left;">'
                + "".join(f"<div>&bull; {b}</div>" for b in bullets) + "</div>")
        tail = (f'<div style="margin:0 8px 7px 8px;background:{ft_bg};border:1px solid {ft_line};border-radius:3px;'
                f'color:{ft_fg};font-size:{ft_size}px;font-weight:bold;text-align:center;padding:3px 2px;">{footer}</div>')
    return (f'<div style="width:{w - 2}px;height:{h - 2}px;display:flex;flex-direction:column;'
            f'justify-content:space-between;{FONT}">{head}{body}{tail}</div>')


def box(cid, col, rel_y, label, stroke):
    cx, cw = COLS[col]
    cell(cid, label, f"rounded=1;arcSize=3;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor={stroke};"
         "strokeWidth=1.2;overflow=hidden;align=left;verticalAlign=top;spacing=0;", BOX_X, rel_y, cw - 16, BOX_H,
         parent=f"col_{col}")


def b(s):
    return f'<b style="color:#0f172a;">{s}</b>'


def build_xml():
    _cells.clear()
    text("title", '<b style="font-size:15px;color:#0f172a;">FOUR-LAYER DIAGNOSTIC-AWARE TELE-RADIOLOGY ARCHITECTURE '
         '(DARDO + CSA + 5G URLLC)</b><br><span style="font-size:11.5px;color:#475569;">Mobile Stroke Unit (MSU) '
         'Scanner &rarr; Dual-Slice 5G Cellular RAN &rarr; Hospital Edge AI Safety Audit</span>',
         0, 4, W_PAGE, 34)
    for col, title in (("tx", "TRANSMITTER: MOBILE STROKE UNIT (MSU)"),
                       ("ran", "5G / B5G CELLULAR RADIO ACCESS NETWORK"),
                       ("rx", "RECEIVER: HOSPITAL EDGE SERVER")):
        x, w = COLS[col]
        cell(f"col_{col}", f"<b>{title}</b>", f"swimlane;whiteSpace=wrap;html=1;startSize={HDR};fillColor=#0f172a;"
             "strokeColor=#cbd5e1;strokeWidth=1.5;fontColor=#ffffff;fontFamily=Helvetica;fontSize=12;align=center;"
             "swimlaneFillColor=#f8fafc;rounded=1;arcSize=3;", x, COL_Y, w, COL_H)

    wtx, wran, wrx = (COLS[c][1] - 16 for c in ("tx", "ran", "rx"))
    box("l1", "tx", BOX1_Y, box_html(
        wtx, BOX_H, 'LAYER 1: TASK PROFILER (CSA) <span style="font-weight:normal;font-size:10px;">&mdash; '
        'Lesion Prior</span>', "#e0f2fe", "#0369a1", "#7dd3fc",
        [f'{b("Raw Data:")} Multi-coil <i>k</i>-space <b>Y</b> &isin; &#x2102;<sup>C&times;K</sup>',
         f'{b("Task Prior:")} <b style="color:#0284c7;"><i>W(k<sub>x</sub>,k<sub>y</sub>) = '
         f'|&#x2131;{{w<sub>CHO</sub>}}|<sup>2</sup></i></b>'],
        'Safety Target: Detectability <i>z</i><sub>CHO</sub> &ge; 2.0', "#f0f9ff", "#38bdf8", "#0284c7"), "#bae6fd")
    box("l2", "tx", BOX2_Y, box_html(
        wtx, BOX_H, "LAYER 2: DIAGNOSTIC COMPRESSION (DARDO)", "#dcfce7", "#15803d", "#86efac",
        [f'{b("Diagnostic Grad:")} <b style="color:#15803d;">&gamma;<sub>k</sub> = &sum;<sub>y</sub> W(k,y) '
         f'||&#x2131;S<sub>k</sub>||<sub>2</sub></b>',
         f'{b("Greedy Split:")} Sort in &lt; 2 ms &rArr; <b style="color:#ea580c;">K<sub>diag</sub></b> vs. '
         f'<b style="color:#64748b;">K<sub>bulk</sub></b>'],
        "Safety Probe: 128-B Token &theta; in Header", "#f0fdf4", "#4ade80", "#166534"), "#bbf7d0")
    box("urllc", "ran", BOX1_Y, box_html(
        wran, BOX_H, "LAYER 3: 5G URLLC SLICE (MISSION-CRITICAL)", "#ffedd5", "#c2410c", "#fdba74",
        [f'{b("Payload:")} <b style="color:#ea580c;">K<sub>diag</sub> = {{k | &gamma;<sub>k</sub> &ge; &tau;}}</b> + '
         f'<b style="color:#15803d;">Token &theta;</b>',
         f'{b("3GPP QoS:")} 5QI 82&ndash;85 (BLER &lt; 10<sup>&minus;5</sup>, &lt; 10 ms)'],
        "Channel: Dedicated BWP (Zero Burst Drop)", "#fff7ed", "#fb923c", "#c2410c"), "#fed7aa")
    box("embb", "ran", BOX2_Y, box_html(
        wran, BOX_H, "LAYER 3: 5G eMBB SLICE (BULK ANATOMY)", "#f1f5f9", "#334155", "#cbd5e1",
        [f'{b("Bulk Payload:")} <b style="color:#475569;">K<sub>bulk</sub> = {{k | &gamma;<sub>k</sub> &lt; &tau;}}</b>'
         ' <i style="color:#64748b;">(Skull Context)</i>',
         f'{b("Policy:")} Dynamic DASH Streaming <i style="color:#64748b;">(Loss-Tolerant)</i>'],
        "Throughput: Best-Effort (Absorbs Congestion)", "#f8fafc", "#94a3b8", "#475569"), "#cbd5e1")
    box("recon", "rx", BOX1_Y, box_html(
        wrx, BOX_H, "EDGE AI RECONSTRUCTION (VarNet)", "#ede9fe", "#6d28d9", "#c4b5fd",
        [f'{b("Stream Fusion:")} <b>Y</b><sub>URLLC</sub> &cup; <b>Y</b><sub>eMBB</sub>',
         f'{b("Deep Recon:")} <b style="color:#6d28d9;">X&#770; = &#x211b;<sub>&theta;</sub>(Y)</b> in 1.8 s on '
         'Edge GPU'],
        'Residual: Passed ||AX&#770; &minus; Y|| &lt; &sigma;<sub>&eta;</sub> (Null-Space Blind)',
        "#f5f3ff", "#c4b5fd", "#7c3aed", ft_size=10), "#ddd6fe")
    box("l4", "rx", BOX2_Y, box_html(
        wrx, BOX_H, "LAYER 4: SEMANTIC AUDIT &amp; DECISION GATE", "#ffe4e6", "#be123c", "#fecdd3", None,
        cards=[("#f0fdf4", "#86efac", "#15803d", "#166534", "&#x2714; z &ge; 2.0 (AUDIT PASSED: STROKE INTACT)",
                "<i>z</i><sub>recon</sub> &ge; <i>z</i><sub>miss</sub> &rarr; Released to PACS &amp; Clinician"),
               ("#fef2f2", "#fca5a5", "#b91c1c", "#dc2626", "&#x2718; z &lt; 2.0 (AUDIT FAILED: STROKE ERASED)",
                "<b>Silent Erasure Alert &rArr; Trigger Targeted S-NACK</b>")]), "#fecdd3")

    # vertical arrows inside the transmitter and receiver, label to the right of the arrow
    for cid, col, lab, color in (("a_tx", "tx", "Prior W(k<sub>x</sub>,k<sub>y</sub>)", "#0284c7"),
                                 ("a_rx", "rx", "Reconstructed X&#770; + &theta;", "#6d28d9")):
        x, w = COLS[col]
        xc = x + w / 2
        y0, y1 = COL_Y + BOX1_Y + BOX_H, COL_Y + BOX2_Y
        arrow(cid, [(xc, y0 + 1), (xc, y1 - 1)], color, 1.6)
        text(cid + "_lab", f'<b style="color:{color};font-size:10px;">{lab}</b>', xc + 7, y0 + 8, 150, 16, "left")

    # inter-column flows, label centred above each arrow
    gaps = ((COLS["tx"][0] + COLS["tx"][1], COLS["ran"][0]), (COLS["ran"][0] + COLS["ran"][1], COLS["rx"][0]))
    for i, (g0, g1) in enumerate(gaps):
        for name, sub, color, lc, rel in (("URLLC Flow", "K<sub>diag</sub> + &theta;", "#ea580c", "#c2410c", BOX1_Y),
                                          ("eMBB Flow", "K<sub>bulk</sub>", "#64748b", "#475569", BOX2_Y)):
            y = COL_Y + rel + BOX_H / 2 + 6
            arrow(f"f_{name[:4]}_{i}", [(g0, y), (g1, y)], color, 2.4)
            text(f"f_{name[:4]}_{i}_lab", f'<b style="color:{lc};font-size:10.5px;">{name}</b><br>'
                 f'<span style="color:{lc};font-size:9.5px;">{sub}</span>', g0, y - 32, g1 - g0, 28)

    # closed loop: Layer 4 -> S-NACK banner -> transmitter
    by, bh, bx, bw = COL_Y + COL_H + 18, 46, 232, 651
    cell("snack", '<div style="' + FONT + 'text-align:center;"><div style="color:#991b1b;font-size:12px;'
         'font-weight:bold;">CLOSED-LOOP S-NACK RETRANSMISSION PROTOCOL</div><div style="color:#7f1d1d;'
         'font-size:10.5px;margin-top:3px;">Smart Recovery: Requests only missing high-&gamma;<sub>k</sub> bands '
         '(&Delta;k &asymp; 1.2 MB, &Delta;t &asymp; 15 ms) &mdash; Avoids 200 MB full retransmission</div></div>',
         "rounded=1;arcSize=4;whiteSpace=wrap;html=1;fillColor=#fef2f2;strokeColor=#fca5a5;strokeWidth=1.3;"
         "align=center;verticalAlign=middle;", bx, by, bw, bh)
    ym = by + bh / 2
    xr = COLS["rx"][0] + COLS["rx"][1] / 2
    xl = COLS["tx"][0] + COLS["tx"][1] / 2
    arrow("loop_r", [(xr, COL_Y + COL_H), (xr, ym), (bx + bw, ym)], "#dc2626")
    arrow("loop_l", [(bx, ym), (xl, ym), (xl, COL_Y + COL_H)], "#dc2626")
    text("loop_r_lab", '<b style="color:#b91c1c;font-size:10px;">Audit Failed<br>(Stroke Erased)</b>',
         xr + 8, COL_Y + COL_H + 6, 120, 28, "left")
    text("loop_l_lab", '<b style="color:#b91c1c;font-size:10px;">Targeted S-NACK<br>(Resend Missing &Delta;k)</b>',
         xl - 8 - 140, COL_Y + COL_H + 6, 140, 28, "right")

    body = "\n        ".join(_cells)
    return f"""<mxfile host="app.diagrams.net" type="device">
  <diagram id="fig_architecture" name="Architecture">
    <mxGraphModel dx="{W_PAGE}" dy="{H_PAGE}" grid="1" gridSize="5" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="{W_PAGE}" pageHeight="{H_PAGE}" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        {body}
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>"""


# Muted palette (19 Nov 2026): the Tailwind-bright hues are mapped to desaturated tones that match the paper's other
# schematics. The URLLC slice is blue, the colour of the priority slice in every results figure; eMBB stays grey.
MUTED = {
    # Layer 1, CSA (sky -> slate blue)
    "#e0f2fe": "#e3ebf2", "#0369a1": "#2e4a66", "#7dd3fc": "#b3c6d8", "#f0f9ff": "#f4f7fa",
    "#38bdf8": "#b3c6d8", "#0284c7": "#3d6a8f", "#bae6fd": "#c9d6e2",
    # Layer 2, DARDO (green -> muted teal)
    "#dcfce7": "#e2eeec", "#15803d": "#2f6a5c", "#86efac": "#b2d1c8", "#f0fdf4": "#f2f7f5",
    "#4ade80": "#b2d1c8", "#166534": "#2f5f52", "#bbf7d0": "#cadfd8",
    # Layer 3, URLLC slice (orange -> priority blue)
    "#ffedd5": "#e3ecf6", "#c2410c": "#2b5a8a", "#fdba74": "#aec5de", "#fff7ed": "#f4f8fc",
    "#fb923c": "#aec5de", "#ea580c": "#3b6ea5", "#fed7aa": "#c8d8ea",
    # edge reconstruction (violet -> slate violet)
    "#ede9fe": "#ebe9f1", "#6d28d9": "#4f4a73", "#c4b5fd": "#c5c1d6", "#f5f3ff": "#f6f5f9",
    "#7c3aed": "#5a5480", "#ddd6fe": "#d6d3e2",
    # Layer 4 and the S-NACK loop (red -> muted brick)
    "#ffe4e6": "#f1e5e5", "#be123c": "#7a3a3a", "#fecdd3": "#dbc1c1", "#fef2f2": "#f8f1f0",
    "#fca5a5": "#d9b3ae", "#b91c1c": "#8c3a32", "#dc2626": "#a8463d", "#991b1b": "#7d3530",
    "#7f1d1d": "#6b3330",
}


def recolor(s):
    for bright, muted in MUTED.items():
        s = s.replace(bright, muted)
    return s


def main():
    xml = recolor(build_xml())
    fig_dir = os.path.abspath("figures")
    with open(os.path.join(fig_dir, "fig4_architecture_diagram_io.drawio"), "w", encoding="utf-8") as f:
        f.write(xml)
    viewer = "file:///" + os.path.abspath("scratch/viewer-static.min.js").replace("\\", "/")
    page = f"""<!DOCTYPE html><html><head><meta charset="utf-8">
<script type="text/javascript" src="{viewer}"></script>
<style>@page {{ size: {W_PAGE}px {H_PAGE}px; margin: 0; }}
* {{ box-sizing: border-box; }} html, body {{ margin: 0; padding: 0; width: {W_PAGE}px; height: {H_PAGE}px;
overflow: hidden; background: #ffffff; }} .mxgraph {{ width: {W_PAGE}px; height: {H_PAGE}px; }}</style></head>
<body><div id="c"></div><script>
const d = document.createElement('div'); d.className = 'mxgraph';
d.setAttribute('data-mxgraph', JSON.stringify({{nav: false, resize: false, toolbar: '', border: 0, xml: {json.dumps(xml)}}}));
document.getElementById('c').appendChild(d); GraphViewer.processElements();
</script></body></html>"""
    page = page.replace(f"height: {H_PAGE}px", f"height: {H_PAGE + 80}px")   # room for the viewer's offset
    html_file = os.path.abspath("scratch/render_fig4.html")
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(page)
    edge = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    url = "file:///" + html_file.replace("\\", "/")
    raw = os.path.abspath("scratch/fig4_raw.png")
    if os.path.exists(raw):
        os.remove(raw)
    subprocess.run([edge, "--headless", "--disable-gpu", "--virtual-time-budget=4000",
                    f"--window-size={W_PAGE},{H_PAGE + 80}", f"--force-device-scale-factor={SCALE}",
                    f"--screenshot={raw}", url], check=True)
    import time
    for _ in range(60):                     # Edge may hand the work to a child process and return early
        if os.path.exists(raw) and os.path.getsize(raw) > 0:
            time.sleep(0.5)
            break
        time.sleep(0.5)

    # crop to the drawn content plus a small even margin
    pix = fitz.Pixmap(raw)
    import numpy as np
    a = np.frombuffer(pix.samples, np.uint8).reshape(pix.height, pix.width, pix.n)[..., :3]
    ink = np.where((a < 245).any(axis=2))
    pad = 6 * SCALE
    y0, y1 = max(ink[0].min() - pad, 0), min(ink[0].max() + pad, pix.height)
    x0, x1 = max(ink[1].min() - pad, 0), min(ink[1].max() + pad, pix.width)
    src = fitz.open(raw)
    rect = fitz.Rect(x0, y0, x1, y1) * (src[0].rect.width / pix.width)
    png = os.path.join(fig_dir, "fig4_architecture.png")
    clip = src[0].get_pixmap(clip=rect, matrix=fitz.Matrix(pix.width / src[0].rect.width, pix.width / src[0].rect.width))
    clip.save(png)
    pdf = os.path.join(fig_dir, "fig4_architecture.pdf")
    out = fitz.open()
    w_pt, h_pt = clip.width / SCALE * 0.75, clip.height / SCALE * 0.75   # CSS px -> pt
    pg = out.new_page(width=w_pt, height=h_pt)
    pg.insert_image(pg.rect, filename=png)
    out.save(pdf, deflate=True)
    print(f"wrote {png} ({clip.width} x {clip.height} px) and {pdf} ({w_pt:.0f} x {h_pt:.0f} pt)")


if __name__ == "__main__":
    main()
