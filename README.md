# 🚀 promql-cli

A command-line interface for querying Prometheus using PromQL.

## ✨ Features

- ⚡ Execute PromQL queries directly from your terminal
- 📊 Display results in a readable format
- 🤖 Easy integration into scripts and automation

## 📦 Installation

Install the required Python packages:

```bash
pip install -r requirements.txt
```

## ⚙️ Configuration

You must either set the Prometheus server host in a `config.json` file or provide it using the `-e`/`--endpoint` flag.

- To use a config file, create `config.json` in the project directory with the following content:
  ```json
  {
    "host": "http://127.0.0.1:9090"
  }
  ```
- Or, specify the endpoint directly with the `-e` flag.

## 🛠️ Usage

```bash
python3 main.py --human <query> --endpoint http://localhost:9090
```
or, using `config.json`:
```bash
python3 main.py --human <query>
```

### 📝 Options

- `--human` or `-H`: Show in a human-readable format
- `--endpoint` or `-e`: Prometheus server URL (overrides `config.json`)
- `--help` or `-h`: Show help message

## 💡 Example

```bash
python3 main.py -H -e http://127.0.0.1:9090 node_memory_Active_bytes
```
or, with `config.json`:
```bash
python3 main.py -H node_memory_Active_bytes
```

## 📋 Requirements

- 🐍 Python 3.7+
- 📈 Prometheus server

## 🤝 Contributing

Contributions are welcome! Please open issues or submit pull requests.

## Future plans

- Add setup.py
- Normal authentication and tls

