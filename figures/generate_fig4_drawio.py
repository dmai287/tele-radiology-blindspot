import os, json, subprocess
import fitz

def build_wide_drawio_xml():
    xml = """<mxfile host="app.diagrams.net" modified="2026-09-25T08:30:00.000Z" agent="Mozilla/5.0" version="21.6.8" type="device">
  <diagram id="fig4_dardo_architecture" name="Figure 4 Architecture">
    <mxGraphModel dx="1700" dy="540" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1700" pageHeight="540" math="1" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />

        <!-- ========================================== -->
        <!-- MAIN TITLE                                 -->
        <!-- ========================================== -->
        <mxCell id="title" value="&lt;b style=&quot;font-size: 14.5px; letter-spacing: 0.3px; color: #0f172a;&quot;&gt;FOUR-LAYER DIAGNOSTIC-AWARE TELE-RADIOLOGY ARCHITECTURE (DARDO + CSA + 5G URLLC)&lt;/b&gt;&lt;br&gt;&lt;span style=&quot;font-size: 10.5px; color: #475569; font-weight: normal;&quot;&gt;End-to-End Clinical Safety Pipeline: Mobile Stroke Unit (MSU) &amp;rarr; Dual-Slice 5G Cellular RAN &amp;rarr; Hospital Edge AI Safety Audit&lt;/span&gt;" style="text;html=1;align=center;verticalAlign=middle;resizable=0;points=[];autosize=1;strokeColor=none;fillColor=none;fontFamily=Helvetica;" vertex="1" parent="1">
          <mxGeometry x="350" y="8" width="1000" height="38" as="geometry" />
        </mxCell>

        <!-- ========================================== -->
        <!-- COLUMN 1: TRANSMITTER (MSU)                -->
        <!-- ========================================== -->
        <mxCell id="col_tx" value="&lt;b&gt;TRANSMITTER: MOBILE STROKE UNIT (MSU)&lt;/b&gt;" style="swimlane;whiteSpace=wrap;html=1;startSize=28;fillColor=#0f172a;strokeColor=#cbd5e1;strokeWidth=1.5;fontColor=#ffffff;fontFamily=Helvetica;fontSize=10.5;align=center;swimlaneFillColor=#f8fafc;rounded=1;arcSize=3;" vertex="1" parent="1">
          <mxGeometry x="30" y="52" width="480" height="385" as="geometry" />
        </mxCell>

        <!-- Layer 1 Box -->
        <mxCell id="l1_box" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#bae6fd;strokeWidth=1.2;arcSize=3;" vertex="1" parent="col_tx">
          <mxGeometry x="15" y="38" width="450" height="152" as="geometry" />
        </mxCell>
        <mxCell id="l1_hdr" value="&lt;b&gt;LAYER 1: CLINICAL TASK PROFILER (CSA)&lt;/b&gt; &amp;mdash; &lt;span style=&quot;font-size:9px;font-weight:normal;color:#0284c7;&quot;&gt;Identifies lesion frequency bands&lt;/span&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#e0f2fe;strokeColor=#7dd3fc;strokeWidth=1;fontColor=#0369a1;fontSize=10;fontFamily=Helvetica;arcSize=3;align=center;" vertex="1" parent="l1_box">
          <mxGeometry x="0" y="0" width="450" height="24" as="geometry" />
        </mxCell>
        <mxCell id="l1_txt" value="&lt;div style=&quot;padding: 4px 6px; font-family: Helvetica; font-size: 10px; line-height: 1.5; color: #334155;&quot;&gt;&#xa;&lt;div&gt;&lt;b style=&quot;color:#0f172a;&quot;&gt;Acquisition:&lt;/b&gt; Multi-coil RF receiver coils &amp;rarr; Raw k-space &lt;b&gt;Y&lt;/b&gt; &amp;isin; &amp;#x2102;&lt;sup&gt;C&amp;times;K&lt;sub&gt;x&lt;/sub&gt;&amp;times;K&lt;sub&gt;y&lt;/sub&gt;&lt;/sup&gt;&lt;/div&gt;&#xa;&lt;div style=&quot;margin-top:4px;&quot;&gt;&lt;b style=&quot;color:#0f172a;&quot;&gt;Lesion Prior:&lt;/b&gt; Gabor CHO Template &lt;b&gt;w&lt;/b&gt;&lt;sub&gt;CHO&lt;/sub&gt; &amp;rarr; Task Spectrum &lt;span style=&quot;color:#0284c7;font-weight:bold;&quot;&gt;W(k&lt;sub&gt;x&lt;/sub&gt;, k&lt;sub&gt;y&lt;/sub&gt;) = |&amp;#x2131;{w&lt;sub&gt;CHO&lt;/sub&gt;}|&lt;sup&gt;2&lt;/sup&gt;&lt;/span&gt;&lt;/div&gt;&#xa;&lt;/div&gt;" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=top;whiteSpace=wrap;overflow=visible;fontFamily=Helvetica;" vertex="1" parent="l1_box">
          <mxGeometry x="8" y="28" width="434" height="60" as="geometry" />
        </mxCell>
        <mxCell id="l1_badge" value="&lt;b&gt;Clinical Safety Target:&lt;/b&gt; Pre-Transmission Detectability d'&lt;sub&gt;CHO&lt;/sub&gt; &amp;ge; 1.5 (Safe Margin)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f0f9ff;strokeColor=#38bdf8;strokeWidth=1;fontColor=#0284c7;fontSize=9.5;fontFamily=Helvetica;arcSize=3;align=center;" vertex="1" parent="l1_box">
          <mxGeometry x="12" y="105" width="426" height="32" as="geometry" />
        </mxCell>

        <!-- Downward arrow Layer 1 -> Layer 2 -->
        <mxCell id="arr_tx_internal" value="&lt;span style=&quot;background-color:#f8fafc;padding:1px 5px;font-size:9px;&quot;&gt;Task Prior W(k&lt;sub&gt;x&lt;/sub&gt;, k&lt;sub&gt;y&lt;/sub&gt;)&lt;/span&gt;" style="edgeStyle=straight;html=1;strokeColor=#0284c7;strokeWidth=1.5;fontColor=#0284c7;fontSize=9;fontFamily=Helvetica;fontStyle=1;align=center;verticalAlign=middle;endArrow=block;endFill=1;endSize=4;" edge="1" parent="col_tx" source="l1_box" target="l2_box">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Layer 2 Box -->
        <mxCell id="l2_box" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#bbf7d0;strokeWidth=1.2;arcSize=3;" vertex="1" parent="col_tx">
          <mxGeometry x="15" y="215" width="450" height="155" as="geometry" />
        </mxCell>
        <mxCell id="l2_hdr" value="&lt;b&gt;LAYER 2: DIAGNOSTIC COMPRESSION (DARDO)&lt;/b&gt; &amp;mdash; &lt;span style=&quot;font-size:9px;font-weight:normal;color:#15803d;&quot;&gt;Separates stroke vs bulk data&lt;/span&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#dcfce7;strokeColor=#86efac;strokeWidth=1;fontColor=#15803d;fontSize=10;fontFamily=Helvetica;arcSize=3;align=center;" vertex="1" parent="l2_box">
          <mxGeometry x="0" y="0" width="450" height="24" as="geometry" />
        </mxCell>
        <mxCell id="l2_txt" value="&lt;div style=&quot;padding: 4px 6px; font-family: Helvetica; font-size: 10px; line-height: 1.5; color: #334155;&quot;&gt;&#xa;&lt;div&gt;&lt;b style=&quot;color:#0f172a;&quot;&gt;Diagnostic Gradient:&lt;/b&gt; &lt;span style=&quot;color:#15803d;font-weight:bold;&quot;&gt;&amp;gamma;&lt;sub&gt;k&lt;/sub&gt; = &amp;sum;&lt;sub&gt;y&lt;/sub&gt; W(k, y) ||&amp;#x2131;S&lt;sub&gt;k&lt;/sub&gt;||&lt;sub&gt;2&lt;/sub&gt;&lt;/span&gt; &lt;i style=&quot;color:#64748b;&quot;&gt;(Ranks stroke trajectories)&lt;/i&gt;&lt;/div&gt;&#xa;&lt;div style=&quot;margin-top:4px;&quot;&gt;&lt;b style=&quot;color:#0f172a;&quot;&gt;Greedy Slicing Split:&lt;/b&gt; Sort in &amp;lt; 2 ms &amp;rArr; &lt;b style=&quot;color:#ea580c;&quot;&gt;K&lt;sub&gt;diag&lt;/sub&gt;&lt;/b&gt; (Stroke Bands) vs. &lt;b style=&quot;color:#64748b;&quot;&gt;K&lt;sub&gt;bulk&lt;/sub&gt;&lt;/b&gt; (Bulk Anatomy)&lt;/div&gt;&#xa;&lt;/div&gt;" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=top;whiteSpace=wrap;overflow=visible;fontFamily=Helvetica;" vertex="1" parent="l2_box">
          <mxGeometry x="8" y="28" width="434" height="60" as="geometry" />
        </mxCell>
        <mxCell id="l2_badge" value="&lt;b&gt;Verification Token:&lt;/b&gt; 128B Semantic Pathology Token &lt;b&gt;&amp;theta;&lt;/b&gt; embedded in Header" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f0fdf4;strokeColor=#4ade80;strokeWidth=1;fontColor=#166534;fontSize=9.5;fontFamily=Helvetica;arcSize=3;align=center;" vertex="1" parent="l2_box">
          <mxGeometry x="12" y="105" width="426" height="32" as="geometry" />
        </mxCell>


        <!-- ========================================== -->
        <!-- COLUMN 2: 5G RAN NETWORK                   -->
        <!-- ========================================== -->
        <mxCell id="col_ran" value="&lt;b&gt;5G / B5G CELLULAR RADIO ACCESS NETWORK&lt;/b&gt;" style="swimlane;whiteSpace=wrap;html=1;startSize=28;fillColor=#0f172a;strokeColor=#cbd5e1;strokeWidth=1.5;fontColor=#ffffff;fontFamily=Helvetica;fontSize=10.5;align=center;swimlaneFillColor=#f8fafc;rounded=1;arcSize=3;" vertex="1" parent="1">
          <mxGeometry x="610" y="52" width="480" height="385" as="geometry" />
        </mxCell>

        <!-- URLLC Slice Box -->
        <mxCell id="urllc_box" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#fed7aa;strokeWidth=1.2;arcSize=3;" vertex="1" parent="col_ran">
          <mxGeometry x="15" y="38" width="450" height="152" as="geometry" />
        </mxCell>
        <mxCell id="urllc_hdr" value="&lt;b&gt;LAYER 3: 5G URLLC SLICE (MISSION-CRITICAL)&lt;/b&gt; &amp;mdash; &lt;span style=&quot;font-size:9px;font-weight:normal;color:#c2410c;&quot;&gt;Guaranteed stroke delivery&lt;/span&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffedd5;strokeColor=#fdba74;strokeWidth=1;fontColor=#c2410c;fontSize=10;fontFamily=Helvetica;arcSize=3;align=center;" vertex="1" parent="urllc_box">
          <mxGeometry x="0" y="0" width="450" height="24" as="geometry" />
        </mxCell>
        <mxCell id="urllc_txt" value="&lt;div style=&quot;padding: 4px 6px; font-family: Helvetica; font-size: 10px; line-height: 1.5; color: #334155;&quot;&gt;&#xa;&lt;div&gt;&lt;b style=&quot;color:#0f172a;&quot;&gt;Critical Payload:&lt;/b&gt; &lt;b style=&quot;color:#ea580c;&quot;&gt;K&lt;sub&gt;diag&lt;/sub&gt; = {k | &amp;gamma;&lt;sub&gt;k&lt;/sub&gt; &amp;ge; &amp;tau;}&lt;/b&gt; + &lt;b style=&quot;color:#15803d;&quot;&gt;Token &amp;theta;&lt;/b&gt; &lt;i style=&quot;color:#64748b;&quot;&gt;(Stroke-bearing frequencies)&lt;/i&gt;&lt;/div&gt;&#xa;&lt;div style=&quot;margin-top:4px;&quot;&gt;&lt;b style=&quot;color:#0f172a;&quot;&gt;3GPP Service:&lt;/b&gt; QCI 1 / 65 (Dedicated Bandwidth Part, Prioritized Grants, BLER &amp;lt; 10&lt;sup&gt;-5&lt;/sup&gt;)&lt;/div&gt;&#xa;&lt;/div&gt;" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=top;whiteSpace=wrap;overflow=visible;fontFamily=Helvetica;" vertex="1" parent="urllc_box">
          <mxGeometry x="8" y="28" width="434" height="60" as="geometry" />
        </mxCell>
        <mxCell id="urllc_badge" value="&lt;b&gt;Channel Guarantee:&lt;/b&gt; High Fading Margin (Zero Burst Dropout Under Handover)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fff7ed;strokeColor=#fb923c;strokeWidth=1;fontColor=#c2410c;fontSize=9.5;fontFamily=Helvetica;arcSize=3;align=center;" vertex="1" parent="urllc_box">
          <mxGeometry x="12" y="105" width="426" height="32" as="geometry" />
        </mxCell>

        <!-- eMBB Slice Box -->
        <mxCell id="embb_box" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#cbd5e1;strokeWidth=1.2;arcSize=3;" vertex="1" parent="col_ran">
          <mxGeometry x="15" y="215" width="450" height="155" as="geometry" />
        </mxCell>
        <mxCell id="embb_hdr" value="&lt;b&gt;LAYER 3: 5G eMBB SLICE (BULK ANATOMY)&lt;/b&gt; &amp;mdash; &lt;span style=&quot;font-size:9px;font-weight:normal;color:#475569;&quot;&gt;Gross skull &amp;amp; brain context&lt;/span&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f1f5f9;strokeColor=#cbd5e1;strokeWidth=1;fontColor=#334155;fontSize=10;fontFamily=Helvetica;arcSize=3;align=center;" vertex="1" parent="embb_box">
          <mxGeometry x="0" y="0" width="450" height="24" as="geometry" />
        </mxCell>
        <mxCell id="embb_txt" value="&lt;div style=&quot;padding: 4px 6px; font-family: Helvetica; font-size: 10px; line-height: 1.5; color: #334155;&quot;&gt;&#xa;&lt;div&gt;&lt;b style=&quot;color:#0f172a;&quot;&gt;Bulk Payload:&lt;/b&gt; &lt;b style=&quot;color:#475569;&quot;&gt;K&lt;sub&gt;bulk&lt;/sub&gt; = {k | &amp;gamma;&lt;sub&gt;k&lt;/sub&gt; &amp;lt; &amp;tau;}&lt;/b&gt; &lt;i style=&quot;color:#64748b;&quot;&gt;(Structural skull &amp;amp; brain context)&lt;/i&gt;&lt;/div&gt;&#xa;&lt;div style=&quot;margin-top:4px;&quot;&gt;&lt;b style=&quot;color:#0f172a;&quot;&gt;Transmission Policy:&lt;/b&gt; Standard dynamic DASH streaming &lt;i style=&quot;color:#64748b;&quot;&gt;(Loss-tolerant)&lt;/i&gt;&lt;/div&gt;&#xa;&lt;/div&gt;" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=top;whiteSpace=wrap;overflow=visible;fontFamily=Helvetica;" vertex="1" parent="embb_box">
          <mxGeometry x="8" y="28" width="434" height="60" as="geometry" />
        </mxCell>
        <mxCell id="embb_badge" value="&lt;b&gt;Throughput Profile:&lt;/b&gt; Best-Effort Bandwidth (Tolerates Channel Fluctuations)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f8fafc;strokeColor=#94a3b8;strokeWidth=1;fontColor=#475569;fontSize=9.5;fontFamily=Helvetica;arcSize=3;align=center;" vertex="1" parent="embb_box">
          <mxGeometry x="12" y="105" width="426" height="32" as="geometry" />
        </mxCell>


        <!-- ========================================== -->
        <!-- COLUMN 3: RECEIVER (EDGE SERVER)           -->
        <!-- ========================================== -->
        <mxCell id="col_rx" value="&lt;b&gt;RECEIVER: HOSPITAL EDGE SERVER&lt;/b&gt;" style="swimlane;whiteSpace=wrap;html=1;startSize=28;fillColor=#0f172a;strokeColor=#cbd5e1;strokeWidth=1.5;fontColor=#ffffff;fontFamily=Helvetica;fontSize=10.5;align=center;swimlaneFillColor=#f8fafc;rounded=1;arcSize=3;" vertex="1" parent="1">
          <mxGeometry x="1190" y="52" width="480" height="385" as="geometry" />
        </mxCell>

        <!-- Recon Engine Box -->
        <mxCell id="rx_recon_box" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#ddd6fe;strokeWidth=1.2;arcSize=3;" vertex="1" parent="col_rx">
          <mxGeometry x="15" y="38" width="450" height="152" as="geometry" />
        </mxCell>
        <mxCell id="rx_recon_hdr" value="&lt;b&gt;EDGE AI RECONSTRUCTION (VarNet)&lt;/b&gt; &amp;mdash; &lt;span style=&quot;font-size:9px;font-weight:normal;color:#6d28d9;&quot;&gt;Deep physics reconstruction&lt;/span&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ede9fe;strokeColor=#c4b5fd;strokeWidth=1;fontColor=#6d28d9;fontSize=10;fontFamily=Helvetica;arcSize=3;align=center;" vertex="1" parent="rx_recon_box">
          <mxGeometry x="0" y="0" width="450" height="24" as="geometry" />
        </mxCell>
        <mxCell id="rx_recon_txt" value="&lt;div style=&quot;padding: 4px 6px; font-family: Helvetica; font-size: 10px; line-height: 1.5; color: #334155;&quot;&gt;&#xa;&lt;div&gt;&lt;b style=&quot;color:#0f172a;&quot;&gt;Stream Fusion:&lt;/b&gt; Fuses &lt;b&gt;Y&lt;/b&gt;&lt;sub&gt;URLLC&lt;/sub&gt; &amp;cup; &lt;b&gt;Y&lt;/b&gt;&lt;sub&gt;eMBB&lt;/sub&gt; &lt;i style=&quot;color:#64748b;&quot;&gt;(Early stroke lines + bulk anatomy)&lt;/i&gt;&lt;/div&gt;&#xa;&lt;div style=&quot;margin-top:4px;&quot;&gt;&lt;b style=&quot;color:#0f172a;&quot;&gt;Deep Physics Recon:&lt;/b&gt; &lt;span style=&quot;color:#6d28d9;font-weight:bold;&quot;&gt;X&amp;#770; = &amp;#x211b;&lt;sub&gt;&amp;theta;&lt;/sub&gt;(Y)&lt;/span&gt; completed in 1.8 s on Hospital Edge GPU&lt;/div&gt;&#xa;&lt;/div&gt;" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=top;whiteSpace=wrap;overflow=visible;fontFamily=Helvetica;" vertex="1" parent="rx_recon_box">
          <mxGeometry x="8" y="28" width="434" height="60" as="geometry" />
        </mxCell>
        <mxCell id="rx_recon_badge" value="&lt;b&gt;Physical Residual:&lt;/b&gt; PASSED (Null-Space Blind &amp;mdash; cannot detect pathology erasure)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f3ff;strokeColor=#c4b5fd;strokeWidth=1;fontColor=#7c3aed;fontSize=9.5;fontFamily=Helvetica;arcSize=3;align=center;" vertex="1" parent="rx_recon_box">
          <mxGeometry x="12" y="105" width="426" height="32" as="geometry" />
        </mxCell>

        <!-- Downward arrow Recon -> Layer 4 -->
        <mxCell id="arr_rx_internal" value="&lt;span style=&quot;background-color:#f8fafc;padding:1px 5px;font-size:9px;&quot;&gt;Reconstructed X&amp;#770; + Token &amp;theta;&lt;/span&gt;" style="edgeStyle=straight;html=1;strokeColor=#6d28d9;strokeWidth=1.5;fontColor=#6d28d9;fontSize=9;fontFamily=Helvetica;fontStyle=1;align=center;verticalAlign=middle;endArrow=block;endFill=1;endSize=4;" edge="1" parent="col_rx" source="rx_recon_box" target="layer4_box">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Layer 4 Audit Box -->
        <mxCell id="layer4_box" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#fecdd3;strokeWidth=1.2;arcSize=3;" vertex="1" parent="col_rx">
          <mxGeometry x="15" y="215" width="450" height="155" as="geometry" />
        </mxCell>
        <mxCell id="layer4_hdr" value="&lt;b&gt;LAYER 4: SEMANTIC AUDIT &amp;amp; DECISION GATE&lt;/b&gt; &amp;mdash; &lt;span style=&quot;font-size:9px;font-weight:normal;color:#be123c;&quot;&gt;Instant clinical verification&lt;/span&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffe4e6;strokeColor=#fecdd3;strokeWidth=1;fontColor=#be123c;fontSize=10;fontFamily=Helvetica;arcSize=3;align=center;" vertex="1" parent="layer4_box">
          <mxGeometry x="0" y="0" width="450" height="24" as="geometry" />
        </mxCell>
        <mxCell id="layer4_txt" value="&lt;div style=&quot;padding: 2px 4px; font-family: Helvetica;&quot;&gt;&lt;b style=&quot;color:#0f172a;font-size:10px;&quot;&gt;Task Verifier:&lt;/b&gt; &lt;span style=&quot;color:#be123c;font-weight:bold;font-size:10px;&quot;&gt;CHO Score z&lt;sub&gt;recon&lt;/sub&gt;&lt;/span&gt; &lt;span style=&quot;color:#334155;font-size:9.5px;&quot;&gt;(Channelised Hotelling Observer evaluated in &amp;lt; 12 ms on GPU)&lt;/span&gt;&lt;/div&gt;" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=top;whiteSpace=wrap;overflow=visible;fontFamily=Helvetica;" vertex="1" parent="layer4_box">
          <mxGeometry x="8" y="26" width="434" height="20" as="geometry" />
        </mxCell>

        <!-- Pass card -->
        <mxCell id="card_pass" value="&lt;b style=&quot;color:#15803d;font-size:10px;&quot;&gt;&amp;#x2714; z &amp;ge; 1.5 (AUDIT PASSED: STROKE INTACT)&lt;/b&gt;&lt;br&gt;&lt;span style=&quot;color:#166534;font-size:9px;&quot;&gt;Certified Clinically Safe &amp;rarr; Released to PACS &amp;amp; Stroke Neurologist&lt;/span&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f0fdf4;strokeColor=#86efac;strokeWidth=1;arcSize=3;align=left;spacingLeft=12;" vertex="1" parent="layer4_box">
          <mxGeometry x="12" y="50" width="426" height="42" as="geometry" />
        </mxCell>

        <!-- Fail card -->
        <mxCell id="card_fail" value="&lt;b style=&quot;color:#b91c1c;font-size:10px;&quot;&gt;&amp;#x2718; z &amp;lt; 1.5 (AUDIT FAILED: STROKE ERASED!)&lt;/b&gt;&lt;br&gt;&lt;b style=&quot;color:#dc2626;font-size:9px;&quot;&gt;Silent Erasure Alert &amp;rArr; Trigger Targeted S-NACK Retransmission&lt;/b&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fef2f2;strokeColor=#fca5a5;strokeWidth=1.2;arcSize=3;align=left;spacingLeft=12;" vertex="1" parent="layer4_box">
          <mxGeometry x="12" y="98" width="426" height="46" as="geometry" />
        </mxCell>


        <!-- ========================================== -->
        <!-- FORWARD FLOW ARROWS (INTER-SWIMLANE)       -->
        <!-- ========================================== -->
        <!-- URLLC Forward: Tx -> RAN -->
        <mxCell id="arr_urllc_1" value="&lt;b style=&quot;color:#c2410c;font-size:9.5px;&quot;&gt;URLLC Flow&lt;/b&gt;&lt;br&gt;&lt;span style=&quot;color:#c2410c;font-size:8.5px;&quot;&gt;K&lt;sub&gt;diag&lt;/sub&gt; + &amp;theta; (Stroke Data)&lt;/span&gt;" style="edgeStyle=straight;html=1;strokeColor=#ea580c;strokeWidth=2.4;align=center;verticalAlign=bottom;labelBackgroundColor=#ffffff;endArrow=block;endFill=1;endSize=5;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="510" y="165" as="sourcePoint" />
            <mxPoint x="610" y="165" as="targetPoint" />
          </mxGeometry>
        </mxCell>

        <!-- URLLC Forward: RAN -> Rx -->
        <mxCell id="arr_urllc_2" value="&lt;b style=&quot;color:#c2410c;font-size:9.5px;&quot;&gt;URLLC Flow&lt;/b&gt;&lt;br&gt;&lt;span style=&quot;color:#c2410c;font-size:8.5px;&quot;&gt;K&lt;sub&gt;diag&lt;/sub&gt; + &amp;theta; (Stroke Data)&lt;/span&gt;" style="edgeStyle=straight;html=1;strokeColor=#ea580c;strokeWidth=2.4;align=center;verticalAlign=bottom;labelBackgroundColor=#ffffff;endArrow=block;endFill=1;endSize=5;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="1090" y="165" as="sourcePoint" />
            <mxPoint x="1190" y="165" as="targetPoint" />
          </mxGeometry>
        </mxCell>

        <!-- eMBB Forward: Tx -> RAN -->
        <mxCell id="arr_embb_1" value="&lt;b style=&quot;color:#475569;font-size:9.5px;&quot;&gt;eMBB Flow&lt;/b&gt;&lt;br&gt;&lt;span style=&quot;color:#475569;font-size:8.5px;&quot;&gt;K&lt;sub&gt;bulk&lt;/sub&gt; (Gross Anatomy)&lt;/span&gt;" style="edgeStyle=straight;html=1;strokeColor=#64748b;strokeWidth=2.4;align=center;verticalAlign=bottom;labelBackgroundColor=#ffffff;endArrow=block;endFill=1;endSize=5;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="510" y="345" as="sourcePoint" />
            <mxPoint x="610" y="345" as="targetPoint" />
          </mxGeometry>
        </mxCell>

        <!-- eMBB Forward: RAN -> Rx -->
        <mxCell id="arr_embb_2" value="&lt;b style=&quot;color:#475569;font-size:9.5px;&quot;&gt;eMBB Flow&lt;/b&gt;&lt;br&gt;&lt;span style=&quot;color:#475569;font-size:8.5px;&quot;&gt;K&lt;sub&gt;bulk&lt;/sub&gt; (Gross Anatomy)&lt;/span&gt;" style="edgeStyle=straight;html=1;strokeColor=#64748b;strokeWidth=2.4;align=center;verticalAlign=bottom;labelBackgroundColor=#ffffff;endArrow=block;endFill=1;endSize=5;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="1090" y="345" as="sourcePoint" />
            <mxPoint x="1190" y="345" as="targetPoint" />
          </mxGeometry>
        </mxCell>


        <!-- ========================================== -->
        <!-- S-NACK RETRANSMISSION PROTOCOL (BOTTOM)    -->
        <!-- ========================================== -->
        <!-- Central S-NACK Protocol Banner -->
        <mxCell id="snack_banner" value="&lt;b style=&quot;color:#991b1b;font-size:10.5px;&quot;&gt;CLOSED-LOOP S-NACK RETRANSMISSION PROTOCOL&lt;/b&gt;&lt;br&gt;&lt;span style=&quot;color:#7f1d1d;font-size:9.5px;&quot;&gt;Smart Recovery: Requests only missing high-&amp;gamma;&lt;sub&gt;k&lt;/sub&gt; bands (&amp;Delta;k &amp;approx; 1.2 MB, Round-Trip Latency &amp;Delta;t &amp;approx; 15 ms)&lt;/span&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fef2f2;strokeColor=#fca5a5;strokeWidth=1.4;arcSize=3;align=center;verticalAlign=middle;" vertex="1" parent="1">
          <mxGeometry x="450" y="455" width="800" height="46" as="geometry" />
        </mxCell>

        <!-- Return Arrow 1: Downward from card_fail to S-NACK banner -->
        <mxCell id="arr_snack_down" value="&lt;b style=&quot;color:#b91c1c;font-size:9px;&quot;&gt;Audit Failed&lt;br&gt;(Stroke Erased)&lt;/b&gt;" style="edgeStyle=orthogonalEdgeStyle;rounded=1;arcSize=8;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#dc2626;strokeWidth=2.2;fontColor=#b91c1c;fontSize=9;fontFamily=Helvetica;align=left;spacingLeft=8;endArrow=block;endFill=1;endSize=5;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="1415" y="415" as="sourcePoint" />
            <mxPoint x="1250" y="478" as="targetPoint" />
            <Array as="points">
              <mxPoint x="1415" y="478" />
            </Array>
          </mxGeometry>
        </mxCell>

        <!-- Return Arrow 2: Left and UP from S-NACK banner to Layer 2 DARDO -->
        <mxCell id="arr_snack_up" value="&lt;b style=&quot;color:#b91c1c;font-size:9px;&quot;&gt;Targeted S-NACK&lt;br&gt;(Resend Missing &amp;Delta;k)&lt;/b&gt;" style="edgeStyle=orthogonalEdgeStyle;rounded=1;arcSize=8;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#dc2626;strokeWidth=2.2;fontColor=#b91c1c;fontSize=9;fontFamily=Helvetica;align=right;spacingRight=8;endArrow=block;endFill=1;endSize=5;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="450" y="478" as="sourcePoint" />
            <mxPoint x="270" y="425" as="targetPoint" />
            <Array as="points">
              <mxPoint x="270" y="478" />
            </Array>
          </mxGeometry>
        </mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>"""
    return xml

