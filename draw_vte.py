import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Set up clean professional font
plt.rcParams['font.sans-serif'] = ['AppleGothic', 'Helvetica', 'Arial', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

# Create figure
fig, ax = plt.subplots(figsize=(10.5, 9), dpi=180)
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Background canvas color
fig.patch.set_facecolor('#ffffff')

# ----------------------------------------------------
# 0. Tech Blueprint Grid (Subtle background styling)
# ----------------------------------------------------
for x in np.linspace(0.2, 9.8, 49):
    ax.plot([x, x], [0.2, 9.8], color='#e2e8f0', linewidth=0.4, alpha=0.5, zorder=0)
for y in np.linspace(0.2, 9.8, 49):
    ax.plot([0.2, 9.8], [y, y], color='#e2e8f0', linewidth=0.4, alpha=0.5, zorder=0)

# ----------------------------------------------------
# 1. Vacuum Chamber Outer & Inner Shell
# ----------------------------------------------------
# Outer metallic casing (sleek dark slate border)
chamber_outer = patches.FancyBboxPatch(
    (1.4, 1.4), 7.2, 7.2, 
    boxstyle="round,pad=0.2", 
    linewidth=4.5, edgecolor='#1e293b', facecolor='#f8fafc', zorder=1
)
ax.add_patch(chamber_outer)

# Inner ultra-clean vacuum region (cool soft blue-gray atmosphere glow)
chamber_inner = patches.FancyBboxPatch(
    (1.55, 1.55), 6.9, 6.9, 
    boxstyle="round,pad=0.2", 
    linewidth=1.5, edgecolor='#cbd5e1', facecolor='#f1f5f9', zorder=2
)
ax.add_patch(chamber_inner)

# Tech status indicator lights on upper corners of the chamber
ax.scatter([1.9, 8.1], [8.4, 8.4], color='#10b981', s=60, edgecolors='#34d399', linewidth=1.5, zorder=3)

# Chamber Label (Clean typography)
ax.text(5.0, 8.85, "진공 챔버 내부 (Vacuum Evaporation Chamber)", 
        color='#0f172a', fontsize=14, fontweight='black', ha='center', zorder=3)
ax.text(5.0, 8.56, "초고진공 유지 상태: 1.0 x 10^-6 Torr", 
        color='#64748b', fontsize=10.5, fontweight='bold', ha='center', zorder=3)

# ----------------------------------------------------
# 2. Substrate & Holder (상단 유리 기판 및 회전 구동 홀더)
# ----------------------------------------------------
# Rotating Holder Base (Dark slate metallic slab)
holder = patches.Rectangle(
    (2.8, 7.2), 4.4, 0.35, 
    facecolor='#334155', edgecolor='#1e293b', linewidth=1.5, zorder=4
)
ax.add_patch(holder)
ax.text(5.0, 7.375, "기판 홀더 (온도 제어 및 회전 구동부)", color='#ffffff', fontsize=9.5, ha='center', va='center', fontweight='black', zorder=6)

# Glass Substrate (Premium crystal cyan glass look)
glass_back = patches.Rectangle((3.1, 7.02), 3.8, 0.18, facecolor='#e0f2fe', edgecolor='#0ea5e9', linewidth=1.5, zorder=5)
ax.add_patch(glass_back)
ax.text(5.0, 7.11, "유리 기판 (OLED 패널 구동 기판)", color='#0284c7', fontsize=11, ha='center', fontweight='black', zorder=6)

# Deposited Thin Film (Organic light-emitting layer forming)
thin_film = patches.Rectangle((3.1, 6.90), 3.8, 0.12, facecolor='#10b981', edgecolor='none', zorder=6)
ax.add_patch(thin_film)

# Glow highlight under thin film
thin_film_glow = patches.Rectangle((3.1, 6.85), 3.8, 0.05, facecolor='#a7f3d0', edgecolor='none', alpha=0.6, zorder=5)
ax.add_patch(thin_film_glow)
ax.text(5.0, 6.62, "형성 중인 유기 발광층 박막 (Thin Film Layer)", color='#047857', fontsize=10, ha='center', fontweight='black', zorder=6)

# ----------------------------------------------------
# 3. Heating Source / Crucible (하단 유기물 가열 도가니)
# ----------------------------------------------------
# Crucible Casing (Charcoal metallic trapezoid)
crucible_outer = patches.Polygon(
    [[3.9, 2.1], [6.1, 2.1], [5.7, 3.2], [4.3, 3.2]], 
    facecolor='#1e293b', edgecolor='#0f172a', linewidth=2, zorder=4
)
ax.add_patch(crucible_outer)

# Inner Crucible Liner (High-temp ceramic look)
crucible_inner = patches.Polygon(
    [[4.05, 2.25], [5.95, 2.25], [5.6, 3.1], [4.4, 3.1]], 
    facecolor='#e2e8f0', edgecolor='#94a3b8', linewidth=1, zorder=5
)
ax.add_patch(crucible_inner)

# Heated Organic Material Powder (Dense purple glowing particles)
np.random.seed(42)
for _ in range(70):
    px = np.random.uniform(4.2, 5.8)
    py = np.random.uniform(2.3, 2.9)
    if py > 2.3 and py < 3.0:
        if px > 4.1 + (py-2.3)*0.1 and px < 5.9 - (py-2.3)*0.1:
            ax.scatter([px], [py], color='#c084fc', s=np.random.uniform(15, 45), alpha=0.9, zorder=6)

ax.text(5.0, 2.6, "유기 재료 분말\n(Crucible Powder)", color='#7e22ce', fontsize=10, ha='center', va='center', fontweight='black', zorder=7)

# Heating Coil representation with deep orange-red glow
for y in np.linspace(2.25, 3.05, 5):
    coil_l = patches.Rectangle((3.6, y-0.05), 0.25, 0.1, facecolor='#ef4444', edgecolor='#b91c1c', linewidth=1, zorder=3)
    ax.add_patch(coil_l)
    coil_r = patches.Rectangle((6.15, y-0.05), 0.25, 0.1, facecolor='#ef4444', edgecolor='#b91c1c', linewidth=1, zorder=3)
    ax.add_patch(coil_r)

# Heat emission line/arrows
ax.text(2.9, 2.65, "히터 고온 가열\n(300°C ~ 400°C)", color='#ef4444', fontsize=10.5, ha='center', va='center', fontweight='black')

# Source Power controller label at the bottom
ax.text(5.0, 1.72, "도가니 소스 가열 제어 (Source Power & Temp Control)", color='#1e293b', fontsize=11, ha='center', fontweight='bold', zorder=5)

# ----------------------------------------------------
# 4. Vapor Stream Plume (기화 유기 분자의 확산 흐름)
# ----------------------------------------------------
np.random.seed(100)
for _ in range(250):
    vy = np.random.uniform(3.2, 6.8)
    width = 0.5 + (vy - 3.2) * 0.45
    vx = np.random.normal(5.0, width * 0.4)
    if vx > 5.0 - width and vx < 5.0 + width:
        color_choices = ['#d8b4fe', '#c084fc', '#a855f7', '#e9d5ff']
        vcolor = np.random.choice(color_choices)
        valpha = 0.65 * (1.0 - (vy - 3.2) / 4.5)
        vsize = np.random.uniform(10, 80)
        ax.scatter([vx], [vy], color=vcolor, s=vsize, alpha=valpha, zorder=3)

# Vapor stream guide lines (curved trajectories)
X_start = np.linspace(4.4, 5.6, 5)
for x0 in X_start:
    t = np.linspace(0, 1, 100)
    x_end = 3.3 + (x0 - 4.4) * (3.4 / 1.2)
    path_x = (1-t)**2 * x0 + 2*(1-t)*t * (x0 + (x_end-x0)/2) + t**2 * x_end
    path_y = 3.2 * (1-t) + 6.8 * t
    ax.plot(path_x, path_y, color='#c084fc', alpha=0.35, linewidth=1.5, linestyle=':', zorder=3)

# High-fidelity vector arrows representing molecular flux
ax.annotate('', xy=(3.8, 5.8), xytext=(4.5, 3.4),
            arrowprops=dict(arrowstyle="->", color="#a855f7", lw=2, ls='-', connectionstyle="arc3,rad=-0.15", shrinkA=5, shrinkB=5, zorder=5))
ax.annotate('', xy=(6.2, 5.8), xytext=(5.5, 3.4),
            arrowprops=dict(arrowstyle="->", color="#a855f7", lw=2, ls='-', connectionstyle="arc3,rad=0.15", shrinkA=5, shrinkB=5, zorder=5))
ax.annotate('', xy=(5.0, 6.1), xytext=(5.0, 3.4),
            arrowprops=dict(arrowstyle="->", color="#a855f7", lw=2, ls='-', shrinkA=5, shrinkB=5, zorder=5))

# Tech Badge for Vapor Stream in center
ax.text(5.0, 4.85, "기화된 유기 분자 흐름 (Vapor Stream)", color='#6b21a8', fontsize=12, ha='center', va='center', fontweight='black',
        bbox=dict(boxstyle="round,pad=0.4", fc="#faf5ff", ec="#e9d5ff", lw=1.5, alpha=0.95), zorder=8)

# ----------------------------------------------------
# 5. Vacuum Pump System (진공 배기 밸브 및 펌프)
# ----------------------------------------------------
flange = patches.Rectangle((0.8, 4.4), 0.8, 0.8, facecolor='#64748b', edgecolor='#334155', linewidth=1.5, zorder=3)
ax.add_patch(flange)

pump_body = patches.FancyBboxPatch(
    (-0.25, 3.9), 1.3, 1.8, 
    boxstyle="round,pad=0.1", 
    facecolor='#e2e8f0', edgecolor='#334155', linewidth=2, zorder=4
)
ax.add_patch(pump_body)
ax.text(0.4, 5.0, "진공 펌프\n시스템", color='#1e293b', fontsize=10, ha='center', va='center', fontweight='black', zorder=5)
ax.text(0.4, 4.3, "배기 작동 중", color='#0284c7', fontsize=9.5, ha='center', va='center', fontweight='bold', zorder=5)

ax.annotate('', xy=(-0.1, 4.8), xytext=(1.8, 4.8),
            arrowprops=dict(arrowstyle="<-", color="#0284c7", lw=3.5, zorder=6))

# ----------------------------------------------------
# 6. QCM Sensor (실시간 수정진동자 증착 속도 감지 센서)
# ----------------------------------------------------
ax.plot([2.5, 2.5], [5.7, 7.3], color='#d97706', linewidth=2.5, zorder=3)
qcm_head = patches.Rectangle(
    (2.1, 5.5), 0.8, 0.25, 
    facecolor='#f59e0b', edgecolor='#b45309', linewidth=1.5, zorder=5
)
ax.add_patch(qcm_head)
ax.text(2.5, 5.15, "QCM 센서\n(증착 속도 측정)", color='#b45309', fontsize=9.5, ha='center', fontweight='black', zorder=6)

ax.plot([2.9, 3.1], [5.62, 6.9], color='#f59e0b', alpha=0.8, linewidth=1.5, linestyle='--', zorder=4)

# ----------------------------------------------------
# 7. Substrate rotation indicator
# ----------------------------------------------------
ax.annotate('', xy=(6.4, 7.82), xytext=(3.6, 7.82),
            arrowprops=dict(arrowstyle="<->", color="#475569", lw=1.5, connectionstyle="arc3,rad=-0.2", zorder=5))
ax.text(5.0, 8.08, "기판 균일 회전", color='#475569', fontsize=9.5, fontweight='black', ha='center', zorder=5)

# ----------------------------------------------------
# 8. Title & Explanation Badge at the bottom
# ----------------------------------------------------
desc_title = "■ VTE (Vacuum Thermal Evaporation - 진공 열 증착) 작동 원리"
desc_body = "우주 공간과 유사한 고진공 상태에서 유기 재료를 가열 기화시켜,\n상단의 유리 기판에 분자 단위로 정밀 충돌시켜 나노미터(nm) 단위 박막을 균일하게 증착하는 방식"

explanation_card = patches.FancyBboxPatch(
    (0.9, 0.15), 8.2, 0.9, 
    boxstyle="round,pad=0.1", 
    facecolor='#ffffff', edgecolor='#cbd5e1', linewidth=1.5, zorder=5
)
ax.add_patch(explanation_card)

ax.plot([0.95, 0.95], [0.2, 1.0], color='#0ea5e9', linewidth=5, solid_capstyle='round', zorder=6)

ax.text(1.15, 0.80, desc_title, color='#0ea5e9', fontsize=12, ha='left', va='center', fontweight='black', zorder=6)
ax.text(1.15, 0.45, desc_body, color='#334155', fontsize=10.5, ha='left', va='center', fontweight='bold', zorder=6)

plt.tight_layout()
plt.savefig('vte_diagram.png', bbox_inches='tight', transparent=False)
plt.close()
print("Sleek, high-fidelity premium VTE diagram successfully generated!")
