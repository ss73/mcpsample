# MCPSample

MCPSample is a sample project demonstrating the use of the MCP (Modular Component Platform) architecture.

## Features

- Modular component structure
- Easy integration and extension
- Sample components for quick start

## Prerequisites
To use MCPSample, you need:

- An Azure AI agent configured to answer questions based on your existing knowledgebase
- A Python installation

## Getting Started

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/mcpsample.git
    cd mcpsample
    ```

2. **Call your own agent:**
To connect your agent, edit the `my_server.py` file to use your Azure AI agent's endpoint and credentials. Update the relevant sections to point to your knowledgebase and ensure authentication is configured. Refer to your agent's documentation for specific integration steps.

3. **Run the MCP server (e.g. in VS Code):**
If using Visual Studio Code, add the following in `mcp.json`in
the `.vscode` folder.
```json
{
	"servers": {
		"coarch": {
			"type": "stdio",
			"command": "<PATH TO PYTHON EXECUTABLE>",
			"args": [
				"<PATH TO SOURCE DIRECTORY>/my_server.py"
			]
		}
	},
	"inputs": []
}
```

## Usage

Interact with the agent using #coarch in the Github Copilot chat. Ask it
to create an RFC or review your documentation

## Contributing

Contributions are welcome! Please submit issues or pull requests for improvements.

## License

This project is licensed under the MIT License.