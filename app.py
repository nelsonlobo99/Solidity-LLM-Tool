
import streamlit as st
import subprocess
import requests
import os

ETHERSCAN_API_KEY = os.getenv("ETHERSCAN_API_KEY")  # Set this in your environment

def fetch_contract_source_from_etherscan(address: str, network: str = "sepolia") -> str:
    """Fetches verified source code of a smart contract from Etherscan."""
    base_url = f"https://api-sepolia.etherscan.io/api"
    params = {
        "module": "contract",
        "action": "getsourcecode",
        "address": address,
        "apikey": ETHERSCAN_API_KEY,
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    if data["status"] == "1" and data["result"][0]["SourceCode"]:
        return data["result"][0]["SourceCode"]
    else:
        return f"// No verified source code found for address {address} on {network}"

def explain_contract(solidity_code: str) -> str:
    prompt = f"""Analyze the following smart contract code:
{solidity_code}

Output a plain-English explanation:
1. What the contract does.
2. Key functions and permissions.
3. Security concerns.
"""
    result = subprocess.run(
        ["ollama", "run", "gemma3:4b"],
        input=prompt,
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout

# Streamlit App UI
st.title("🧠 Solidity LLM Tools")

tab1, tab2 = st.tabs(["🛠️ NL → Solidity", "🔍 Explain Smart Contract"])

with tab1:
    st.header("Convert Natural Language to Solidity")
    nl_input = st.text_area("Describe the contract logic (natural language)", height=150)
    if st.button("Generate Solidity"):
        if nl_input:
            with st.spinner("Generating Solidity code..."):
                result = subprocess.run(
                    ["ollama", "run", "gemma3:4b"],
                    input=f"""Instruction: {nl_input}
                    Output format:
                    [Solidity Code]
                    [Explanation]
                    [Security Tradeoffs]""",
                    capture_output=True,
                    text=True,
                    check=True,
                )
                st.code(result.stdout, language="solidity")

with tab2:
    st.header("Explain a Smart Contract")
    st.markdown("You can either enter a **contract address** (e.g., Sepolia testnet) or paste **raw Solidity code** below.")

    contract_input = st.text_area("Input (contract address or Solidity code)", height=150)
    explain_btn = st.button("Explain Contract")

    if explain_btn:
        if contract_input.startswith("0x") and len(contract_input) == 42:
            with st.spinner("Fetching contract source from Etherscan..."):
                solidity_code = fetch_contract_source_from_etherscan(contract_input)
        else:
            solidity_code = contract_input

        with st.spinner("Analyzing contract..."):
            explanation = explain_contract(solidity_code)
            st.markdown("### Explanation")
            st.text(explanation)
