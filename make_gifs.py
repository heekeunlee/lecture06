import numpy as np
import matplotlib.pyplot as plt
import imageio
import os

# Set global matplotlib parameters to match the aesthetic
plt.rcParams['font.sans-serif'] = ['AppleGothic', 'Malgun Gothic', 'NanumGothic', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

colors = {
    'accent': '#0ea5e9',   # Sky blue
    'accent2': '#10b981',  # Emerald green
    'danger': '#ef4444',   # Red
    'warning': '#f59e0b',  # Amber/Orange
    'text': '#1e293b'      # Dark slate text
}

def create_gif(filename, make_frame, frames=20, fps=10, polar=False):
    images = []
    for i in range(frames):
        if polar:
            fig, ax = plt.subplots(figsize=(4.5, 3.8), dpi=110, subplot_kw=dict(projection='polar'))
        else:
            fig, ax = plt.subplots(figsize=(4.5, 3.4), dpi=110)
        
        # Set clean aesthetic backgrounds
        fig.patch.set_facecolor('#f8fafc')
        if not polar:
            ax.set_facecolor('#ffffff')
        
        make_frame(ax, i, frames)
        
        plt.tight_layout()
        fig.canvas.draw()
        image = np.asarray(fig.canvas.buffer_rgba())[..., :3]
        images.append(image)
        plt.close(fig)
        
    imageio.mimsave(filename, images, fps=fps, loop=0)
    print(f"Saved {filename}")

# Step 1: Selecting process (blinking node in a network)
def step1(ax, i, frames):
    ax.set_title("대상 설비 선택 (VTE-03)", fontsize=10, fontweight='bold', pad=8, color=colors['text'])
    ax.scatter([0, 1, 2], [1, 2, 1], c=['#cbd5e1', '#cbd5e1', '#cbd5e1'], s=150, zorder=3)
    alpha = (np.sin(i / frames * 2 * np.pi) + 1) / 2
    # Flash selected node
    ax.scatter([1], [2], c=[colors['accent']], s=250, alpha=alpha, zorder=4)
    ax.plot([0, 1], [1, 2], c='#cbd5e1', zorder=1, lw=2)
    ax.plot([1, 2], [2, 1], c='#cbd5e1', zorder=1, lw=2)
    
    ax.text(0, 0.7, "VTE-01 (정상)", ha='center', fontsize=8, fontweight='bold', color='#64748b')
    ax.text(1, 2.3, "VTE-03 (분석 선택)", ha='center', fontsize=8, fontweight='bold', color=colors['accent'])
    ax.text(2, 0.7, "VTE-05 (정상)", ha='center', fontsize=8, fontweight='bold', color='#64748b')
    
    ax.set_xlim(-0.5, 2.5)
    ax.set_ylim(0.2, 2.8)
    
    # Hide axes for node diagram
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

# Step 2: Normal monitoring (sine wave)
def step2(ax, i, frames):
    ax.set_title("VTE-03 실시간 압력 (정상 가동)", fontsize=10, fontweight='bold', pad=8, color=colors['text'])
    x = np.linspace(0, 10, 100)
    y = 1.02 + np.sin(x + i/frames * 2 * np.pi) * 0.05
    ax.plot(x, y, c=colors['accent2'], lw=2.2, label="챔버 압력 (측정값)")
    ax.axhline(1.85, c=colors['danger'], ls='--', lw=1.5, label="UCL 관리상한선 (1.85)")
    ax.set_ylim(0.5, 2.2)
    ax.set_xlabel("시간 (분)", fontsize=8, color='#475569')
    ax.set_ylabel("압력 (x10^-6 Torr)", fontsize=8, color='#475569')
    ax.tick_params(axis='both', which='major', labelsize=7.5)
    ax.grid(True, linestyle=':', alpha=0.5)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_color('#94a3b8')
    ax.spines['left'].set_color('#94a3b8')
    ax.legend(loc='lower left', fontsize=7.5, framealpha=0.9)

# Step 3: Anomaly (drift upwards)
def step3(ax, i, frames):
    ax.set_title("챔버 압력 상승 (이상 전조 발생)", fontsize=10, fontweight='bold', pad=8, color=colors['text'])
    x = np.linspace(0, 10, 100)
    # Drift increases over frames
    drift = (i/frames) * 0.75 * (x/10)
    y = 1.02 + np.sin(x*2) * 0.05 + drift
    ax.plot(x, y, c=colors['warning'], lw=2.2, label="챔버 압력 (측정값)")
    ax.axhline(1.85, c=colors['danger'], ls='--', lw=1.5, label="UCL 관리상한선 (1.85)")
    ax.set_ylim(0.5, 2.2)
    ax.set_xlabel("시간 (분)", fontsize=8, color='#475569')
    ax.set_ylabel("압력 (x10^-6 Torr)", fontsize=8, color='#475569')
    ax.tick_params(axis='both', which='major', labelsize=7.5)
    ax.grid(True, linestyle=':', alpha=0.5)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_color('#94a3b8')
    ax.spines['left'].set_color('#94a3b8')
    
    # Text annotation pointing to drift
    if i > frames // 4:
        ax.annotate("진공 미세 누설 시작 ↗", xy=(8.5, 1.02 + 0.65 * (i/frames)), xytext=(2.5, 1.55),
                    arrowprops=dict(arrowstyle="->", color=colors['warning'], lw=1.2),
                    fontsize=8.5, color=colors['warning'], fontweight='bold')
                    
    ax.legend(loc='lower left', fontsize=7.5, framealpha=0.9)

# Step 4: AI detection (pulse alert)
def step4(ax, i, frames):
    ax.set_title("AI 자동 검지 및 관리한계 이탈 판정", fontsize=10, fontweight='bold', pad=8, color=colors['text'])
    x = np.linspace(0, 10, 100)
    drift = 0.9 * (x/10)
    y = 1.02 + np.sin(x*2) * 0.05 + drift
    ax.plot(x, y, c=colors['danger'], lw=2.2, label="챔버 압력 (측정값)")
    ax.axhline(1.85, c=colors['danger'], ls='--', lw=1.5, label="UCL 관리상한선 (1.85)")
    ax.set_ylim(0.5, 2.2)
    ax.set_xlabel("시간 (분)", fontsize=8, color='#475569')
    ax.set_ylabel("압력 (x10^-6 Torr)", fontsize=8, color='#475569')
    ax.tick_params(axis='both', which='major', labelsize=7.5)
    ax.grid(True, linestyle=':', alpha=0.5)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_color('#94a3b8')
    ax.spines['left'].set_color('#94a3b8')
    
    # Highlight cross point
    intersection_x = 9.4
    intersection_y = 1.85
    ax.scatter([intersection_x], [intersection_y], c=colors['danger'], s=60, zorder=5)
    
    # Flashing alert ring
    alpha = (np.sin(i * np.pi / 2) + 1) / 2
    ax.scatter([intersection_x], [intersection_y], c=colors['danger'], s=160 * alpha, alpha=0.4 * alpha, zorder=4)
    
    ax.annotate("AI 실시간 자동 알람 발령!", xy=(intersection_x, intersection_y), xytext=(2.5, 1.45),
                arrowprops=dict(arrowstyle="->", color=colors['danger'], lw=1.2),
                fontsize=8.5, color=colors['danger'], fontweight='bold')
                
    ax.legend(loc='lower left', fontsize=7.5, framealpha=0.9)

# Step 5: Dashboard (radar signature animating)
def step5(ax, i, frames):
    ax.set_title("실시간 다차원 설비 서명 (상태 지문)", fontsize=10, fontweight='bold', pad=12, color=colors['text'])
    
    categories = ["냉각유량\n(Flow)", "챔버압력\n(Press)", "QCM속도\n(Rate)", "도가니온도\n(Temp)"]
    N = len(categories)
    
    # Compute angles for each category
    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles += angles[:1] # close the loop
    
    # Data values
    bars = [30, 88, 22, 95]
    current_values = [b * (i/frames) for b in bars]
    current_values += current_values[:1] # close the loop
    
    # Plot radar outline & fill
    ax.plot(angles, current_values, color=colors['danger'], lw=2.2, label="실시간 위험 서명")
    ax.fill(angles, current_values, color=colors['danger'], alpha=0.25)
    
    # Offset starting angle to top (12 o'clock)
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1) # clockwise
    
    # Set labels
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=8.5, fontweight='bold', color='#475569')
    
    # Radial ticks
    ax.set_rlabel_position(45) # put labels at 45 deg out of the way
    ax.set_yticks([25, 50, 75, 100])
    ax.set_yticklabels(["25%", "50%", "75%", "100%"], color="#94a3b8", fontsize=7.5)
    ax.set_ylim(0, 100)
    
    # Custom grid style
    ax.grid(True, color="#cbd5e1", linestyle="--", linewidth=0.7)
    
    # Add a normal range boundary polygon (e.g. at 40% risk for all variables)
    normal_boundary = [40] * (N + 1)
    ax.plot(angles, normal_boundary, color=colors['accent2'], lw=1.5, ls=':', label="정상 관리 한계")
    
    ax.legend(loc='lower center', bbox_to_anchor=(0.5, -0.28), fontsize=8, framealpha=0.9, ncol=2)

