import numpy as np
import matplotlib.pyplot as plt
import imageio
import os

# Set global matplotlib parameters to match the aesthetic
plt.rcParams['font.sans-serif'] = ['sans-serif']
plt.rcParams['axes.facecolor'] = '#f8f9fa'
plt.rcParams['figure.facecolor'] = '#f8f9fa'

colors = {
    'accent': '#0071e3',
    'accent2': '#22c55e',
    'danger': '#ef4444',
    'warning': '#f59e0b',
    'text': '#1d1d1f'
}

def create_gif(filename, make_frame, frames=20, fps=10):
    images = []
    for i in range(frames):
        fig, ax = plt.subplots(figsize=(3, 2), dpi=100)
        make_frame(ax, i, frames)
        
        ax.set_xticks([])
        ax.set_yticks([])
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)
        
        plt.tight_layout()
        fig.canvas.draw()
        image = np.asarray(fig.canvas.buffer_rgba())[..., :3]
        images.append(image)
        plt.close(fig)
        
    imageio.mimsave(filename, images, fps=fps, loop=0)
    print(f"Saved {filename}")

# Step 1: Selecting process (blinking node in a network)
def step1(ax, i, frames):
    ax.scatter([0, 1, 2], [1, 2, 1], c=['#ccc', '#ccc', '#ccc'], s=200)
    alpha = (np.sin(i / frames * 2 * np.pi) + 1) / 2
    ax.scatter([1], [2], c=[colors['accent']], s=300, alpha=alpha)
    ax.plot([0, 1], [1, 2], c='#ccc', zorder=0)
    ax.plot([1, 2], [2, 1], c='#ccc', zorder=0)
    ax.set_xlim(-0.5, 2.5)
    ax.set_ylim(0, 3)

# Step 2: Normal monitoring (sine wave)
def step2(ax, i, frames):
    x = np.linspace(0, 10, 100)
    y = np.sin(x + i/frames * 2 * np.pi) * 0.2
    ax.plot(x, y, c=colors['accent2'], lw=3)
    ax.set_ylim(-1, 1)

# Step 3: Anomaly (drift upwards)
def step3(ax, i, frames):
    x = np.linspace(0, 10, 100)
    # Drift increases over time frames
    drift = (i/frames) * (x/10)
    y = np.sin(x*2) * 0.1 + drift
    ax.plot(x, y, c=colors['warning'], lw=3)
    # UCL line
    ax.axhline(0.8, c=colors['danger'], ls='--', lw=2)
    ax.set_ylim(-0.5, 1.2)

# Step 4: AI detection (pulse alert)
def step4(ax, i, frames):
    x = np.linspace(0, 10, 100)
    y = np.sin(x) * 0.1 + (x/10)
    ax.plot(x, y, c=colors['danger'], lw=3)
    ax.axhline(0.8, c=colors['danger'], ls='--', lw=2)
    # Pulse red dot when crossing UCL
    if i > frames // 2:
        alpha = (np.sin(i * np.pi) + 1) / 2
        ax.scatter([8], [0.8], c=colors['danger'], s=300 * alpha, alpha=alpha)
    ax.set_ylim(-0.2, 1.2)

# Step 5: Dashboard (bars animating)
def step5(ax, i, frames):
    bars = [3, 5, 2, 8]
    current_bars = [b * (i/frames) for b in bars]
    ax.bar(range(len(bars)), current_bars, color=[colors['accent'], colors['warning'], colors['accent2'], colors['danger']])
    ax.set_ylim(0, 10)

# Step 6: Engineer check (magnifying glass effect)
def step6(ax, i, frames):
    x = np.linspace(0, 10, 100)
    y = np.sin(x) * 0.3
    ax.plot(x, y, c=colors['text'], lw=2)
    # Moving circle
    cx = 2 + (i/frames)*6
    cy = np.sin(cx) * 0.3
    circle = plt.Circle((cx, cy), 1, color=colors['accent'], fill=False, lw=3)
    ax.add_patch(circle)
    ax.set_ylim(-2, 2)

# Step 7: Report sharing (sending arrow/nodes)
def step7(ax, i, frames):
    ax.scatter([0, 2], [1, 1], c=[colors['accent'], colors['accent2']], s=300)
    progress = i/frames * 2
    if progress <= 2:
        ax.scatter([progress], [1], c=colors['danger'], s=150)
    ax.plot([0, 2], [1, 1], c='#ccc', zorder=0, ls='--')
    ax.set_xlim(-0.5, 2.5)
    ax.set_ylim(0, 2)

if __name__ == '__main__':
    create_gif('step1.gif', step1, frames=20, fps=10)
    create_gif('step2.gif', step2, frames=20, fps=10)
    create_gif('step3.gif', step3, frames=20, fps=10)
    create_gif('step4.gif', step4, frames=20, fps=10)
    create_gif('step5.gif', step5, frames=20, fps=10)
    create_gif('step6.gif', step6, frames=20, fps=10)
    create_gif('step7.gif', step7, frames=20, fps=10)
