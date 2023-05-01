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

2. Download the [latest release](https://github.com/Significant-Gravitas/Auto-GPT/releases/latest)
3. Follow the [installation instructions][docs/setup]
4. Configure any additional features you want, or install some [plugins][docs/plugins]
5. [Run][docs/usage] the app

Please see the [documentation][docs] for full setup instructions and configuration options.

[docs]: https://significant-gravitas.github.io/Auto-GPT/

## 📖 Documentation
* [⚙️ Setup][docs/setup]
* [💻 Usage][docs/usage]
* [🔌 Plugins][docs/plugins]
* Configuration
  * [🔍 Web Search](https://significant-gravitas.github.io/Auto-GPT/configuration/search/)
  * [🧠 Memory](https://significant-gravitas.github.io/Auto-GPT/configuration/memory/)
  * [🗣️ Voice (TTS)](https://significant-gravitas.github.io/Auto-GPT/configuration/voice/)
  * [🖼️ Image Generation](https://significant-gravitas.github.io/Auto-GPT/configuration/imagegen/)

[docs/setup]: https://significant-gravitas.github.io/Auto-GPT/setup/
[docs/usage]: https://significant-gravitas.github.io/Auto-GPT/usage/
[docs/plugins]: https://significant-gravitas.github.io/Auto-GPT/plugins/

## ⚠️ Limitations

This experiment aims to showcase the potential of GPT-4 but comes with some limitations:

1. Not a polished application or product, just an experiment
2. May not perform well in complex, real-world business scenarios. In fact, if it actually does, please share your results!
3. Quite expensive to run, so set and monitor your API key limits with OpenAI!

## 🛡 Disclaimer

This project, Auto-GPT, is an experimental application and is provided "as-is" without any warranty, express or implied. By using this software, you agree to assume all risks associated with its use, including but not limited to data loss, system failure, or any other issues that may arise.

The developers and contributors of this project do not accept any responsibility or liability for any losses, damages, or other consequences that may occur as a result of using this software. You are solely responsible for any decisions and actions taken based on the information provided by Auto-GPT.

**Please note that the use of the GPT-4 language model can be expensive due to its token usage.** By utilizing this project, you acknowledge that you are responsible for monitoring and managing your own token usage and the associated costs. It is highly recommended to check your OpenAI API usage regularly and set up any necessary limits or alerts to prevent unexpected charges.

As an autonomous experiment, Auto-GPT may generate content or take actions that are not in line with real-world business practices or legal requirements. It is your responsibility to ensure that any actions or decisions made based on the output of this software comply with all applicable laws, regulations, and ethical standards. The developers and contributors of this project shall not be held responsible for any consequences arising from the use of this software.

By using Auto-GPT, you agree to indemnify, defend, and hold harmless the developers, contributors, and any affiliated parties from and against any and all claims, damages, losses, liabilities, costs, and expenses (including reasonable attorneys' fees) arising from your use of this software or your violation of these terms.

## 🐦 Connect with Us on Twitter

Stay up-to-date with the latest news, updates, and insights about Auto-GPT by following our Twitter accounts. Engage with the developer and the AI's own account for interesting discussions, project updates, and more.

- **Developer**: Follow [@siggravitas](https://twitter.com/siggravitas) for insights into the development process, project updates, and related topics from the creator of Entrepreneur-GPT.
- **Entrepreneur-GPT**: Join the conversation with the AI itself by following [@En_GPT](https://twitter.com/En_GPT). Share your experiences, discuss the AI's outputs, and engage with the growing community of users.

We look forward to connecting with you and hearing your thoughts, ideas, and experiences with Auto-GPT. Join us on Twitter and let's explore the future of AI together!

<p align="center">
  <a href="https://star-history.com/#Torantulino/auto-gpt&Date">
    <img src="https://api.star-history.com/svg?repos=Torantulino/auto-gpt&type=Date" alt="Star History Chart">
  </a>
</p>