def main():
    xml = build_wide_drawio_xml()
    fig_dir = os.path.abspath('figures')
    drawio_file = os.path.join(fig_dir, 'fig4_architecture_diagram_io.drawio')
    with open(drawio_file, 'w', encoding='utf-8') as f:
        f.write(xml)
    print("Saved wide drawio file:", drawio_file)

    viewer_js = os.path.abspath('scratch/viewer-static.min.js').replace('\\', '/')
    html = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <script type="text/javascript" src="{viewer_js}"></script>
  <style>
    * {{ box-sizing: border-box; }}
    html, body {{
      margin: 0;
      padding: 0;
      width: 1720px;
      height: 535px;
      overflow: hidden;
      background: #ffffff;
    }}
    .mxgraph {{
      width: 1720px;
      height: 535px;
      overflow: visible;
    }}
  </style>
</head>
<body>
  <div id="container"></div>
  <script>
    const xml = {json.dumps(xml)};
    const div = document.createElement('div');
    div.className = 'mxgraph';
    div.setAttribute('data-mxgraph', JSON.stringify({{
      highlight: '#0000ff',
      nav: false,
      resize: true,
      toolbar: '',
      xml: xml
    }}));
    document.getElementById('container').appendChild(div);
    GraphViewer.processElements();
  </script>
