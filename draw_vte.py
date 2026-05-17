import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Set up clean professional font
plt.rcParams['font.sans-serif'] = ['AppleGothic', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

# Create figure
fig, ax = plt.subplots(figsize=(10, 8.5), dpi=150)
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Background color
fig.patch.set_facecolor('#ffffff')

# 1. Vacuum Chamber (진공 챔버 외벽)
chamber = patches.FancyBboxPatch((1.5, 1.5), 7.0, 7.0, 
                                 boxstyle="round,pad=0.2", 
                                 linewidth=4, edgecolor='#495057', facecolor='#f8f9fa')
ax.add_patch(chamber)

# Chamber inner grid/glow
inner_chamber = patches.FancyBboxPatch((1.7, 1.7), 6.6, 6.6, 
                                       boxstyle="round,pad=0.2", 
                                       linewidth=1, edgecolor='#dee2e6', facecolor='#f1f3f5')
ax.add_patch(inner_chamber)

# Chamber Label
ax.text(5.0, 8.7, "진공 챔버 내부 (초고진공 상태: 10^-6 Torr)", 
        color='#343a40', fontsize=14, fontweight='bold', ha='center')

# 2. Substrate & Holder (상단 유리 기판 및 홀더)
# Holder
holder = patches.Rectangle((3.0, 7.2), 4.0, 0.4, facecolor='#6c757d', edgecolor='#495057', linewidth=1.5, zorder=3)
ax.add_patch(holder)
ax.text(5.0, 7.8, "기판 홀더 (온도 제어 및 회전 구동)", color='#495057', fontsize=10, ha='center', fontweight='bold')

# Glass Substrate
glass = patches.Rectangle((3.2, 7.0), 3.6, 0.2, facecolor='#e8f7ff', edgecolor='#0071e3', linewidth=2, zorder=4)
ax.add_patch(glass)
ax.text(5.0, 7.45, "유리 기판 (OLED 패널)", color='#0071e3', fontsize=11, ha='center', fontweight='bold')

# Thin Film (Deposited layer under the glass)
thin_film = patches.Rectangle((3.2, 6.9), 3.6, 0.1, facecolor='#22c55e', edgecolor='none', zorder=5)
ax.add_patch(thin_film)
ax.text(5.0, 6.65, "형성되는 유기 발광층 박막 (Thin Film)", color='#166534', fontsize=10.5, ha='center', fontweight='bold')

# 3. Heating Source / Crucible (하단 유기물 가열 도가니)
# Crucible Body
crucible_outer = patches.Polygon([[4.0, 2.2], [6.0, 2.2], [5.7, 3.2], [4.3, 3.2]], 
                                 facecolor='#495057', edgecolor='#212529', linewidth=2, zorder=3)
ax.add_patch(crucible_outer)
crucible_inner = patches.Polygon([[4.15, 2.35], [5.85, 2.35], [5.6, 3.1], [4.4, 3.1]], 
                                 facecolor='#d946ef', alpha=0.3, zorder=4)
ax.add_patch(crucible_inner)

# Organic Material inside crucible (glowing)
ax.text(5.0, 2.5, "유기 재료 분말\n(도가니 내 가열)", color='#c026d3', fontsize=10, ha='center', va='center', fontweight='bold', zorder=5)

# Heating Coil representation (lines around crucible)
for y in np.linspace(2.3, 3.0, 4):
    ax.plot([3.8, 4.1], [y, y], color='#ef4444', linewidth=3, zorder=2)
    ax.plot([5.9, 6.2], [y, y], color='#ef4444', linewidth=3, zorder=2)
ax.text(3.1, 2.65, "히터 가열\n(300°C~400°C)", color='#ef4444', fontsize=10, ha='center', va='center', fontweight='bold')

# Source Power Label
ax.text(5.0, 1.8, "소스 가열 전원 제어 (온도 제어)", color='#212529', fontsize=11, ha='center', fontweight='bold')

# 4. Vapor Stream (기화 유기물 상승 흐름)
# Draw beautiful vapor paths
X = np.linspace(4.3, 5.7, 5)
for x_start in X:
    # Curved path from source to substrate
    path_x = np.linspace(x_start, 3.5 + (x_start - 4.3) * (3.0/1.4), 100)
    path_y = np.linspace(3.2, 6.9, 100)
    # Add some sinusoidal wave to make it look like vapor
    path_x += 0.15 * np.sin(path_y * 2)
    ax.plot(path_x, path_y, color='#a855f7', alpha=0.4, linewidth=2, linestyle='--', zorder=2)

# Vapor arrows
ax.annotate('', xy=(4.0, 5.5), xytext=(4.5, 3.5),
            arrowprops=dict(arrowstyle="->", color="#a855f7", lw=2.5, ls='-', connectionstyle="arc3,rad=-0.15"))
ax.annotate('', xy=(6.0, 5.5), xytext=(5.5, 3.5),
            arrowprops=dict(arrowstyle="->", color="#a855f7", lw=2.5, ls='-', connectionstyle="arc3,rad=0.15"))
ax.annotate('', xy=(5.0, 6.0), xytext=(5.0, 3.5),
            arrowprops=dict(arrowstyle="->", color="#a855f7", lw=2.5, ls='-'))

ax.text(5.0, 4.8, "기화된 유기 분자 흐름\n(Vapor Stream)", color='#7e22ce', fontsize=12, ha='center', va='center', fontweight='bold',
        bbox=dict(boxstyle="round,pad=0.3", fc="#f3e8ff", ec="#c084fc", lw=1, alpha=0.9))

# 5. Vacuum Pump System (진공 배기계)
# Port connection
pump_port = patches.Rectangle((0.8, 4.5), 1.0, 0.6, facecolor='#adb5bd', edgecolor='#495057', linewidth=2)
ax.add_patch(pump_port)

# Pump Box
pump_box = patches.FancyBboxPatch((-0.2, 4.0), 1.2, 1.6, boxstyle="round,pad=0.1", 
                                  facecolor='#e9ecef', edgecolor='#495057', linewidth=2)
ax.add_patch(pump_box)
ax.text(0.4, 4.8, "진공 펌프\n시스템", color='#495057', fontsize=10, ha='center', va='center', fontweight='bold')
ax.text(0.4, 4.2, "배기 작동", color='#0071e3', fontsize=9, ha='center', va='center', fontweight='bold')

# Arrow pointing out
ax.annotate('', xy=(0.2, 4.8), xytext=(1.8, 4.8),
            arrowprops=dict(arrowstyle="<-", color="#0071e3", lw=3))

# 6. QCM Sensor (실시간 두께/속도 감지 센서)
qcm_holder = patches.Rectangle((2.3, 5.8), 0.6, 0.2, facecolor='#f59e0b', edgecolor='#d97706', linewidth=1.5, zorder=3)
ax.add_patch(qcm_holder)
ax.plot([2.6, 2.6], [5.8, 7.5], color='#d97706', linewidth=1.5, zorder=2)
ax.text(2.3, 5.4, "QCM 센서\n(증착 속도 측정)", color='#b45309', fontsize=9.5, ha='center', fontweight='bold')

# 7. Substrate rotation indicator
ax.annotate('', xy=(6.5, 8.2), xytext=(3.5, 8.2),
            arrowprops=dict(arrowstyle="<->", color="#495057", lw=1.5, connectionstyle="arc3,rad=-0.2"))
ax.text(5.0, 8.35, "회전", color='#495057', fontsize=9, ha='center')

# Title & Description Box at the bottom
desc_text = "■ 진공 열 증착(VTE) 원리:\n고진공 상태에서 유기 재료를 가열 기화시켜 상단의 유리 기판에 나노미터(nm) 단위로 정밀 증착하는 방식"
ax.text(5.0, 0.4, desc_text, color='#495057', fontsize=12, ha='center', va='center', fontweight='bold',
        bbox=dict(boxstyle="round,pad=0.5", fc="#f8f9fa", ec="#ced4da", lw=1.5))

plt.tight_layout()
plt.savefig('vte_diagram.png', bbox_inches='tight')
plt.close()
print("VTE diagram generated successfully with Korean labels!")