# Step 6: Engineer check (magnifying glass effect)
def step6(ax, i, frames):
    ax.set_title("정비 히스토리 정밀 매칭 (패턴 비교)", fontsize=10, fontweight='bold', pad=8, color=colors['text'])
    x = np.linspace(0, 10, 100)
    y = 1.2 + np.sin(x*1.5) * 0.2
    ax.plot(x, y, c='#64748b', lw=1.5, label="정상 이력 패턴")
    
    cx = 2 + (i/frames)*6
    cy = 1.2 + np.sin(cx*1.5) * 0.2
    
    # Magnifying glass circle
    circle = plt.Circle((cx, cy), 1.2, color=colors['accent'], fill=False, lw=2.5, zorder=5)
    ax.add_patch(circle)
    
    # Highlight segment inside magnifying glass
    mask = (x >= cx - 1.2) & (x <= cx + 1.2)
    ax.plot(x[mask], y[mask], c=colors['accent'], lw=3.0, zorder=4)
    
    ax.set_ylim(0.2, 2.2)
    ax.set_xlabel("과거 정비 데이터 타임라인", fontsize=8, color='#475569')
    ax.set_ylabel("패턴 매칭도", fontsize=8, color='#475569')
    ax.tick_params(axis='both', which='major', labelsize=7.5)
    ax.grid(True, linestyle=':', alpha=0.5)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_color('#94a3b8')
    ax.spines['left'].set_color('#94a3b8')
    ax.legend(loc='lower left', fontsize=7.5, framealpha=0.9)