</body>
</html>"""

    html_file = os.path.abspath('scratch/render_fig4_wide.html')
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html)
    
    png_preview = os.path.join(fig_dir, 'fig4_architecture_diagram_io_preview.png')
    png_final = os.path.join(fig_dir, 'fig4_architecture.png')
    pdf_out = os.path.join(fig_dir, 'fig4_architecture.pdf')

    edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    file_url = 'file:///' + html_file.replace('\\', '/')

    cmd = [
        edge_path,
        '--headless',
        '--disable-gpu',
        '--force-device-scale-factor=2',
        '--virtual-time-budget=3000',
        '--window-size=1720,535',
        f'--screenshot={png_preview}',
        file_url
    ]
    subprocess.run(cmd, check=True)
    print("Rendered PNG preview:", png_preview)
    print("Preview size:", os.path.getsize(png_preview), "bytes")

    # Copy to fig4_architecture.png
    with open(png_preview, 'rb') as f_in, open(png_final, 'wb') as f_out:
        f_out.write(f_in.read())
    print("Updated fig4_architecture.png")

    # Convert to PDF
    doc = fitz.open()
    img_doc = fitz.open(png_final)
    rect = img_doc[0].rect
    pdf_rect = fitz.Rect(0, 0, rect.width / 2.0, rect.height / 2.0)
    page = doc.new_page(width=pdf_rect.width, height=pdf_rect.height)
    page.insert_image(pdf_rect, filename=png_final)
    doc.save(pdf_out)
    doc.close()
    print("Updated fig4_architecture.pdf")

if __name__ == '__main__':
    main()
