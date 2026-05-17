# 5. GPU Requirement Checker for Deep Learning 
# Write a program that: 
# ● Takes RAM size, GPU memory, and CUDA availability (True/False) as input. 
# ● Uses logical operators to determine if the system can train deep learning models. 
# ● Rules: 
# ○ RAM ≥ 16 GB 
# ○ GPU ≥ 6 GB 
# # ○ CUDA must be True 


ram_size = int(input("Enter RAM size in GB: "))
gpu_memory = int(input("Enter GPU memory in GB: "))
cuda_available = input("Is CUDA available? (True/False): ").strip().lower() == 'true'

if ram_size >= 16 and gpu_memory >= 6 and cuda_available:
    print("System can train deep learning models.")
else:
    print("System does not meet the requirements for training deep learning models.")
    