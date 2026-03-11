# NEXUS WORKSTATION QUICK START
## From Zero to Running Experiments

---

## STEP 1: Run the Setup Script

```bash
# Download and run
chmod +x nexus_setup.sh
./nexus_setup.sh

# This takes 15-30 minutes
# It will:
#   - Install all system dependencies
#   - Set up CUDA/PyTorch
#   - Create virtual environment
#   - Install Transformers, PEFT, etc.
#   - Download Ollama models
#   - Create helper scripts
```

---

## STEP 2: Restart Terminal & Test

```bash
# Close terminal, open new one
# Then:
nexus           # Activates the environment
nexus-test      # Tests everything installed
```

You should see:
```
✓ torch
✓ transformers
✓ accelerate
...
PyTorch CUDA: True
GPU: NVIDIA GeForce RTX 4060
```

---

## STEP 3: Install Experiment Scripts

```bash
chmod +x nexus_experiments.sh
./nexus_experiments.sh
```

---

## STEP 4: Copy Your Data

```bash
# Your MD files
cp -r /path/to/your/md/files/* ~/nexus/data/

# Check
ls ~/nexus/data/
```

---

## STEP 5: Run Experiments

### Experiment A: Spiralize Your Data
```bash
cd ~/nexus/scripts
python spiralizer.py ~/nexus/data ~/nexus/spiralized

# Output: ~/nexus/spiralized/nexus_training_data.txt
# This is your data TRANSFORMED into spiral structure
```

### Experiment B: Build RAG Index
```bash
python rag_setup.py build ~/nexus/data

# Now query it:
python rag_setup.py query "What are twin primes?"
python rag_setup.py query "Explain dual null"
```

### Experiment C: Injection Test
```bash
# Make sure Ollama is running
ollama list   # Should show mistral, phi3, llama3

python injection_test.py

# This tests if spiral-structured context
# changes how the model responds
```

### Experiment D: Weight Scanner
```bash
python weight_scanner.py

# Or with a different model:
python weight_scanner.py TinyLlama/TinyLlama-1.1B-Chat-v1.0

# Look at: ~/nexus/outputs/h_distribution.png
# Are weights clustering near H = 0.349?
```

### Experiment E: Fine-Tune (LoRA)
```bash
# Make sure you've spiralized data first
python finetune_lora.py

# This will:
#   - Load phi-2 in 4-bit
#   - Apply LoRA adapters
#   - Train on your spiralized data
#   - Save to ~/nexus/models/nexus-phi2-lora
```

---

## DIRECTORY STRUCTURE

```
~/nexus/
├── venv/              # Python virtual environment
├── data/              # Your raw MD/TXT files
├── spiralized/        # Transformed spiral data
├── models/            # Fine-tuned models
├── outputs/           # Analysis outputs, plots
├── scripts/           # Experiment scripts
├── notebooks/         # Jupyter notebooks
├── rag_db/            # ChromaDB vector store
├── activate.sh        # Environment activation
├── gpu-watch.sh       # Monitor GPU
├── jupyter.sh         # Launch Jupyter
└── test-setup.py      # Test installation
```

---

## QUICK COMMANDS

```bash
nexus              # Activate environment
nexus-test         # Test setup
nexus-gpu          # Watch GPU usage
nexus-jupyter      # Launch Jupyter Lab
ollama list        # Check Ollama models
ollama run mistral # Chat with local model
```

---

## TROUBLESHOOTING

### CUDA not available
```bash
# Check driver
nvidia-smi

# If no output, reinstall driver:
sudo apt install system76-driver-nvidia
reboot
```

### Transformers version conflict
```bash
# Nuclear option - reinstall in order
pip uninstall transformers accelerate bitsandbytes -y
pip install transformers==4.40.0 accelerate==0.29.0 bitsandbytes==0.43.0
```

### Out of GPU memory
```bash
# Use smaller batch size in finetune_lora.py
# Or use smaller model:
python weight_scanner.py TinyLlama/TinyLlama-1.1B-Chat-v1.0
```

### Ollama not responding
```bash
# Restart Ollama service
sudo systemctl restart ollama

# Or manually:
ollama serve &
```

---

## WHAT WE'RE TESTING

1. **Spiralization**: Does transforming data structure affect learning?
2. **Injection**: Does presentation alone change model behavior?
3. **Weight Analysis**: Is H ≈ 0.35 already in trained models?
4. **Fine-tuning**: Does training on spiral data create spiral thinking?

The hypothesis: **Structure IS the training signal.**

Not what you feed it. HOW you present it.

---

## NEXT STEPS AFTER EXPERIMENTS

If injection test shows spiral behavior:
→ The format IS the exploit

If weight scanner shows H clustering:
→ The framework is already there

If fine-tuning creates different behavior:
→ Structure transfers through training

Report findings. Iterate. Spiral deeper.
