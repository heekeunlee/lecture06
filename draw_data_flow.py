import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Set up clean professional font
plt.rcParams['font.sans-serif'] = ['AppleGothic', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

# Create figure
fig, ax = plt.subplots(figsize=(11, 7.5), dpi=150)
ax.set_xlim(0, 11)
ax.set_ylim(0, 8)
ax.axis('off')

# Background color
fig.patch.set_facecolor('#ffffff')

# 1. Title
ax.text(5.5, 7.4, "OLED 증착 설비 실시간 센서 데이터 수집 체계 (1분 주기 Polling)", 
        color='#111827', fontsize=15, fontweight='bold', ha='center')

# 2. Sensors Layer (왼쪽)
ax.text(1.2, 5.8, "현장 물리 센서", color='#374151', fontsize=11, fontweight='bold', ha='center')

sensors = [
    {"name": "온도 센서 (Temp)", "val": "382.4 °C", "color": "#ef4444", "y": 4.8},
    {"name": "진공도 센서 (Press)", "val": "1.02e-6 Torr", "color": "#0071e3", "y": 3.7},
    {"name": "QCM 속도 센서 (Rate)", "val": "1.24 Å/s", "color": "#f59e0b", "y": 2.6},
    {"name": "냉각수 센서 (Flow)", "val": "12.4 L/min", "color": "#10b981", "y": 1.5}
]

for s in sensors:
    # Sensor Card
    card = patches.FancyBboxPatch((0.2, s["y"] - 0.4), 2.0, 0.8, boxstyle="round,pad=0.08",
                                  facecolor='#ffffff', edgecolor=s["color"], linewidth=2)
    ax.add_patch(card)
    ax.text(1.2, s["y"] + 0.15, s["name"], color='#1f2937', fontsize=9.5, fontweight='bold', ha='center')
    ax.text(1.2, s["y"] - 0.2, s["val"], color=s["color"], fontsize=10, fontweight='bold', ha='center')

# 3. PLC / Edge Gateway Box (중앙 왼쪽)
gateway_box = patches.FancyBboxPatch((3.0, 2.5), 1.8, 2.2, boxstyle="round,pad=0.1",
                                     facecolor='#f3f4f6', edgecolor='#4b5563', linewidth=2)
ax.add_patch(gateway_box)
ax.text(3.9, 4.3, "PLC / 현장 Gateway", color='#1f2937', fontsize=11, fontweight='bold', ha='center')
ax.text(3.9, 3.8, "(시그널 변환)", color='#4b5563', fontsize=9.5, ha='center')
ax.text(3.9, 3.2, "Analog ➡ Digital", color='#0071e3', fontsize=10, fontweight='bold', ha='center')
ax.text(3.9, 2.7, "Modbus / TCP 프로토콜", color='#4b5563', fontsize=8.5, ha='center')

# Draw arrows from sensors to Gateway
for s in sensors:
    ax.annotate('', xy=(3.0, 3.6), xytext=(2.3, s["y"]),
                arrowprops=dict(arrowstyle="->", color="#9ca3af", lw=1.5, connectionstyle="arc3,rad=0.1"))

# 4. SCADA & MES Layer (중앙 오른쪽)
# SCADA Box
scada_box = patches.FancyBboxPatch((5.6, 4.1), 2.2, 1.3, boxstyle="round,pad=0.1",
                                   facecolor='#eff6ff', edgecolor='#2563eb', linewidth=2)
ax.add_patch(scada_box)
ax.text(6.7, 5.0, "SCADA 감시 시스템", color='#1e3a8a', fontsize=11, fontweight='bold', ha='center')
ax.text(6.7, 4.5, "실시간 설비 모니터링\n센서 시각화 및 제어", color='#1e40af', fontsize=9, ha='center')

# MES Box
mes_box = patches.FancyBboxPatch((5.6, 2.0), 2.2, 1.3, boxstyle="round,pad=0.1",
                                 facecolor='#ecfdf5', edgecolor='#059669', linewidth=2)
ax.add_patch(mes_box)
ax.text(6.7, 2.9, "MES 제조 관리 시스템", color='#064e3b', fontsize=11, fontweight='bold', ha='center')
ax.text(6.7, 2.4, "종합 생산 관리\n공정 이력 / 불량 검증", color='#065f46', fontsize=9, ha='center')

# Draw arrows from Gateway to SCADA/MES
ax.annotate('', xy=(5.5, 4.8), xytext=(4.9, 3.8),
            arrowprops=dict(arrowstyle="->", color="#2563eb", lw=2, connectionstyle="arc3,rad=-0.1"))
ax.annotate('', xy=(5.5, 2.7), xytext=(4.9, 3.4),
            arrowprops=dict(arrowstyle="->", color="#059669", lw=2, connectionstyle="arc3,rad=0.1"))

# 5. Time Database (오른쪽 끝)
db_box = patches.FancyBboxPatch((8.6, 2.6), 2.1, 2.0, boxstyle="round,pad=0.1",
                                 facecolor='#fffbeb', edgecolor='#d97706', linewidth=2)
ax.add_patch(db_box)

# DB Cylinders representation
db_cyl1 = patches.Ellipse((9.65, 4.1), 1.2, 0.3, facecolor='#fef3c7', edgecolor='#d97706', linewidth=1.5, zorder=2)
db_cyl2 = patches.Rectangle((9.05, 3.4), 1.2, 0.7, facecolor='#fef3c7', edgecolor='#d97706', linewidth=1.5, zorder=1)
db_cyl3 = patches.Ellipse((9.65, 3.4), 1.2, 0.3, facecolor='#fde047', edgecolor='#d97706', linewidth=1.5, zorder=2)
ax.add_patch(db_cyl1)
ax.add_patch(db_cyl2)
ax.add_patch(db_cyl3)

ax.text(9.65, 2.9, "시계열 DB (Historian)", color='#78350f', fontsize=10.5, fontweight='bold', ha='center')
ax.text(9.65, 2.1, "1분 간격 Sensor Log 저장", color='#b45309', fontsize=9, fontweight='bold', ha='center')

# Draw arrows from SCADA/MES to DB
ax.annotate('', xy=(8.5, 3.8), xytext=(7.9, 4.6),
            arrowprops=dict(arrowstyle="->", color="#b45309", lw=2, connectionstyle="arc3,rad=0.1"))
ax.annotate('', xy=(8.5, 3.4), xytext=(7.9, 2.8),
            arrowprops=dict(arrowstyle="->", color="#b45309", lw=2, connectionstyle="arc3,rad=-0.1"))

# 6. Polling clock highlight
clock_circle = patches.Circle((4.9, 5.7), 0.45, facecolor='#fee2e2', edgecolor='#ef4444', lw=2)
ax.add_patch(clock_circle)
ax.plot([4.9, 4.9], [5.7, 6.0], color='#ef4444', lw=2.5) # clock hands
ax.plot([4.9, 5.15], [5.7, 5.7], color='#ef4444', lw=2.5)
ax.text(5.5, 5.7, "정밀 1분 주기 수집\n(1-Minute Polling)", color='#b91c1c', fontsize=9.5, fontweight='bold', va='center')

# Description Text
desc_text = "■ 1분 데이터 수집 원리:\n공장 내 물리 센서들의 디지털화된 시그널을 SCADA 및 MES 서버가 매 1분 정각 주기마다\n자동 수집(Polling)하여 유실 없이 장기 시계열 DB에 안전하게 기록합니다."
ax.text(5.5, 0.8, desc_text, color='#374151', fontsize=11, ha='center', va='center', fontweight='bold',
        bbox=dict(boxstyle="round,pad=0.5", fc="#f9fafb", ec="#e5e7eb", lw=1.5))

plt.tight_layout()
plt.savefig('data_collection_flow.png', bbox_inches='tight')
plt.close()
print("Data collection flow diagram generated successfully with Korean labels!")