# Step 7: Report sharing (sending arrow/nodes)
def step7(ax, i, frames):
    ax.set_title("정비 조치 지시서(SOP) 즉각 전송", fontsize=10, fontweight='bold', pad=8, color=colors['text'])
    ax.scatter([0.5, 2.5], [1, 1], c=[colors['accent'], colors['accent2']], s=180, zorder=3)
    ax.plot([0.5, 2.5], [1, 1], c='#cbd5e1', zorder=1, lw=2, ls='--')
    
    # Message packet moving
    progress = 0.5 + (i/frames) * 2.0
    ax.scatter([progress], [1], c=colors['danger'], s=80, zorder=4)
    
    ax.text(0.5, 0.7, "생산 제어부\n(SCADA/MES)", ha='center', va='top', fontsize=8, fontweight='bold', color='#475569')
    ax.text(2.5, 0.7, "현장 정비팀\n(SOP 실행)", ha='center', va='top', fontsize=8, fontweight='bold', color=colors['accent2'])
    
    ax.set_xlim(0, 3)
    ax.set_ylim(0.3, 1.7)
    
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

if __name__ == '__main__':
    create_gif('step1.gif', step1, frames=20, fps=10)
    create_gif('step2.gif', step2, frames=20, fps=10)
    create_gif('step3.gif', step3, frames=20, fps=10)
    create_gif('step4.gif', step4, frames=20, fps=10)
    create_gif('step5.gif', step5, frames=20, fps=10, polar=True)
    create_gif('step6.gif', step6, frames=20, fps=10)
    create_gif('step7.gif', step7, frames=20, fps=10)
