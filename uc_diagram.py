import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 7))

# Draw system boundary
boundary = patches.Rectangle((0.2, 0.2), 0.6, 0.6, edgecolor='black', facecolor='none', lw=2)
ax.add_patch(boundary)
ax.text(0.5, 0.77, "Fullerton_Bird (fBird) System", fontsize=12, ha="center", fontweight="bold")

actors = {
    "Operator": (0.05, 0.65),
    "Remote Pilot": (0.05, 0.45),
    "System Engineer": (0.05, 0.25),
    "Satellite System": (0.95, 0.65),
    "Weather Data Service": (0.95, 0.45)
}

use_cases = {
    "Control UAVs": (0.4, 0.65),
    "Monitor UAV Status": (0.4, 0.5),
    "Process Sensor Data": (0.4, 0.35),
    "Transmit Data to Satellite": (0.6, 0.65),
    "Receive Weather Data": (0.6, 0.45)
}

# Draw actors
for actor, pos in actors.items():
    ax.text(pos[0], pos[1], f"{actor}", fontsize=10, ha="center", bbox=dict(facecolor="lightgray", edgecolor="black", boxstyle="round,pad=0.3"))

# Draw ovals to represent use cases
for use_case, pos in use_cases.items():
    ellipse = patches.Ellipse(pos, 0.18, 0.08, edgecolor='black', facecolor='white', lw=1.5)
    ax.add_patch(ellipse)
    ax.text(pos[0], pos[1], use_case, fontsize=10, ha="center", va="center")

# Draw connections between actors and use cases
connections = [
    ("Operator", "Control UAVs"),
    ("Remote Pilot", "Monitor UAV Status"),
    ("System Engineer", "Process Sensor Data"),
    ("Satellite System", "Transmit Data to Satellite"),
    ("Weather Data Service", "Receive Weather Data"),
    ("Monitor UAV Status", "Process Sensor Data"),  # Internal relation
    ("Process Sensor Data", "Transmit Data to Satellite")  # Internal relation
]

# Draw lines
for actor, use_case in connections:
    start = actors[actor] if actor in actors else use_cases[actor]
    end = use_cases[use_case]
    ax.plot([start[0], end[0]], [start[1], end[1]], 'k-', lw=1)

# Hide axes
ax.set_xticks([])
ax.set_yticks([])
ax.set_frame_on(False)

plt.show()

# For saving the diagram
file_path = ""
plt.savefig(file_path, dpi=300, bbox_inches='tight')
file_path
