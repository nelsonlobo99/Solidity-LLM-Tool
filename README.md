# 🧠 Solidity LLM Tools

A simple yet powerful Streamlit app that provides two essential tools for interacting with Solidity smart contracts using local LLMs:

1. **Natural Language to Solidity Converter**
2. **Smart Contract Explanation Tool**

Built with 💡 **Streamlit**, 🧠 **Ollama (Gemma3:4b)**, and 🔗 **Etherscan API**.

---

## 🚀 Features

### 🛠️ Natural Language → Solidity

* Describe contract behavior in plain English.
* Get back Solidity code, an explanation, and security tradeoffs.
* Powered by a local LLM (Gemma3:4b via Ollama).

### 🔍 Explain Smart Contract

* Input a smart contract address (e.g., on Sepolia) or paste raw Solidity code.
* Fetches and analyzes verified contracts from Etherscan.
* Outputs a plain-English explanation, highlights key functions, permissions, and potential security concerns.

---

## 📦 Requirements

* Python 3.8+
* [Streamlit](https://streamlit.io/)
* [Ollama](https://ollama.com/) with the `gemma3:4b` model installed
* [Etherscan API Key](https://etherscan.io/apis) (for contract lookup)

---

## 🔧 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/solidity-llm-tools.git
cd solidity-llm-tools

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install streamlit requests
```

---

## 🔑 Setup

Set your Etherscan API key in your environment:

```bash
export ETHERSCAN_API_KEY=your_etherscan_api_key
```

Windows (PowerShell):

```powershell
$env:ETHERSCAN_API_KEY="your_etherscan_api_key"
```

Make sure you have [Ollama](https://ollama.com/) installed and the `gemma3:4b` model pulled:

```bash
ollama run gemma3:4b
```

---

## ▶️ Running the App

```bash
streamlit run app.py
```

---

---

🏗️ Build and Run Instructions

# Build the Docker image
```bash
docker build -t solidity-llm-tools .
```

# Run the container with Etherscan API key and Ollama model available
```bash
docker run -p 8501:8501 -e ETHERSCAN_API_KEY=your_etherscan_api_key \
    -v ~/.ollama:/root/.ollama \
    solidity-llm-tools
```

✅ Note:

This setup assumes Ollama has already pulled the gemma3:4b model locally on your host and is mounted into the container.

For GPU acceleration, you’d modify the Docker base image and runtime setup.

---

## 📁 File Structure

```
app.py               # Main Streamlit application
README.md            # Project documentation
requirements.txt     # Optional: for pip installs
```

---

## ⚠️ Notes

* The contract fetch tool is hardcoded for the **Sepolia** testnet. You can change this in `fetch_contract_source_from_etherscan()`.
* This app uses **local inference** via Ollama, so no OpenAI or cloud model access is required.

---

## 🧠 Example Prompts

**Natural Language to Solidity:**

> "Create a contract that lets users deposit Ether, and only the owner can withdraw."

**Explain a Contract:**

> Paste a contract address like `0x123...` or Solidity source code.

---

## 📈 Planned Improvements

Here are a few enhancements that can be done:

* 🔍 **RAG (Retrieval-Augmented Generation)** using the latest [Solidity documentation](https://docs.soliditylang.org) for more accurate and context-rich contract explanations.
* 🧠 **Agentic workflows**: Multi-step reasoning and tool use (e.g., static analysis + spec generation).
* 🧪 **Formal verification hooks**: Integrate tools like Slither or MythX to flag vulnerabilities in contract logic.
* 📚 **Multi-source enrichment**: Combine contract data from multiple explorers (e.g., Sepolia, Goerli, Mainnet).
* 🗂️ **Project-based prompt memory**: Remember previously generated contracts and explanations in the session.
* 🌐 **Better testnet/network support**: Expand contract fetching to support all major Ethereum testnets.

