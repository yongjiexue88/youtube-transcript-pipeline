import os
import json

channels = {
    "microconf": 1,
    "saasclub": 6,
    "robwalling": 8,
    "lennyspodcast": 7,
    "gregisenberg": 8,
    "saastr": 18
}

clean_base_dir = "/Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/clean_transcripts"
tasks_dir = "/Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/subagent_tasks"

os.makedirs(tasks_dir, exist_ok=True)

for channel, num_batches in channels.items():
    channel_dir = os.path.join(clean_base_dir, channel)
    if not os.path.exists(channel_dir):
        print(f"Directory {channel_dir} does not exist. Skipping.")
        continue
        
    files = sorted([f for f in os.listdir(channel_dir) if f.endswith(('.txt', '.md'))])
    total_files = len(files)
    batch_size = (total_files + num_batches - 1) // num_batches
    
    print(f"Channel '{channel}': {total_files} files -> {num_batches} batches (max {batch_size} files/batch)")
    
    for i in range(num_batches):
        batch_files = files[i * batch_size : (i + 1) * batch_size]
        task_data = {
            "task_id": f"{channel}_{i+1:02d}",
            "channel": channel,
            "files": batch_files,
            "output_file": f"/Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/clean_transcripts/{channel}/output_batch_{i+1:02d}.md"
        }
        
        task_path = os.path.join(tasks_dir, f"task_{channel}_{i+1:02d}.json")
        with open(task_path, 'w', encoding='utf-8') as f:
            json.dump(task_data, f, ensure_ascii=False, indent=2)
            
print("Subagent task generation completed.")
