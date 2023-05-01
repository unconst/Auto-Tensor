# Auto-Tensor: An Autonomous Bittensor Experiment 

Auto-Tensor is a fork of Auto-GPT but with openai's engine removed and the bittensor network injected. Just like AutoGPT, the agent chains together LLM "thoughts", into an autononous agent which runs on your computer. 
The difference is that Auto-Tensor's thoughts come from a decentralized network of miners on the Bittensor network. 

## 🚀 Features

- 🌐 Internet access for searches and information gathering
- 💾 Long-term and short-term memory management
- 🧠 GPT-4 instances for text generation
- 🔗 Access to popular websites and platforms
- 🗃️ File storage and summarization with GPT-3.5
- 🔌 Extensibility with Plugins

## Quickstart

1. Install Bittensor
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/opentensor/bittensor/master/scripts/install.sh)"
```

2. Clone this repository and install it.
```
git clone https://github.com/unconst/Auto-Tensor.git
cd Auto-Tensor
python3 -m pip install -e .
```

3. Create a bittensor wallet. (Store your mnemonic safely.)
```
btcli new_coldkey
```

4. Run AutoTensor
```
./run.sh
```
