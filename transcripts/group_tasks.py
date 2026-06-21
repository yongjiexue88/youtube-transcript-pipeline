import os
import json

tasks_dir = "/Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/subagent_tasks"

# Get all task JSON files
task_files = sorted([f for f in os.listdir(tasks_dir) if f.startswith("task_") and f.endswith(".json")])

print(f"Found {len(task_files)} task files.")

# Group into 8 groups
num_groups = 8
group_size = (len(task_files) + num_groups - 1) // num_groups

for i in range(num_groups):
    group_tasks = task_files[i * group_size : (i + 1) * group_size]
    group_data = {
        "group_id": f"group_{i+1:02d}",
        "tasks": [os.path.join(tasks_dir, tf) for tf in group_tasks]
    }
    
    group_path = os.path.join(tasks_dir, f"group_{i+1:02d}.json")
    with open(group_path, 'w', encoding='utf-8') as f:
        json.dump(group_data, f, ensure_ascii=False, indent=2)
        
    print(f"Group {i+1}: {len(group_tasks)} tasks -> {group_path}")
